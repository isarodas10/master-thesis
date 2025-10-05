# Comprehensive Notebook Series - FINAL PLAN
## Based on Actual Thesis Methodology (2021)

This notebook series follows the exact methodology from Isabella Rodas's master's thesis at Universidad de los Andes.

---

## 📓 Notebook 1: Initial Data Exploration
**File:** `01_initial_data_exploration.ipynb`

### Content:
1. **Setup & Imports**
2. **Load Survey Data** (N=242 adolescents, Barú, Colombia)
3. **Survey Questions Documentation**
   - 15 questions on sexual behavior, attitudes, risk perceptions
   - Spanish questions with English translations
4. **Missing Data Analysis**
   - Missing data matrix (missingno)
   - Percentage missing by variable
   - Patterns and structure
5. **Demographic Overview**
   - Age distribution (13-17 years)
   - Sex/gender distribution
   - Partnership status
6. **Key Variable Distributions**
   - Sexual understanding and experience
   - Risk perceptions
   - Protection behaviors
7. **Correlation Analysis**
   - Spearman correlations (ordinal data)
   - Identify highly correlated variables → motivation for Factor Analysis

**Output:** Understanding of data structure, high correlation among variables

---

## 📓 Notebook 2: Data Cleaning & Preprocessing
**File:** `02_data_cleaning_preprocessing.ipynb`

### Content:
1. **Load Raw Data**
2. **Handle Missing Data**
   - Systematic skip logic
   - Imputation strategies (MICE)
3. **Variable Recoding**
   - Collapse categories for parsimony
   - Standardize scales
   - Map age codes to actual ages
4. **Data Quality Checks**
   - Distribution checks after cleaning
   - Verify consistency
5. **Export Clean Data**
   - Save `datos_preprocesados_FA.csv` for Factor Analysis

**Output:** `Data/1_Preprocess/datos_preprocesados_FA.csv`

---

## 📓 Notebook 3: Factor Analysis & Clustering (MAIN ANALYSIS)
**File:** `03_factor_analysis_clustering.ipynb`

### Content:

#### Part A: Factor Analysis Suitability Tests
1. **Bartlett's Test of Sphericity**
   - Tests if correlation matrix is identity matrix
   - H₀: Variables are uncorrelated
   - If p < 0.05 → Factor Analysis is appropriate
2. **Kaiser-Meyer-Olkin (KMO) Test**
   - Measures sampling adequacy
   - KMO > 0.6: acceptable, >0.8: excellent
3. **Correlation Matrix**
   - Visualize high correlations justifying FA

#### Part B: Factor Analysis
4. **Extract Factors**
   - Principal Component Analysis or Maximum Likelihood
   - Eigenvector analysis
   - Scree plot
5. **Determine Optimal Number of Factors**
   - Kaiser criterion (eigenvalue > 1)
   - Scree plot elbow
   - Variance explained
6. **Factor Rotation** (if applicable)
   - Varimax or Promax rotation
7. **Factor Loadings**
   - Interpret factors based on loadings
8. **Cronbach's Alpha**
   - Validate internal consistency of each factor
   - α > 0.7 is acceptable

#### Part C: Clustering on Factors
9. **Prepare Factor Scores**
   - Extract factor scores for each participant
10. **Apply 8 Clustering Methods:**
    - **Affinity Propagation**
    - **Agglomerative Clustering**
    - **BIRCH** ✓
    - **OPTICS**
    - **K-Means** ✓
    - **Mean Shift**
    - **Spectral Clustering**
    - **Gaussian Mixture Model** ✓
11. **Evaluate Each Method with 3 Indices:**
    - **Silhouette Score** (how similar objects are within clusters)
    - **Calinski-Harabasz Index** (ratio of between/within cluster dispersion)
    - **Davies-Bouldin Index** (average similarity between clusters)
12. **Compare Methods**
    - Table of all scores
    - Identify best performing methods
13. **Final Clustering Selection**
    - K-Means, BIRCH, and Gaussian all produce same 5 clusters
    - Use these 5 clusters as final grouping
14. **Characterize 5 Clusters**
    - Cluster sizes
    - Factor score profiles
    - Behavioral characteristics
    - Demographics by cluster

**Output:** 
- Factor loadings and interpretation
- 5 final clusters (from K-Means/BIRCH/Gaussian)
- Cluster assignments for each participant

---

## 📓 Notebook 4: Social Network Analysis Integration
**File:** `04_network_analysis.ipynb`

### Content:
1. **Load Network Data from Gephi**
   - Friendship network files (.gexf)
   - Network metrics extracted in Gephi
2. **Network Metrics**
   - Degree centrality
   - Betweenness centrality
   - Closeness centrality
   - Eigenvector centrality
   - Community detection
3. **Merge with Cluster Assignments**
   - Combine network metrics with 5 behavioral clusters
4. **Network Patterns by Cluster**
   - Average centrality by cluster
   - Network position and sexual behavior profiles
   - Visualizations
5. **Prepare for Susceptibility Modeling**
   - Create predictor matrix: demographics + network metrics
   - Target variable: cluster assignment

**Output:** 
- Integrated dataset with clusters + network metrics
- Understanding of network-behavior relationships

---

## 📓 Notebook 5: Susceptibility Models
**File:** `05_susceptibility_models.ipynb`

### Content:
1. **Define Susceptibility**
   - Which clusters represent "risky sexual behavior"?
   - Binary or multi-class classification
2. **Feature Engineering**
   - Individual attributes (age, sex, partnership)
   - Network metrics (centrality, community)
   - Factor scores
3. **Train/Test Split**
   - 80/20 split, stratified sampling
4. **Model 1: Decision Tree**
   - Train decision tree classifier
   - Visualize tree
   - Feature importance
   - Performance metrics
5. **Model 2: Random Forest**
   - Ensemble of decision trees
   - Feature importance (mean decrease impurity)
   - Out-of-bag error
   - Performance metrics
6. **Model 3: LASSO Regression**
   - Regularized linear/logistic model
   - Cross-validation for λ selection
   - Feature selection (non-zero coefficients)
   - Performance metrics
7. **Model Comparison**
   - Accuracy, Precision, Recall, F1
   - ROC curves and AUC
   - Confusion matrices
8. **Feature Importance Analysis**
   - Which variables predict risky behavior?
   - Compare across all 3 models
   - Network vs. individual predictors
9. **Key Findings**
   - Most susceptible clusters
   - Most important predictive variables
   - Practical implications

**Output:**
- Model performance comparison
- Feature importance rankings
- Understanding of susceptibility predictors

---

## 🔗 Complete Workflow

```
Data Collection (2021, Barú)
         ↓
Notebook 1: Initial Exploration
         ↓
Notebook 2: Data Cleaning
         ↓
    Export CSV
         ↓
Notebook 3: Factor Analysis
         ↓
    8 Clustering Methods
         ↓
    Choose best 3 (K-Means, BIRCH, Gaussian)
         ↓
    5 Final Clusters
         ↓
         ↓ ← Gephi Network Analysis
         ↓
Notebook 4: Network Integration
         ↓
Notebook 5: Susceptibility Models
         ↓
Final Results & Thesis
```

---

## 📊 Key Datasets

| File | Created By | Used By | Purpose |
|------|------------|---------|---------|
| Raw survey | Data collection | NB1, NB2 | Input |
| `datos_preprocesados_FA.csv` | NB2 | NB3 | Factor analysis input |
| Factor scores | NB3 | NB3 clustering | Clustering input |
| Network files (.gexf) | Gephi | NB4 | Network metrics |
| Clustered data + network | NB4 | NB5 | Susceptibility modeling |

---

## 🎯 What Makes This Showcase-Quality

1. ✅ **Follows Actual Thesis** - Exact methodology from your defense
2. ✅ **Rigorous Statistical Testing** - Bartlett, KMO, Cronbach's Alpha
3. ✅ **Comprehensive Clustering** - 8 methods, 3 evaluation indices
4. ✅ **Multiple Models** - Decision Tree, Random Forest, LASSO
5. ✅ **Clear Documentation** - Every step explained with theory
6. ✅ **Professional Visualizations** - Publication-ready plots
7. ✅ **Reproducible** - Complete workflow from raw data to results
8. ✅ **Bilingual** - Spanish questions + English analysis

---

## 📝 Notes

- **LCA exploration:** Was attempted but didn't work for this data (see `original_code/`)
- **Final method:** Factor Analysis + Clustering (K-Means/BIRCH/Gaussian agree on 5 clusters)
- **Thesis defense:** December 7th, 2021, Universidad de los Andes
- **Repository organization:** October 2025

---

*This plan now accurately reflects your master's thesis methodology!*