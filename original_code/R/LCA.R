library(dplyr)
library(readr)
library(poLCA)
library(plotly)
library(corrplot)
library(RColorBrewer)
library(depmixS4)
library(mclust)
#library(Hmisc)

current_working_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(current_working_dir)


datos_preprocesados_lca <- read_csv("../Datos/1_Preprocess/datos_preprocesados_lca.csv")
datos_preprocesados_fa <- read_csv("../Datos/1_Preprocess/datos_preprocesados_FA.csv")

rownames(datos_preprocesados_lca) <- datos_preprocesados_lca$ID
datos_preprocesados_lca <- datos_preprocesados_lca[,2:length(colnames(datos_preprocesados_lca))]

rownames(datos_preprocesados_fa) <- datos_preprocesados_fa$ID
datos_preprocesados_fa <- datos_preprocesados_fa[,2:length(colnames(datos_preprocesados_fa))]

correlacion <- round(cor(datos_preprocesados_fa),2)

corrplot(correlacion, type="upper", order="hclust",
         col=brewer.pal(n=8, name="RdYlBu"))

model_definition <- mix(list(Factor_1 ~ 1, 
                             Factor_2 ~ 1, 
                             Factor_3 ~ 1),
                        family = list(gaussian(), gaussian(), gaussian()), # should be indicated in the list.
                        data =datos_preprocesados_fa,
                        nstates = 5, #This is the number of classes
                        respstart=runif(30)
)
fit.mod <- fit(model_definition)   # Fit the model

summary(fit.mod)
fit.mod@posterior

entropy.R2 <- function(fit) {
  entropy <- function(p){ 
    aux = -p * log(p)
    resp = sum(aux[!is.na(aux)])
    return(resp)
    }
  error_prior <- entropy(fit@posterior) # Class proportions
  error_post <- mean(apply(fit@posterior, 1, entropy))
  R2_entropy <- (error_prior - error_post) / error_prior
  R2_entropy
}

entropy.R2(fit.mod)



# shows model fit (BIC) on y-axis and number of latent classes on x-axis
BIC = mclustBIC(datos_preprocesados_fa, 
                G=1:12) # G tells it how many latent classes to try 
plot(BIC) # different lines represent different assumptions about the covariance structure

BIC = mclustBIC(datos_preprocesados_lca, 
                G=1:9) # G tells it how many latent classes to try 
plot(BIC)

aic <- c()
bic <- c()
g <- c()
chi <- c()
entropy <- c()

poLCA.entropy.fix <- function (lc)
{
  K.j <- sapply(lc$probs, ncol)
  fullcell <- expand.grid(sapply(K.j, seq, from = 1))
  P.c <- poLCA.predcell(lc, fullcell)
  return(-sum(P.c * log(P.c), na.rm = TRUE))
}
#poLCA.entropy.fix(lca_1)

entropy.R2 <- function(fit) {
  entropy <- function(p) sum(-p * ifelse(log(p) == Inf | log(p) == -Inf, 0, log(p)))
  error_prior <- entropy(fit$P) # Class proportions
  error_post <- mean(apply(fit$posterior, 1, entropy))
  R2_entropy <- (error_prior - error_post) / error_prior
  R2_entropy
}
#entropy.R2(lca_1)

for (i in c(2,3,4,5)){
  lca_1 <- poLCA(cbind(Sex, Understand, Had_sex, Sex_within_a_year, Age_sex, 
                       Pregnancy_prevention, Sex_under_the_influence,
                       Sex_with_partner, Sex_stregthen_relationship, 
                       STD_preocupation, Partner_status, Avoid_pregnancy) ~ 1, 
                 maxiter=50000, nclass=i, 
                 nrep=10, data=datos_lca)
  
  aic <- c(aic, lca_1$aic)
  bic <- c(bic, lca_1$bic)
  g <- c(g, lca_1$Gsq)
  chi <- c(chi, lca_1$Chisq)
  entropy <- c(entropy, entropy.R2(lca_1))#poLCA.entropy.fix(lca_1))
}

x <- c(2:5)

data <- data.frame(x, aic, bic, g, chi)

ay <- list(
  overlaying = "y",
  side = "right",
  title = "<b>Chi^2</b> values")

fig <- plot_ly(data, x = ~x, y = ~aic, name = 'AIC', type = 'scatter', mode = 'lines+markers') 
fig <- fig %>% add_trace(y = ~bic, name = 'BIC', mode = 'lines+markers') 
fig <- fig %>% add_trace(y = ~g, name = 'Likehood Ratio', mode = 'lines+markers')
fig <- fig %>% add_trace(y = ~chi, name = 'Chi^2', mode = 'lines+markers', yaxis = 'y2')

fig <- fig %>% layout(
  title = "Performance Measures", yaxis2 = ay,
  xaxis = list(title="Number of Classes"),
  yaxis = list(title="<b>AIC, BIC, Likehood Radio</b> Values")
)
fig

fig2 <- plot_ly(x = x, y = entropy, type = 'scatter', mode = 'lines+markers')
fig2 <- fig2 %>% layout(
  title = "Absolute Entropy Measure",
  xaxis = list(title="Number of Classes"),
  yaxis = list(title="Entropy Values")
)
fig2

# Me quedo con 4 clases
lca_4 <- poLCA(cbind(Sex, Understand, Had_sex, Sex_within_a_year, Age_sex, 
                     Pregnancy_prevention, Sex_under_the_influence,
                     Sex_with_partner, Sex_stregthen_relationship, 
                     STD_preocupation, Partner_status, Avoid_pregnancy) ~ 1, 
               maxiter=50000, nclass=4, 
               nrep=10, data=datos_lca)
entropy.R2(lca_4)
lca_4$posterior
lca_4$predclass
plot(lca_4)

datos_preprocesados_lca['Class_LCA'] <- lca_4$predclass

write_csv(datos_preprocesados_lca, '../Datos/1_Preprocess/data_clustered.csv')

lca.plot.probs <- function(fit.mod, start, end) {
  require(gridExtra)
  require(grid)
  require(ggplot2)
  require(reshape2)
  #a<-lapply(1:length(fit.mod@response[[1]]), function(y) {
  #  sapply(fit.mod@response, function(x) x[[y]]@parameters$coefficients)
  #})
  #names(a)<-sapply(1:length(fit.mod@response[[1]]), function(y) as.character(fit.mod@response[[1]][[y]]@formula[[2]]))
  a <- fit.mod$probs
  g<-grid::gList()
  for(i in start:end) {
    g[[i-start + 1]]<- ggplotGrob(ggplot(melt(a[[i]]), aes(paste("Class", rev(Var1) ), value, fill=as.factor(Var2), label=round(value, 2)))+
                          geom_col()+geom_text(position=position_stack(vjust=0.5))+coord_flip()+scale_fill_brewer(type="seq", palette=i)+
                          labs(x="", y="", title=names(a)[i], fill="Categories")+theme_minimal())
  }
  grid.arrange(grobs=g, nrow=end -start + 1 )
}
lca.plot.probs(lca_4, 12, 12)
ggsave('12_classes.png')

aux <- melt(lca_4$probs[[1]])
aux <- aux %>%
  mutate(Var2 = case_when(
    Var2 == 'Pr(1)' ~ 'Man',
    Var2 == 'Pr(2)' ~ 'Woman',
    Var2 == 'Pr(3)' ~ 'Other',
  ))
  

ggplot(aux, aes(gsub(': ','',rev(Var1)), value, fill=as.factor(Var2), label=round(value, 2)))+
  geom_col()+geom_text(position=position_stack(vjust=0.5))+coord_flip()+scale_fill_brewer(type="seq", palette=i)+
  labs(x="", y="Percentage", title=names(lca_4$probs)[1], fill="Categories")+theme_minimal()
ggsave('sex_classes.png')

aux <- melt(lca_4$probs[[2]])
aux <- aux %>%
  mutate(Var2 = case_when(
    Var2 == 'Pr(1)' ~ 'Yes',
    Var2 == 'Pr(2)' ~ 'No'
  ))


ggplot(aux, aes(gsub(': ','',rev(Var1)), value, fill=as.factor(Var2), label=round(value, 2)))+
  geom_col()+geom_text(position=position_stack(vjust=0.5))+coord_flip()+scale_fill_brewer(type="seq", palette=i)+
  labs(x="", y="Percentage", title=names(lca_4$probs)[2], fill="Categories")+theme_minimal()

ggsave('understands_classes.png')

library(depmixS4)

model_definition <- mix(list(Sex ~ 1, 
                             Understand ~ 1, 
                             Had_sex ~ 1,
                             Sex_within_a_year ~ 1,
                             Age_sex ~ 1,
                             Pregnancy_prevention ~ 1,
                             Sex_under_the_influence ~ 1,
                             Sex_with_partner ~ 1,
                             Sex_stregthen_relationship ~ 1,
                             STD_preocupation ~ 1, 
                             Pregnancy_preocupation ~ 1,
                             Partner_status ~ 1, 
                             Avoid_pregnancy ~ 1),
                        family = list(multinomial("identity"), #For every corresponding 
                                      multinomial("identity"),  #  indicator a family of distribution 
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity"),
                                      multinomial("identity")), # should be indicated in the list.
                        data =datos_lca,
                        nstates = 5, #This is the number of classes
                        respstart=runif(210)
)
fit.mod <- fit(model_definition)   # Fit the model






