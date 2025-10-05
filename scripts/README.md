# R Scripts

This directory contains R scripts for statistical analysis.

## Files

### `LCA.R`
**Latent Class Analysis using poLCA**

Performs polytomous latent class analysis to identify behavioral profiles among adolescents based on sexual behavior survey responses.

**Key analyses:**
- Model selection (2-5 classes) using AIC, BIC, and entropy
- Optimal model: 4 latent classes
- Visualization of class probabilities
- Entropy R² calculation for classification quality

**Dependencies:** `dplyr`, `readr`, `poLCA`, `plotly`, `corrplot`, `RColorBrewer`, `depmixS4`, `mclust`, `ggplot2`, `reshape2`, `gridExtra`

**Input:** `Data/1_Preprocess/datos_preprocesados_lca.csv`  
**Output:** `Data/1_Preprocess/data_clustered.csv`, various plots

---

### `xgboost.R`
**Gradient Boosting & LASSO for Class Prediction**

Uses XGBoost and LASSO regression to predict latent class membership using individual and social network predictors.

**Key analyses:**
- XGBoost multi-class classification with 10-fold CV
- Feature importance ranking
- LASSO multinomial regression for feature selection
- Confusion matrix evaluation

**Dependencies:** `xgboost`, `tidyverse`, `caret`, `glmnet`, `Ckmeans.1d.dp`

**Input:**
- `Data/1_Preprocess/x_train.csv`
- `Data/1_Preprocess/y_train.csv`
- `Data/1_Preprocess/x_test.csv`
- `Data/1_Preprocess/y_test.csv`

---

### `missing_data_in_R.R`
**Missing Data Analysis in R**

Alternative approach to missing data analysis using R packages.

**Dependencies:** `dplyr`, `readr`, `poLCA`, `plotly`, `corrplot`, `RColorBrewer`

---

## Running the Scripts

### Prerequisites
Install required packages:
```r
Rscript ../install_R_packages.R
```

### Execution Order
1. **Data preprocessing** (done in Python notebooks)
2. **LCA.R** - Identify latent classes
3. **xgboost.R** - Predict class membership using predictors

### Working Directory
Scripts automatically set working directory to their location:
```r
current_working_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(current_working_dir)
```

**Note:** If running from command line, you may need to adjust paths manually.
