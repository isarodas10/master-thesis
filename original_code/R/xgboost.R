install.packages("xgboost")
install.packages("tidyverse")
install.packages("caret")
install.packages('glmnet')

library("xgboost")
library("tidyverse")
library("caret")
library(glmnet)

current_working_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(current_working_dir)


X_train <- as.data.frame(read_csv("x_train.csv"))
X_train <- X_train[, -1]
names <- colnames(X_train)
Y_train <- as.data.frame(read_csv("y_train.csv"))
Y_train <- Y_train[, -1]

X_test <- as.data.frame(read_csv("x_test.csv"))
X_test <- X_test[, -1]
Y_test <- as.data.frame(read_csv("y_test.csv"))
Y_test <- Y_test[, -1]

# GXBOOST -----------------------------------------------------------------


X_train <- X_train %>% 
  as.matrix() %>% 
  xgb.DMatrix(data = ., label = Y_train)

numberOfClasses <- length(unique(Y_train))
xgb_params <- list("objective" = "multi:softprob",
                   "eval_metric" = "mlogloss",
                   "num_class" = numberOfClasses)
nround    <- 200 # number of XGBoost rounds
cv.nfold  <- 10

# Fit cv.nfold * cv.nround XGB models and save OOF predictions
cv_model <- xgb.cv(params = xgb_params,
                   data = X_train, 
                   nrounds = nround,
                   nfold = cv.nfold,
                   verbose = FALSE,
                   prediction = TRUE)

OOF_prediction <- data.frame(cv_model$pred) %>%
  mutate(max_prob = max.col(., ties.method = "last"),
         label = Y_train + 1)
head(OOF_prediction)

confusionMatrix(factor(OOF_prediction$max_prob),
                factor(OOF_prediction$label),
                mode = "everything")

bst_model <- xgb.train(params = xgb_params,
                       data = X_train,
                       nrounds = nround)

# Predict hold-out test set
test_pred <- predict(bst_model, newdata = as.matrix(X_test))
test_prediction <- matrix(Y_test, nrow = numberOfClasses,
                          ncol=length(test_pred)/numberOfClasses) %>%
  t() %>%
  data.frame() %>%
  mutate(label = Y_test + 1,
         max_prob = max.col(., "last"))
# confusion matrix of test set
confusionMatrix(factor(test_prediction$max_prob),
                factor(test_prediction$label),
                mode = "everything")
# compute feature importance matrix
importance_matrix = xgb.importance(feature_names = names, model = bst_model)
head(importance_matrix)


library("Ckmeans.1d.dp")
gp = xgb.ggplot.importance(importance_matrix)
print(gp) 



# LASSO -------------------------------------------------------------------
cvfit = cv.glmnet(X_train,Y_train,type.measure="class",alpha=1,family="multinomial")
coef(cvfit, s = "lambda.min")

