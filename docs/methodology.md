# Methodology

Detailed description of analytical methods used in this research.

---

## Table of Contents
1. [Study Design](#study-design)
2. [Data Collection](#data-collection)
3. [Data Preprocessing](#data-preprocessing)
4. [Factor Analysis](#factor-analysis)
5. [Clustering Methods](#clustering-methods)
6. [Predictive Modeling](#predictive-modeling)
7. [Network Analysis](#network-analysis)
8. [Cluster Profiling](#cluster-profiling)
9. [Validation & Evaluation](#validation--evaluation)

**Note:** This document describes the final methodology used in the thesis. The original 2021 analysis code (including LCA exploration) is preserved in `original_code/` but LCA was not used in the final thesis.

---

## Study Design

### Research Design
**Cross-sectional survey study** with social network analysis component.

### Sample
- **Population:** Adolescents (ages 13-17) attending rural schools
- **Sample size:** N = 242
- **Sampling:** Convenience sample from participating schools
- **Time period:** April 2019

### Inclusion Criteria
- Age 13-17 years
- Enrolled in participating schools
- Parental consent + adolescent assent
- Completed minimum 50% of survey questions

### Ethical Approval
- IRB/Ethics Committee: [Approval number]
- Parental consent obtained
- Adolescent assent obtained
- Data anonymization protocol followed

---

## Data Collection

### Survey Instrument

**15-item questionnaire** covering:

1. **Demographics** (2 items)
   - Age, sex/gender

2. **Sexual Understanding & Experience** (3 items)
   - Understanding of sexual intercourse
   - Sexual activity status
   - Age of first intercourse

3. **Contextual Factors** (3 items)
   - Substance use during first sex
   - Contraceptive use at first sex
   - Partnership status

4. **Partner-Specific Behaviors** (2 items)
   - Sexual activity with partner
   - Perceived relationship impact

5. **Risk Perceptions** (3 items)
   - STD concern
   - Pregnancy concern
   - Current contraceptive use

6. **Future Intentions** (1 item)
   - Likelihood of future sexual activity

**Response format:** Mix of binary, ordinal, and categorical responses

### Social Network Data

**Friendship nomination survey:**
- Participants nominated friends within school
- Directed network (A nominates B ≠ B nominates A)
- Network analyzed in Gephi software
- Metrics: centrality, community structure, degree

---

## Data Preprocessing

### 1. Missing Data Handling

**Strategy: Systematic categorization before imputation**

#### Step 1: Identify Missing Data Patterns
```python
# Categorize missingness reasons
Category 1: Does not understand sexual intercourse (skip logic)
Category 2: No response to understanding question
Category 3: Understands but no response to sexual activity
Category 4: Has not had sexual intercourse (skip logic)
Category 5: Refused to answer about sexual activity
Categories 6-8: Various partner-related skip patterns
```

#### Step 2: Code Systematic Skips
- Systematic skip patterns coded with negative values (-1 to -7)
- True missing data retained as NaN

#### Step 3: Imputation
- **Method:** MICE (Multivariate Imputation by Chained Equations)
- **Implementation:** `sklearn.impute.IterativeImputer`
- **Parameters:**
  - `max_iter=10`
  - `random_state=0` (reproducibility)
- **Training:** Fit on complete cases only
- **Application:** Transform incomplete cases
- **Post-processing:** Round to nearest integer (categorical data)

### 2. Response Recoding

#### Age Variable
```python
# Map coded responses to actual ages
{1.0: 13, 2.0: 14, 3.0: 15, 4.0: 16, 5.0: 17}
```

#### Categorical Reduction
Many variables collapsed from 6-11 categories to 2-3 categories:
- **Binary:** Yes/No/Other
- **Ordinal:** Low/Medium/High concern
- **Partner status:** Partner/No partner/Other

**Rationale:** Increase statistical power, reduce sparsity

### 3. Data Transformation

**Survey text decoding:**
- Original: Numeric codes
- Transformed: Text labels (for visualization)
- Preserved: Numeric codes (for modeling)

---

## Exploratory Clustering

### K-Modes Clustering

**Why K-modes?**
- Designed for **categorical data**
- Uses mode instead of mean
- Handles nominal variables appropriately

#### Initialization Methods Compared

**1. Cao Initialization**
```python
from kmodes.kmodes import KModes
km_cao = KModes(n_clusters=k, init='Cao', n_init=1, verbose=1)
clusters = km_cao.fit_predict(data)
```
- Deterministic initialization
- Selects most dissimilar modes
- Faster convergence

**2. Huang Initialization**
```python
km_huang = KModes(n_clusters=k, init='Huang', n_init=1, verbose=1)
clusters = km_huang.fit_predict(data)
```
- Random initialization with refinement
- Multiple restarts recommended
- Potentially better global optimum

#### Model Selection
- **Range tested:** k = 1 to 5 clusters
- **Criterion:** Cost function (within-cluster dissimilarity)
- **Method:** Elbow plot
- **Optimal k:** 4 clusters (both methods)

### DBSCAN Clustering

**Why DBSCAN?**
- Density-based clustering
- Identifies outliers (noise points)
- No need to specify k beforehand

#### Gower Distance
```python
import gower
distance_matrix = gower.gower_matrix(data)
```
**Why Gower?**
- Handles **mixed data types** (categorical + numeric)
- Normalized distance metric [0, 1]
- Appropriate for survey data

#### DBSCAN Parameters
```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=2, metric='precomputed')
clusters = dbscan.fit_predict(distance_matrix)
```
- `eps=0.3`: Maximum distance for density
- `min_samples=2`: Minimum cluster size
- `metric='precomputed'`: Use Gower distance matrix

---

## Latent Class Analysis

**Primary method for identifying behavioral profiles.**

### Why LCA?

- **Model-based clustering** for categorical data
- Estimates **probability of class membership**
- Provides **statistical fit indices** (AIC, BIC)
- Handles **measurement error**
- Identifies **unobserved subgroups**

### Implementation

**R Package:** `poLCA` (Polytomous Latent Class Analysis)

#### Model Specification
```r
library(poLCA)

formula <- cbind(Sex, Understand, Had_sex, Sex_within_a_year, 
                 Age_sex, Pregnancy_prevention, Sex_under_the_influence,
                 Sex_with_partner, Sex_stregthen_relationship, 
                 STD_preocupation, Partner_status, Avoid_pregnancy) ~ 1

lca_model <- poLCA(formula, 
                   data = datos_lca,
                   nclass = k,        # Number of classes
                   maxiter = 50000,   # Max iterations
                   nrep = 10,         # Restarts (avoid local maxima)
                   verbose = TRUE)
```

### Model Selection

**Classes tested:** k = 2, 3, 4, 5

**Evaluation criteria:**

1. **Akaike Information Criterion (AIC)**
   - Lower is better
   - Penalizes model complexity
   - Formula: AIC = -2 * log-likelihood + 2 * parameters

2. **Bayesian Information Criterion (BIC)**
   - Lower is better
   - Stronger complexity penalty than AIC
   - Formula: BIC = -2 * log-likelihood + log(n) * parameters

3. **Likelihood Ratio G²**
   - Goodness-of-fit statistic
   - Lower is better

4. **Entropy R²**
   - Classification certainty [0, 1]
   - Higher is better (>0.80 is good)
   - Formula: R² = (E_prior - E_post) / E_prior

**Entropy Calculation:**
```r
entropy.R2 <- function(fit) {
  entropy <- function(p) sum(-p * log(p), na.rm=TRUE)
  error_prior <- entropy(fit$P)           # Class proportions
  error_post <- mean(apply(fit$posterior, 1, entropy))
  R2_entropy <- (error_prior - error_post) / error_prior
  return(R2_entropy)
}
```

**Optimal model:** k = 4 classes
- Best balance of fit indices
- Interpretable class profiles
- Adequate entropy (>0.8)

### Class Interpretation

Classes interpreted based on:
- **Item-response probabilities** for each class
- **Conditional probabilities** P(response | class)
- **Class sizes** (prevalence)
- **Substantive meaning**

---

## Predictive Modeling

**Goal:** Predict latent class membership using individual and network predictors.

### Features

**Individual-level predictors:**
- Age
- Sex/gender
- Demographic characteristics

**Network-level predictors:**
- Degree centrality
- Betweenness centrality
- Community membership
- In-degree / Out-degree

### XGBoost (Gradient Boosting)

#### Why XGBoost?
- Handles **non-linear relationships**
- **Feature importance** ranking
- Excellent **predictive performance**
- Handles **mixed data types**

#### Implementation
```r
library(xgboost)
library(caret)

# Prepare data
X_train <- xgb.DMatrix(data = as.matrix(X_train), label = Y_train)

# Parameters
xgb_params <- list(
  "objective" = "multi:softprob",    # Multi-class classification
  "eval_metric" = "mlogloss",        # Log loss
  "num_class" = 4                     # 4 LCA classes
)

# Cross-validation
cv_model <- xgb.cv(
  params = xgb_params,
  data = X_train,
  nrounds = 200,
  nfold = 10,
  verbose = FALSE,
  prediction = TRUE
)

# Final model
bst_model <- xgb.train(params = xgb_params, 
                       data = X_train, 
                       nrounds = 200)
```

#### Feature Importance
```r
importance_matrix <- xgb.importance(feature_names = names, model = bst_model)
xgb.ggplot.importance(importance_matrix)
```

### LASSO Regression

#### Why LASSO?
- **Feature selection** via L1 regularization
- Shrinks unimportant coefficients to zero
- Interpretable results

#### Implementation
```r
library(glmnet)

# Cross-validated LASSO
cvfit <- cv.glmnet(
  x = X_train,
  y = Y_train,
  family = "multinomial",    # Multi-class
  type.measure = "class",     # Classification error
  alpha = 1                   # L1 penalty (LASSO)
)

# Extract coefficients at optimal lambda
coef(cvfit, s = "lambda.min")
```

### Evaluation

**Metrics:**
- **Accuracy:** Overall correct classification rate
- **Confusion matrix:** Class-specific performance
- **Precision, Recall, F1:** Per-class metrics
- **10-fold CV:** Cross-validation for generalizability

---

## Network Analysis

### Gephi Analysis

**Software:** Gephi 0.9.x

**Network type:** Directed friendship network

### Metrics Calculated

**Node-level metrics:**

1. **Degree Centrality**
   - Total connections (in + out)
   - Measures popularity

2. **In-Degree**
   - Incoming nominations
   - Measures prestige (being chosen)

3. **Out-Degree**
   - Outgoing nominations
   - Measures sociability (choosing others)

4. **Betweenness Centrality**
   - Number of shortest paths through node
   - Measures bridging role

5. **Closeness Centrality**
   - Average distance to all other nodes
   - Measures reach

6. **Eigenvector Centrality**
   - Connections to well-connected nodes
   - Measures influence

**Network-level metrics:**
- Community detection (modularity)
- Network density
- Average path length

---

## Validation & Evaluation

### Internal Validation

**LCA Model:**
- Bootstrap resampling (if applicable)
- Stability of class assignment
- Entropy > 0.80 threshold

**Clustering:**
- Silhouette scores (for numeric clusters)
- Cluster size balance
- Substantive interpretability

### External Validation

**Predictive Models:**
- 10-fold cross-validation
- Train/test split (80/20)
- Confusion matrix analysis

### Sensitivity Analyses

**Tested:**
- Different imputation methods
- Alternative cluster numbers
- Varying LCA starting values (nrep=10)
- Different distance metrics (Gower vs. others)

---

## Software & Reproducibility

### Python Environment
```bash
Python 3.9+
numpy==1.21.0
pandas==1.3.0
scikit-learn==0.24.0
kmodes==0.12.0
gower==0.1.2
```

### R Environment
```r
R version 4.0+
poLCA 1.4.1
xgboost 1.4.x
caret 6.0-x
glmnet 4.1-x
```

### Reproducibility
- **Random seeds set:** `random_state=0` (Python), `set.seed(123)` (R)
- **Version control:** Git
- **Environment:** `requirements.txt`, `install_R_packages.R`
- **Data:** Anonymized data preserved in `Data/1_Preprocess/`

---

## Limitations

### Methodological
- **Cross-sectional design:** Cannot infer causality
- **Self-report data:** Social desirability bias possible
- **Convenience sample:** Limited generalizability
- **Missing data:** Despite careful handling, may introduce bias

### Statistical
- **Small sample size:** Limited power for rare behaviors
- **Multiple testing:** No correction applied (exploratory)
- **Model assumptions:** LCA assumes local independence

### Social Network
- **Boundary specification:** Limited to school networks
- **Nomination limits:** May miss important ties
- **Unreciprocated ties:** Asymmetry interpretation challenges

---

## References

### Key Methods Papers

**Latent Class Analysis:**
- Linzer, D. A., & Lewis, J. B. (2011). poLCA: An R package for polytomous variable latent class analysis. *Journal of Statistical Software*, 42(10), 1-29.

**K-modes:**
- Huang, Z. (1998). Extensions to the k-means algorithm for clustering large data sets with categorical values. *Data Mining and Knowledge Discovery*, 2(3), 283-304.

**XGBoost:**
- Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. *Proceedings of the 22nd ACM SIGKDD*, 785-794.

**Missing Data:**
- van Buuren, S., & Groothuis-Oudshoorn, K. (2011). mice: Multivariate imputation by chained equations in R. *Journal of Statistical Software*, 45(3), 1-67.

---

*For implementation details, see code in `src/`, `scripts/`, and `notebooks/`.*
