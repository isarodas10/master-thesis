# Individual Attributes and Social Network Predictors for Sexual Behaviour Profiles Among Adolescents in a Rural Area

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)

**Master's Thesis Research Repository**  
*Isabella Rodas*

> 🕐 **Timeline Note:** The original analysis was conducted in **2021** as part of my master's thesis research. This repository was organized and documented for public showcase in **October 2025**. The original analysis code is preserved in the `original_code/` directory.

---

## 📋 Abstract

This research investigates sexual behavior profiles among adolescents (ages 13-17) in a rural area, examining how individual attributes and social network characteristics predict membership in distinct behavioral profiles. Using a comprehensive analytical approach combining **Factor Analysis**, **8 clustering algorithms**, and **4 predictive models** (Decision Tree, Random Forest, LASSO, XGBoost), we identify **5 robust behavioral profiles** and analyze their predictors using both survey data and social network metrics from Gephi.

### Key Findings
- **5 distinct behavioral profiles** identified through Factor Analysis + Clustering
- **Social network variables dominate** the top 15 predictors (8/15 are network measures)
- **Network position** (centrality, clustering, community) is crucial for prediction
- **Convergence across methods**: K-Means, BIRCH, and Gaussian Mixture all identified 5 clusters
- **Individual + social context**: Both behavioral attributes and network position matter

---

## 🎯 Research Questions

1. What distinct sexual behavior profiles exist among rural adolescents?
2. How do individual attributes (age, gender, partnership status) predict profile membership?
3. How do social network characteristics (centrality, community) predict behavior profiles?
4. What is the relationship between risk perception and behavioral profiles?

---

## 📊 Methodology

### Data Collection
- **Sample:** 242 adolescents (ages 13-17) from rural schools
- **Survey:** 15 questions covering sexual behavior, attitudes, and risk perception
- **Social Network:** Friendship nomination data analyzed in Gephi
- **Ethics:** IRB approved, fully anonymized data

### Analytical Approach

```
┌─────────────────────────────────────────────────────────────┐
│                    Analysis Pipeline                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Initial Exploration (Notebook 1)                        │
│     ├── Survey question definitions                         │
│     ├── Missing data patterns visualization                 │
│     ├── Demographics & distributions                        │
│     └── Correlation analysis (motivation for FA)            │
│                                                             │
│  2. Data Cleaning (Notebook 2)                              │
│     ├── Filter participants >50% missing                    │
│     ├── Skip logic application (negative coding)            │
│     ├── Categorical variable recoding (12 operations)       │
│     └── MICE imputation                                     │
│                                                             │
│  3. Factor Analysis & Clustering (Notebook 3)               │
│     ├── Bartlett's & KMO tests (data suitability)           │
│     ├── Factor extraction (Kaiser criterion)                │
│     ├── 8 clustering methods tested:                        │
│     │   • Affinity Propagation, Agglomerative, BIRCH        │
│     │   • OPTICS, K-Means, Mean Shift                       │
│     │   • Spectral, Gaussian Mixture Model                  │
│     ├── 3 evaluation indices:                               │
│     │   • Silhouette, Calinski-Harabasz, Davies-Bouldin     │
│     └── Result: 5 clusters (K-Means, BIRCH, Gaussian agree) │
│                                                             │
│  4. Susceptibility Models (Notebook 4)                      │
│     ├── Data integration:                                   │
│     │   • 23 behavioral questions (literature-based)        │
│     │   • 8 network variables (from Gephi)                  │
│     │   • 5 cluster labels (target)                         │
│     ├── Train/test split (70/30, stratified)                │
│     ├── 4 models: Decision Tree, Random Forest,             │
│     │            LASSO, XGBoost                             │
│     └── Feature importance extraction                       │
│                                                             │
│  5. Cluster Profiling (Notebook 5)                          │
│     ├── Consolidate feature importance (4 models)           │
│     ├── Profile each of 5 clusters:                         │
│     │   • Demographics (age, sex)                           │
│     │   • Behavioral characteristics                        │
│     │   • Network position                                  │
│     ├── Radar charts for comparison                         │
│     └── Intervention implications                           │
│                                                             │
│  * Network Analysis (Gephi - external)                      │
│     ├── Friendship network from peer nominations            │
│     ├── 8 metrics: centrality, clustering, community        │
│     └── Export → merge with survey data                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Statistical Methods
- **Factor Analysis:** Extract latent dimensions from correlated behavioral variables
- **Varimax Rotation:** Orthogonal rotation for factor interpretability
- **Cronbach's Alpha:** Assess factor reliability
- **Multiple Clustering:** 8 algorithms for robust profile identification
- **Cluster Validation:** 3 evaluation metrics (Silhouette, Calinski-Harabasz, Davies-Bouldin)
- **Decision Tree:** Interpretable classification with feature importance
- **Random Forest:** Ensemble method for robust prediction
- **LASSO Regression:** L1 regularization for feature selection
- **XGBoost:** Gradient boosting for optimal performance
- **Network Analysis:** Gephi for social network metrics

---

## 🗂️ Repository Structure

```
master-thesis/
│
├── README.md                             # This file
├── LICENSE                               # MIT License
├── requirements.txt                      # Python dependencies
├── install_R_packages.R                  # R package installer
├── .gitignore                            # Git exclusions (protects sensitive data)
│
├── Data/                                 # Dataset (see Data/README.md)
│   ├── README.md                         # Data documentation & ethics
│   ├── 0_Raw/                            # Original data (git-ignored)
│   │   ├── 2. Participants attributes.xlsx
│   │   └── schoolanonymFINALAgosto2.csv
│   ├── 1_Preprocess/                     # Cleaned, analysis-ready data
│   │   ├── datos_preprocesados_FA.csv    # For Factor Analysis
│   │   ├── data_clustered.csv            # With cluster assignments
│   │   ├── x_train.csv, x_test.csv       # Features (train/test)
│   │   └── y_train.csv, y_test.csv       # Target (train/test)
│   └── Network_Gephi/                    # Social network files
│       └── red_positiva.gexf             # Gephi network file
│
├── notebooks/                            # Complete analysis workflow
│   ├── README.md                         # Notebook documentation
│   ├── 01_initial_data_exploration.ipynb # Survey, missing data, correlations
│   ├── 02_data_cleaning_preprocessing.ipynb # Filtering, recoding, imputation
│   ├── 03_factor_analysis_clustering.ipynb  # FA + 8 clustering methods
│   ├── 04_susceptibility_models.ipynb       # 4 predictive models
│   └── 05_cluster_profiling_interpretation.ipynb # Final profiles & insights
│
├── docs/                                 # Documentation
│   ├── methodology.md                    # Detailed analytical methods
│   └── data_dictionary.md                # Variable descriptions & coding
│
├── original_code/                        # Original 2021 analysis (preserved)
│   ├── Initial_data_exploration.ipynb
│   ├── Python/
│   │   ├── LCA Preprocessing.ipynb
│   │   └── lca.py
│   └── R/
│       ├── LCA.R                         # Explored but not used in final
│       ├── xgboost.R                     # Original modeling code
│       └── missing_data_in_R.R
│
├── Presentation_Spanish.pdf              # Defense slides (Dec 7, 2021)
├── Individual Attributes and Social Network Predictors....pdf  # Thesis PDF
│
├── SETUP.md                              # Setup instructions
├── MIGRATION_GUIDE.md                    # 2021→2025 organization notes
└── CHANGELOG_2025.md                     # Documentation of 2025 updates
```

---

## 🚀 Getting Started

### Prerequisites

**Python Requirements:**
- Python 3.9+
- Jupyter Notebook
- See `requirements.txt` for package list

**R Requirements:**
- R 4.0+
- RStudio (recommended)
- See `install_R_packages.R` for package list

**Optional:**
- Gephi (for network visualization)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/master-thesis.git
cd master-thesis
```

#### 2. Set Up Python Environment
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Set Up R Environment
```R
# Run from R console or RStudio
source("install_R_packages.R")
```

#### 4. Data Access
⚠️ **Important:** Raw data files are not included in this repository due to privacy concerns.

- Preprocessed, anonymized data is available in `Data/1_Preprocess/`
- For access to raw data, see `Data/README.md`
- To run the full pipeline, place raw data in `Data/0_Raw/`

---

## 📖 Usage

### Running the Analysis

The complete analysis is organized in **5 Jupyter notebooks** that should be run sequentially:

```bash
# Launch Jupyter
cd notebooks
jupyter notebook

# Run notebooks in order:
# 1. 01_initial_data_exploration.ipynb        - Survey structure & missing data
# 2. 02_data_cleaning_preprocessing.ipynb     - Filtering & imputation
# 3. 03_factor_analysis_clustering.ipynb      - FA + 8 clustering methods
# 4. 04_susceptibility_models.ipynb           - 4 predictive models
# 5. 05_cluster_profiling_interpretation.ipynb - Final cluster profiles
```

Each notebook is fully documented with:
- Clear section headers and markdown explanations
- Inline comments for code clarity
- Visualizations with interpretations
- Summary sections with key findings

### Accessing Original Code

The original 2021 analysis code is preserved in `original_code/`:

**Python (Jupyter):**
```python
# Original exploratory analysis
original_code/Initial_data_exploration.ipynb
original_code/Python/LCA Preprocessing.ipynb
```

**R (Scripts):**
```R
# From RStudio or R console
setwd("original_code/R/")

# Original LCA exploration (not used in final thesis)
source("LCA.R")

# Original predictive modeling
source("xgboost.R")
```

---

## 📈 Key Results

### Five Behavioral Profiles Identified

Through rigorous Factor Analysis and multi-algorithm clustering, we identified **5 distinct behavioral profiles**:

| Cluster | Size (n) | Description | Key Characteristics |
|---------|----------|-------------|---------------------|
| **Cluster 0** | 22 | **High-Risk Early Initiators** | Predominantly male (13-16 years), early sexual debut (10-13 years), risky behavior (no contraception, substance use during first sex), currently in relationships but haven't had sex with current partner yet expect to within the year despite not preferring it. Shows signs of peer pressure. |
| **Cluster 1** | 126 | **Abstinent/Uninitiated** | Predominantly female (13-15 years), majority in or have been in relationships, no sexual experience, do not expect to have sex within the next year. Represents over half the sample (55%). |
| **Cluster 2** | 42 | **Safe & Experienced** | Predominantly male (15-17 years), in relationships, older sexual debut (14+ years), consistent contraceptive use, no substance use during sex, sexually active with current partner, worried about STDs/pregnancy, expect to have sex willingly in next year. Practicing safe sex. |
| **Cluster 3** | 13 | **Private/Reluctant to Disclose** | Gender-balanced (51% male, 49% female, 15-16 years), in relationships, understand sexual intercourse but refuse to answer questions about sexual experience and future intentions. May find survey overwhelming or too private. |
| **Cluster 4** | 25 | **Uninformed/Limited Knowledge** | Young (13-15 years), 55% female, 45% male, some identify as other gender, in relationships or don't disclose status, **do not understand the term "sexual intercourse"**, zero knowledge about sex and what it entails. |

*Note: Detailed cluster profiles with demographic breakdowns, behavioral patterns, and network characteristics are available in **Notebook 5: Cluster Profiling & Interpretation**.*

**Key Insight:** The profiles range from high-risk early initiators (Cluster 0) to uninformed youth with zero sexual knowledge (Cluster 4), highlighting the need for **cluster-specific interventions** rather than one-size-fits-all approaches.

*(Complete thesis results: see PDF in repository)*

### Model Performance & Key Predictors

**Clustering Validation:**
- **Methods Tested:** 8 algorithms (Affinity Propagation, Agglomerative, BIRCH, OPTICS, K-Means, Mean Shift, Spectral, Gaussian)
- **Convergence:** K-Means, BIRCH, and Gaussian Mixture Model all identified 5 clusters
- **Evaluation:** 3 indices (Silhouette, Calinski-Harabasz, Davies-Bouldin)

**Predictive Model Results:**
- **4 Models:** Decision Tree, Random Forest, LASSO, XGBoost
- **Top Predictors (consolidated):** Network centrality metrics dominate (8/15 top predictors are network variables)
- **Key Finding:** Social network position is more predictive than traditional demographic/behavioral variables alone

**Most Important Variables:**
1. Network centrality (eigenvector, betweenness, closeness)
2. Network connectivity (in-degree, out-degree)
3. Community membership
4. Substance use patterns
5. Parental monitoring

---

## 🛠️ Technologies Used

### Languages & Frameworks
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

### Python Libraries
- **Data:** `pandas`, `numpy`, `openpyxl`
- **Factor Analysis:** `factor_analyzer`
- **Clustering:** `scikit-learn` (8 algorithms)
- **ML Models:** `scikit-learn` (Decision Tree, Random Forest, LASSO), `xgboost`
- **Stats:** `scipy`, `statsmodels`
- **Imputation:** `sklearn.impute.IterativeImputer` (MICE)
- **Viz:** `matplotlib`, `seaborn`, `missingno`

### R Packages (Original Code)
- **LCA Exploration:** `poLCA`, `depmixS4`, `mclust` *(explored but not used in final)*
- **ML:** `xgboost`, `caret`, `glmnet`
- **Viz:** `ggplot2`, `plotly`, `corrplot`

### Tools
- **Network Analysis:** Gephi (centrality, community detection)
- **Development:** Jupyter Notebook, Python 3.9+
- **Version Control:** Git & GitHub

---

## 🌐 Analysis Evolution: Original (2021) → Documented (2025)

### Original 2021 Workflow (Polyglot: Python + R)
The original thesis combined Python and R strategically:

| Task | Language | Tool/Package |
|------|----------|--------------|
| **Data Preprocessing** | Python | pandas, sklearn |
| **Exploratory Analysis** | Python | Jupyter notebooks |
| **LCA Exploration** | R | poLCA, depmixS4 *(explored alternative)* |
| **Predictive Modeling** | R | xgboost, glmnet |

### 2025 Documented Workflow (Python-Centric)
For clarity and reproducibility, the 2025 documentation implements the complete methodology in Python:

| Task | Implementation | Notebook |
|------|----------------|----------|
| **Data Exploration** | Python | Notebook 1 |
| **Data Cleaning** | Python | Notebook 2 |
| **Factor Analysis + Clustering** | Python (`factor_analyzer`, `sklearn`) | Notebook 3 |
| **Predictive Modeling** | Python (`sklearn`, `xgboost`) | Notebook 4 |
| **Cluster Profiling** | Python | Notebook 5 |

**Why Python?**
- **Reproducibility:** Single-language workflow easier to share and replicate
- **Documentation:** Jupyter notebooks provide inline explanations
- **Modern Stack:** All major ML/stats methods available in Python
- **Accessibility:** Lower barrier for future researchers

**Original R Code:** Preserved in `original_code/` for reference and validation

---

## 📚 Documentation

- **[Data Dictionary](docs/data_dictionary.md)** - Variable descriptions & coding
- **[Methodology](docs/methodology.md)** - Detailed analytical methods
- **[Thesis PDF](Individual%20Attributes%20and%20Social%20Network%20Predictors%20for%20Sexual%20Behaviour%20Pro%20les%20Among%20Adolescents%20in%20a%20Rural%20Area.pdf)** - Complete thesis document
- **[Defense Slides](Presentation_Spanish.pdf)** - Thesis defense presentation (December 7th, 2021) *(in Spanish)*

---

## 🔒 Ethics & Privacy

This research was conducted with full ethical approval and adheres to:
- ✅ IRB/ethics committee approval
- ✅ Parental consent + adolescent assent
- ✅ Complete data anonymization
- ✅ Secure data storage
- ✅ No personally identifiable information

**Data Sharing:** Raw data is not publicly available to protect participant privacy. Anonymized, aggregated data may be shared upon reasonable request and with appropriate ethical approval.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Isabella Rodas**  
Master's Student | Universidad de los Andes  
📧 Email: [isabella.rodas.arango@gmail.com](mailto:isabella.rodas.arango@gmail.com)  
🔗 LinkedIn: [Isabella Rodas Arango](https://www.linkedin.com/in/isabella-rodas-arango/)  
🐦 GitHub: [@isarodas10](https://github.com/isarodas10)

---

## 🙏 Acknowledgments

- Thesis advisor: Felipe Montes and Ana María Guerra 
- Institución Educativa Santa Ana and its students in Barú, Colombia
- IsBaru project participants and collaborators

---

## 📖 Citation

If you use this research, methodology, or code, please cite:

```bibtex
@mastersthesis{rodas2025sexual,
  author  = {Isabella Rodas},
  title   = {Individual Attributes and Social Network Predictors for Sexual 
             Behaviour Profiles Among Adolescents in a Rural Area},
  school  = {Universidad de los Andes},
  year    = {2021},
  type    = {Master's Thesis},
  url     = {https://github.com/isarodas10/master-thesis}
}
```

---

## 🗺️ Roadmap & Future Work

- [ ] Longitudinal follow-up study
- [ ] Extended network analysis (negative ties)
- [ ] Machine learning interpretability (SHAP values)
- [ ] Intervention program development
- [ ] Publication in peer-reviewed journal

---

*Last Updated: October 2025*