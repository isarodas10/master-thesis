# Analysis Notebooks - Complete Workflow

This directory contains the **complete analysis pipeline** in 5 comprehensive Jupyter notebooks, presenting the 2021 master's thesis research in a reproducible format.

> **Timeline:** Original analysis conducted in 2021. Notebooks created/documented in October 2025 for reproducibility and professional showcase.

---

## 📊 The 5-Notebook Analysis Pipeline

### Workflow Overview

```
Data Flow:
  Raw Survey → Notebook 1 → Notebook 2 → Notebook 3 → Notebook 4 → Notebook 5
  (Explore)    (Clean)      (Cluster)    (Predict)    (Profile)
```

**Run notebooks sequentially:** Each builds on outputs from the previous.

---

## 📓 Notebook 1: Initial Data Exploration

**File:** `01_initial_data_exploration.ipynb`

**Purpose:** Understand the survey data structure and motivate Factor Analysis

**Contents:**
- 📋 **Survey Questions:** Bilingual definitions (English/Spanish) of all 15 questions
- 🔍 **Missing Data Patterns:** Visualization using `missingno` (70-85% missing due to skip logic)
- 👥 **Demographics:** Age and sex distributions
- 📊 **Key Variables:** Distributions of understanding, sexual experience, intentions
- 🔗 **Correlation Analysis:** Spearman correlations showing high multicollinearity
- 💡 **Motivation:** Why Factor Analysis is needed (reduce correlated variables)

**Key Outputs:**
- Missing data visualizations
- Demographic summaries
- Correlation heatmap (motivation for FA)

**Next Step:** → Notebook 2 (Data Cleaning)

---

## 🧹 Notebook 2: Data Cleaning & Preprocessing

**File:** `02_data_cleaning_preprocessing.ipynb`

**Purpose:** Prepare data for Factor Analysis following exact thesis methodology

**Contents:**
1. **Load Survey Data** (242 participants, 15 questions)
2. **Missing Data Patterns** (raw visualization)
3. **Filter Participants:**
   - ⚠️ Remove participants with >50% missing behavioral data
   - Visualization: Red/blue bar chart with 50% threshold line
4. **Skip Logic Application:**
   - 10 rules with negative value coding (-1 to -7)
   - Systematic vs. true missing distinction
5. **Categorical Recoding:**
   - 12 variable recodings (binary, ordinal collapsed)
   - Examples: Age sex outliers, pregnancy prevention, STD preoccupation
6. **MICE Imputation:**
   - Multivariate Imputation by Chained Equations
   - For remaining true missing values
7. **Export Clean Data:**
   - Output: `../Data/1_Preprocess/datos_preprocesados_FA.csv`

**Key Implementation:** Exactly follows 2021 thesis cleaning workflow

**Key Outputs:**
- `datos_preprocesados_FA.csv` (ready for Factor Analysis)
- Missing data summary table
- Recoding verification tables

**Next Step:** → Notebook 3 (Factor Analysis & Clustering)

---

## 🔬 Notebook 3: Factor Analysis & Clustering

**File:** `03_factor_analysis_clustering.ipynb`

**Purpose:** Extract latent dimensions and identify 5 behavioral profiles

**Contents:**

### Part A: Data Suitability Tests
- **Bartlett's Test:** Variables sufficiently correlated? (p < 0.05 ✓)
- **KMO Test:** Sampling adequate? (KMO > 0.6 ✓)

### Part B: Factor Analysis
- **Factor Extraction:**
  - Kaiser criterion (eigenvalues > 1)
  - Scree plot & cumulative variance
  - Varimax rotation for interpretability
- **Factor Loadings:** Identify variables strongly associated with each factor
- **Cronbach's Alpha:** Assess factor reliability
- **Factor Scores:** Extract for clustering

### Part C: Clustering on Factor Scores
**8 Algorithms Tested:**
1. Affinity Propagation
2. Agglomerative Clustering
3. BIRCH
4. OPTICS
5. K-Means
6. Mean Shift
7. Spectral Clustering
8. Gaussian Mixture Model

**Cluster Numbers Tested:** k = 3, 4, 5, 6, 7

**3 Evaluation Metrics:**
1. Silhouette Score (higher = better)
2. Calinski-Harabasz Index (higher = better)
3. Davies-Bouldin Index (lower = better)

### Part D: Final Selection
- **Result:** K-Means, BIRCH, and Gaussian **all identified 5 clusters**
- **Interpretation:** Robust, algorithm-independent solution
- **Visualization:** Cluster profiles in factor space

**Key Outputs:**
- Factor scores for all participants
- 5 cluster assignments (Gaussian Mixture used)
- Evaluation metrics for all configurations
- Cluster visualization

**Next Step:** → Notebook 4 (Susceptibility Models)

---

## 🎯 Notebook 4: Susceptibility Models

**File:** `04_susceptibility_models.ipynb`

**Purpose:** Identify predictors of cluster membership using machine learning

**Contents:**

### Data Integration (Explained!)
Shows how three data sources were merged:
1. **23 Behavioral Questions** (literature-selected)
   - Categorized: Demographics, attitudes, substance use, knowledge
2. **8 Social Network Variables** (from Gephi)
   - Centrality, clustering, community, connectivity
3. **5 Cluster Labels** (from Notebook 3)
   - Target variable for prediction

**Total:** 31 features → predicting 5 clusters

### Train/Test Split
- 70% training (172 participants)
- 30% test (58 participants)
- Stratified by cluster

### Four Predictive Models

#### 1. Decision Tree
- Interpretable rules
- Feature importance
- Tree visualization (top 3 levels)

#### 2. Random Forest
- Ensemble of 200 trees
- Robust to overfitting
- Feature importance

#### 3. LASSO Regression
- L1 regularization
- Feature selection (some coefficients → 0)
- Identifies most predictive variables

#### 4. XGBoost
- Gradient boosting
- Often best performance
- Feature importance (gain-based)

### Model Comparison
- Accuracy (train vs. test)
- Overfitting assessment
- Confusion matrices (all 4 models)
- Feature importance consolidation

**Key Findings:**
- **Social network variables dominate** top predictors
- All models successfully predict cluster membership
- Different models agree on key predictors

**Key Outputs:**
- Model performance comparison
- Feature importance rankings
- Confusion matrices

**Next Step:** → Notebook 5 (Cluster Profiling)

---

## 📈 Notebook 5: Cluster Profiling & Interpretation

**File:** `05_cluster_profiling_interpretation.ipynb`

**Purpose:** Characterize the 5 clusters and provide actionable insights

**Contents:**

### 1. Cluster Overview
- Distribution (pie + bar charts)
- Sample sizes: n=22, 126, 42, 13, 25

### 2. Consolidated Feature Importance
- Averages importance across all 4 models
- Ranks top 20 predictors
- Categorizes: Network vs. Behavioral
- **Finding:** 8/15 top predictors are network variables!

### 3. Demographic Profiling
- Age distribution by cluster
- Sex distribution by cluster
- Statistical summaries

### 4. Network Characteristics
- Mean network metrics per cluster
- Heatmap visualization (8 network variables × 5 clusters)

### 5. Behavioral Characteristics
- Top 10 behavioral predictors per cluster
- Heatmap visualization

### 6. Radar Charts
- Visual comparison across clusters
- Top 8 predictive variables
- Normalized 0-1 scale

### 7. Cluster Interpretations

**Cluster 0 (n=22): High-Risk Early Initiators**
- Males 13-16, early debut (10-13 years)
- Risky behaviors, peer pressure indicators

**Cluster 1 (n=126): Abstinent/Uninitiated**
- Largest group (55%)
- Females 13-15, no sexual experience

**Cluster 2 (n=42): Safe & Experienced**
- Males 15-17, practicing safe sex
- Consistent contraceptive use

**Cluster 3 (n=13): Private/Reluctant to Disclose**
- Gender-balanced, refuse to answer questions

**Cluster 4 (n=25): Uninformed/Limited Knowledge**
- Young 13-15, don't understand "sexual intercourse"

### 8. Key Findings Summary
- 5 distinct profiles identified
- Network position crucial for prediction
- Intervention implications

**Key Outputs:**
- Comprehensive cluster profiles
- Feature importance rankings
- Visual comparisons (radar charts, heatmaps)
- Intervention recommendations

**Analysis Complete!** 🎉

---

## 🔄 Original Analysis Notebooks (2021)

The complete original analysis from 2021 is preserved in `/original_code/`:

### Python (Jupyter)
- `/original_code/Initial_data_exploration.ipynb` - Original exploratory analysis
- `/original_code/Python/LCA Preprocessing.ipynb` - Original preprocessing pipeline

### R (Scripts)
- `/original_code/R/LCA.R` - Latent Class Analysis exploration (not used in final)
- `/original_code/R/xgboost.R` - Original modeling code
- `/original_code/R/missing_data_in_R.R` - Missing data handling

**Note:** LCA was explored as an alternative but **Factor Analysis + Clustering** was used in the final thesis (as shown in these 5 notebooks).

---

## 🚀 Running the Notebooks

### Prerequisites
```bash
# Install dependencies
pip install -r ../requirements.txt

# Key packages:
# - pandas, numpy, openpyxl (data)
# - factor_analyzer (Factor Analysis)
# - scikit-learn (clustering, models)
# - xgboost (XGBoost model)
# - matplotlib, seaborn, missingno (visualization)
```

### Launch Jupyter
```bash
cd notebooks
jupyter notebook
```

### Execution Order (IMPORTANT!)

**Run sequentially** - each notebook depends on previous outputs:

1. **`01_initial_data_exploration.ipynb`**
   - Self-contained, explores raw data
   - No dependencies

2. **`02_data_cleaning_preprocessing.ipynb`**
   - Reads: `../Data/0_Raw/2. Participants attributes.xlsx`
   - Exports: `../Data/1_Preprocess/datos_preprocesados_FA.csv`

3. **`03_factor_analysis_clustering.ipynb`**
   - Reads: `datos_preprocesados_FA.csv`
   - Exports: Cluster assignments, factor scores

4. **`04_susceptibility_models.ipynb`**
   - Reads: Pre-prepared train/test data
     - `x_train.csv`, `x_test.csv` (features)
     - `y_train.csv`, `y_test.csv` (cluster labels)
   - Shows how data integration happened

5. **`05_cluster_profiling_interpretation.ipynb`**
   - Reads: Train/test data + cluster data
   - Produces: Final interpretations and profiles

### Tips
- **Run all cells** in each notebook before moving to next
- **Check outputs** are saved to `Data/1_Preprocess/`
- **Read markdown cells** for context and explanations
- Each notebook is **fully documented** with inline explanations

---

## 📂 Directory Structure

```
notebooks/
├── README.md                              # This file
├── 01_initial_data_exploration.ipynb      # Notebook 1
├── 02_data_cleaning_preprocessing.ipynb   # Notebook 2
├── 03_factor_analysis_clustering.ipynb    # Notebook 3
├── 04_susceptibility_models.ipynb         # Notebook 4
└── 05_cluster_profiling_interpretation.ipynb  # Notebook 5

Assumes this parent structure:
predictors-for-sexual-behaviour-profiles/
├── notebooks/          # You are here
├── Data/
│   ├── 0_Raw/         # Input data (git-ignored)
│   └── 1_Preprocess/  # Cleaned data (notebooks save here)
├── original_code/     # Original 2021 analysis
├── docs/              # Methodology documentation
└── README.md          # Main project overview
```

---

## 💡 Key Features

### Self-Contained Documentation
Each notebook includes:
- 📝 Introduction section with context
- 📋 Table of contents (for long notebooks)
- 💬 Extensive markdown explanations
- 📊 Inline visualizations
- ✅ Summary sections with key findings

### Reproducibility
- Clear execution order
- Explicit data paths
- All dependencies specified
- Outputs saved at each step

### Professional Quality
- Clean code with comments
- Consistent styling
- Publication-ready figures
- Comprehensive documentation

---

## 🎯 Quick Reference

**Total Participants:** 242 → 230 (after filtering)

**5 Clusters Identified:**
- Cluster 0: High-Risk Early Initiators (n=22)
- Cluster 1: Abstinent/Uninitiated (n=126)
- Cluster 2: Safe & Experienced (n=42)
- Cluster 3: Private/Reluctant to Disclose (n=13)
- Cluster 4: Uninformed/Limited Knowledge (n=25)

**Key Finding:** Social network position predicts behavior profiles more strongly than demographics alone.

**Methods Used:**
- Factor Analysis (Bartlett's, KMO, Varimax rotation)
- 8 Clustering Algorithms (K-Means, BIRCH, Gaussian, etc.)
- 3 Evaluation Metrics (Silhouette, Calinski-Harabasz, Davies-Bouldin)
- 4 Predictive Models (Decision Tree, Random Forest, LASSO, XGBoost)

---

## 📧 Questions?

- **Main README:** `../README.md` - Project overview
- **Setup Guide:** `../SETUP.md` - Installation & getting started
- **Methodology:** `../docs/methodology.md` - Detailed methods
- **Contact:** isabella.rodas.arango@gmail.com

---

*Notebooks created October 2025 | Original analysis 2021 | Thesis defense December 7th, 2021*