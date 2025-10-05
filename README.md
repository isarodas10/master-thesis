# Individual Attributes and Social Network Predictors for Sexual Behaviour Profiles Among Adolescents in a Rural Area

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)

**Master's Thesis Research Repository**  
*Isabella Rodas*

> 🕐 **Timeline Note:** The original analysis was conducted in **2021** as part of my master's thesis research. This repository was organized and documented for public showcase in **October 2025**. The original analysis code is preserved in the `original_code/` directory.

---

## 📋 Abstract

This research investigates sexual behavior profiles among adolescents (ages 13-17) in a rural area, examining how individual attributes and social network characteristics predict membership in distinct behavioral profiles. Using a mixed-methods approach combining **Latent Class Analysis (LCA)**, **clustering algorithms**, and **gradient boosting models**, we identify 4 distinct behavioral profiles and analyze their predictors using both survey data and social network metrics.

### Key Findings
- **4 distinct behavioral profiles** identified through LCA
- **Social network position** significantly predicts profile membership
- **Age, gender, and partnership status** are key individual predictors
- **Risk perception** varies substantially across profiles

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
│                    Analysis Pipeline                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Data Preprocessing (Python)                              │
│     ├── Missing data analysis & imputation                   │
│     ├── Response recoding & standardization                  │
│     └── Variable transformation                              │
│                                                              │
│  2. Exploratory Clustering (Python)                          │
│     ├── K-modes clustering (Cao & Huang)                     │
│     ├── DBSCAN with Gower distance                           │
│     └── Cluster validation & comparison                      │
│                                                              │
│  3. Latent Class Analysis (R)                                │
│     ├── Model selection (2-5 classes)                        │
│     ├── Optimal model: 4 classes                             │
│     ├── AIC, BIC, Entropy evaluation                         │
│     └── Class probability estimation                         │
│                                                              │
│  4. Predictive Modeling (R)                                  │
│     ├── XGBoost multi-class classification                   │
│     ├── LASSO multinomial regression                         │
│     ├── Feature importance ranking                           │
│     └── 10-fold cross-validation                             │
│                                                              │
│  5. Network Analysis (Gephi)                                 │
│     ├── Centrality measures                                  │
│     ├── Community detection                                  │
│     └── Visual network mapping                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Statistical Methods
- **Latent Class Analysis (poLCA):** Identify unobserved behavioral profiles
- **K-modes Clustering:** Handle categorical survey data
- **DBSCAN:** Density-based clustering with mixed-type distance (Gower)
- **XGBoost:** Gradient boosting for profile prediction
- **LASSO Regression:** Feature selection with regularization
- **Spearman Correlation:** Assess relationships between ordinal variables

---

## 🗂️ Repository Structure

```
master-thesis/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── install_R_packages.R               # R package installer
├── .gitignore                         # Git exclusions
│
├── Data/                              # Dataset (see Data/README.md)
│   ├── README.md                      # Data documentation & ethics
│   ├── 0_Raw/                         # Original data (git-ignored)
│   ├── 1_Preprocess/                  # Cleaned, analysis-ready data
│   └── Network_Gephi/                 # Social network files (.gexf)
│
├── notebooks/                         # Jupyter notebooks (Python)
│   ├── README.md                      # Notebook documentation
│   └── 01_data_exploration.ipynb      # Initial data exploration
│
├── src/                               # Python modules
│   ├── __init__.py
│   ├── preprocessing.py               # Data cleaning functions
│   ├── clustering.py                  # K-modes, DBSCAN functions
│   ├── lca.py                         # Custom LCA implementation
│   └── visualization.py               # Plotting functions
│
├── scripts/                           # R scripts
│   ├── README.md                      # Script documentation
│   ├── LCA.R                          # Latent class analysis (poLCA)
│   ├── xgboost.R                      # XGBoost & LASSO modeling
│   └── missing_data_in_R.R            # Missing data handling in R
│
├── results/                           # Analysis outputs
│   ├── figures/                       # Plots and visualizations
│   ├── tables/                        # Summary statistics & results
│   └── models/                        # Saved model objects
│
├── docs/                              # Documentation
│   ├── methodology.md                 # Detailed methods
│   └── data_dictionary.md             # Variable descriptions
│
└── original_code/                     # Original 2021 analysis (preserved)
    ├── Initial_data_exploration.ipynb
    ├── Python/
    │   ├── LCA Preprocessing.ipynb
    │   └── lca.py
    └── R/
        ├── LCA.R
        ├── xgboost.R
        └── missing_data_in_R.R
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

#### Python Analysis (Notebooks)
```bash
# Launch Jupyter
cd notebooks
jupyter notebook

# Run notebooks in order:
# 1. 01_data_exploration.ipynb
# (See original notebooks in /Code for complete pipeline)
```

#### R Analysis (Scripts)
```R
# From RStudio or R console
setwd("scripts/")

# 1. Latent Class Analysis
source("LCA.R")

# 2. Predictive Modeling
source("xgboost.R")
```

### Using Custom Modules

**Python:**
```python
from src.preprocessing import iterative_impute, map_age_codes
from src.clustering import fit_kmodes, get_cluster_summary
from src.visualization import plot_correlation_heatmap

# Load and preprocess data
data = pd.read_csv('Data/1_Preprocess/data_clustered.csv')
data = map_age_codes(data)

# Fit K-modes clustering
model, clusters = fit_kmodes(data, n_clusters=4)
summary = get_cluster_summary(data, cluster_col='cluster')
```

**R:**
```R
# Load preprocessed data
data <- read_csv("Data/1_Preprocess/data_clustered.csv")

# Run LCA
lca_model <- poLCA(formula, data, nclass=4, nrep=10)
```

---

## 📈 Key Results

### Behavioral Profiles Identified

| Profile | Size | Description | Key Characteristics |
|---------|------|-------------|---------------------|
| **Profile 1** | n=XX | **Inexperienced/Abstinent** | No sexual experience, low future intent |
| **Profile 2** | n=XX | **Cautious/Protected** | Sexual experience with consistent protection |
| **Profile 3** | n=XX | **Risk-Taking** | Sexual experience with inconsistent protection |
| **Profile 4** | n=XX | **High-Risk** | Early initiation, substance use, low protection |

*(Full results in thesis document: see PDF in repository)*

### Model Performance

- **LCA Model Fit:** BIC = XXX, Entropy = 0.XX
- **XGBoost Accuracy:** XX% (10-fold CV)
- **Top Predictors:** Age, network centrality, partnership status

---

## 🛠️ Technologies Used

### Languages & Frameworks
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

### Python Libraries
- **Data:** `pandas`, `numpy`, `openpyxl`
- **Clustering:** `kmodes`, `scikit-learn`, `gower`
- **Stats:** `scipy`, `statsmodels`
- **Viz:** `matplotlib`, `seaborn`, `plotly`, `missingno`

### R Packages
- **LCA:** `poLCA`, `depmixS4`, `mclust`
- **ML:** `xgboost`, `caret`, `glmnet`
- **Viz:** `ggplot2`, `plotly`, `corrplot`

### Tools
- **Network Analysis:** Gephi
- **Version Control:** Git & GitHub

---

## 🌐 Polyglot Repository: Python + R

This project leverages the strengths of both Python and R:

| Task | Language | Rationale |
|------|----------|-----------|
| **Data Preprocessing** | Python | Flexible, extensive libraries (pandas, sklearn) |
| **Exploratory Clustering** | Python | K-modes (kmodes), DBSCAN (sklearn) |
| **Latent Class Analysis** | R | Gold-standard package (poLCA) |
| **Predictive Modeling** | R | XGBoost & LASSO implementations |
| **Visualization** | Both | Matplotlib/seaborn (Python), ggplot2 (R) |

### Workflow Integration
1. **Python** → Data cleaning, imputation, exploratory clustering
2. **R** → LCA model selection, final clustering
3. **Python** ← Reload clustered data for further analysis
4. **R** → Predictive modeling with network features

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

## ⭐ Star This Repository

If you find this research useful, please consider giving it a star! It helps others discover the work.

[![GitHub stars](https://img.shields.io/github/stars/yourusername/master-thesis?style=social)](https://github.com/isarodas10/master-thesis/stargazers)

---

*Last Updated: October 2025*