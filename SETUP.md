# Quick Setup Guide

Get started with this repository in 5 minutes.

> **Timeline Context:** This repository contains the 2021 master's thesis analysis, reorganized and documented in October 2025. The complete analysis is now presented in **5 Jupyter notebooks** for reproducibility.

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/isarodas10/master-thesis.git
cd master-thesis
```

### 2. Install Python Dependencies
```bash
# Option A: Using pip
pip install -r requirements.txt

# Option B: Using virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Key packages installed:**
- Data: `pandas`, `numpy`, `openpyxl`
- Factor Analysis: `factor_analyzer`
- Clustering: `scikit-learn` (8 algorithms)
- Models: `scikit-learn`, `xgboost`
- Visualization: `matplotlib`, `seaborn`, `missingno`

### 3. (Optional) Install R for Original Code
The documented analysis uses **Python only**. R packages are only needed if you want to explore the original 2021 code in `original_code/R/`:

```R
# Open R or RStudio
source("install_R_packages.R")
```

### 4. Verify Installation
```bash
# Python (main requirements)
python -c "import pandas, numpy, sklearn, factor_analyzer, xgboost, seaborn; print('✓ Python packages OK')"

# Start Jupyter
cd notebooks
jupyter notebook
```

---

## 📂 What's Where?

| What You Want | Where To Go |
|---------------|-------------|
| **Understand the project** | Read `README.md` (overview with timeline & cluster profiles) |
| **Run complete analysis** | `notebooks/` - 5 notebooks, run sequentially |
| **Initial exploration** | `notebooks/01_initial_data_exploration.ipynb` |
| **Data cleaning** | `notebooks/02_data_cleaning_preprocessing.ipynb` |
| **Factor Analysis & Clustering** | `notebooks/03_factor_analysis_clustering.ipynb` |
| **Predictive models** | `notebooks/04_susceptibility_models.ipynb` |
| **Cluster profiling** | `notebooks/05_cluster_profiling_interpretation.ipynb` |
| **Original 2021 code** | `original_code/` (Python + R from thesis) |
| **Understand variables** | `docs/data_dictionary.md` |
| **Methods details** | `docs/methodology.md` |
| **Data info** | `Data/README.md` |
| **Thesis PDF** | `Individual Attributes and Social Network....pdf` |
| **Defense slides** | `Presentation_Spanish.pdf` (Dec 7, 2021) |

---

## 🔍 Analysis Workflow (5 Notebooks)

The complete analysis is now unified in **Python** for reproducibility:

```
┌─────────────────────────────────────────────────────────────┐
│              5-Notebook Analysis Pipeline                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📊 Notebook 1: Initial Data Exploration                    │
│     • Survey questions & definitions                        │
│     • Missing data patterns                                 │
│     • Demographics & correlations                           │
│                                                             │
│  🧹 Notebook 2: Data Cleaning & Preprocessing               │
│     • Filter participants (>50% missing)                    │
│     • Skip logic & recoding                                 │
│     • MICE imputation                                       │
│                                                             │
│  🔬 Notebook 3: Factor Analysis & Clustering                │
│     • Bartlett's & KMO tests                                │
│     • Factor extraction                                     │
│     • 8 clustering methods → 5 clusters                     │
│                                                             │
│  🎯 Notebook 4: Susceptibility Models                       │
│     • Merge: behavioral + network + clusters                │
│     • 4 models: DT, RF, LASSO, XGBoost                      │
│     • Feature importance                                    │
│                                                             │
│  📈 Notebook 5: Cluster Profiling & Interpretation          │
│     • Consolidate feature importance                        │
│     • Profile 5 clusters in detail                          │
│     • Intervention implications                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Why Python-only?**
- Single-language workflow = easier to reproduce
- All methods available in Python
- Better for sharing and teaching
- Original R code preserved in `original_code/` for reference

---

## 🗺️ Typical Usage Paths

### Path 1: "I want to understand the research"
1. Read `README.md` (overview, 5 cluster profiles, key findings)
2. Look at `docs/methodology.md` (detailed methods)
3. Browse notebooks sequentially:
   - Start with `notebooks/01_initial_data_exploration.ipynb`
   - Each notebook has extensive documentation
4. View thesis PDF and defense slides for complete context

### Path 2: "I want to reproduce the analysis"
1. **Install dependencies** (see Quick Start above)
2. **Get data access** (see `Data/README.md` for access instructions)
3. **Run notebooks sequentially:**
   ```bash
   cd notebooks
   jupyter notebook
   
   # Run in order:
   # 01_initial_data_exploration.ipynb
   # 02_data_cleaning_preprocessing.ipynb
   # 03_factor_analysis_clustering.ipynb
   # 04_susceptibility_models.ipynb
   # 05_cluster_profiling_interpretation.ipynb
   ```
4. Each notebook is fully self-contained with documentation

### Path 3: "I want to adapt the methods to my data"
1. Study `docs/methodology.md` (conceptual approach)
2. Review notebooks to see implementation details:
   - Notebook 2: Data cleaning strategies
   - Notebook 3: Factor Analysis + clustering approach
   - Notebook 4: Model comparison framework
   - Notebook 5: Profiling methodology
3. See `docs/data_dictionary.md` for variable structure
4. Adapt data preprocessing to your survey structure

### Path 4: "I want to explore the original 2021 code"
1. Navigate to `original_code/`
2. Python notebooks: `original_code/Initial_data_exploration.ipynb`
3. R scripts: `original_code/R/` (includes LCA exploration)
4. Note: LCA was explored but Factor Analysis was used in final thesis

### Path 5: "I want to cite or build on this work"
1. See citation format in `README.md`
2. Check `LICENSE` (MIT - permissive use)
3. Review thesis PDF for full context
4. Contact: isabella.rodas.arango@gmail.com

---

## ⚠️ Common Issues

### Issue: "Cannot find data files"
**Solution:** Raw data is not included in the repository (privacy protection). 

Options:
1. **Use preprocessed data:** Available in `Data/1_Preprocess/`
   - `datos_preprocesados_FA.csv` - Ready for Factor Analysis
   - `x_train.csv`, `x_test.csv`, `y_train.csv`, `y_test.csv` - Ready for modeling
2. **Request raw data access:** See `Data/README.md` for contact information
3. **Adapt to your data:** Follow notebook structure with your own dataset

### Issue: "Import errors or package conflicts"
**Solution:** Use a virtual environment (strongly recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Verify
python -c "import factor_analyzer, sklearn, xgboost; print('✓ All packages OK')"
```

### Issue: "Jupyter kernel not found"
**Solution:** Install jupyter in your virtual environment:
```bash
# With venv activated
pip install jupyter ipykernel
python -m ipykernel install --user --name=venv

# Then in Jupyter, select kernel: venv
```

### Issue: "Want to run R original code"
**Solution:** R code is preserved but optional:
```R
# From RStudio or R console
setwd("path/to/master-thesis/original_code/R")
source("xgboost.R")  # Original modeling code
source("LCA.R")      # LCA exploration (not in final thesis)
```

### Issue: "Notebook cells don't run"
**Solution:** Run notebooks sequentially:
1. Notebooks 2-5 depend on outputs from previous notebooks
2. Start with Notebook 1, run all cells
3. Move to Notebook 2, and so on
4. Each notebook saves outputs to `Data/1_Preprocess/`

---

## 📧 Need Help?

### 1. Check Documentation (in order)
- ✅ **`README.md`** - Start here! Overview, cluster profiles, key findings
- 📚 **`docs/methodology.md`** - Detailed methods (Factor Analysis, clustering, models)
- 📊 **`Data/README.md`** - Data access, ethics, variable information
- 📓 **`notebooks/README.md`** - Notebook workflow guide
- 📖 **Thesis PDF** - Complete thesis document with full results

### 2. Review Original Code
- Full 2021 analysis preserved in `original_code/`
- Python: `original_code/Initial_data_exploration.ipynb`
- R: `original_code/R/` (includes LCA exploration)

### 3. Contact
- **Email:** isabella.rodas.arango@gmail.com
- **GitHub:** [@isarodas10](https://github.com/isarodas10)
- **GitHub Issues:** Open an issue on this repository
- **LinkedIn:** [Isabella Rodas Arango](https://www.linkedin.com/in/isabella-rodas-arango/)

---

## ✅ Checklist: Ready to Start?

**Setup:**
- [ ] Repository cloned from GitHub
- [ ] Python 3.9+ installed
- [ ] Virtual environment created and activated
- [ ] All Python dependencies installed (`pip install -r requirements.txt`)
- [ ] Jupyter notebook accessible

**Understanding:**
- [ ] Read `README.md` (overview + cluster profiles)
- [ ] Understand data privacy (raw data not included)
- [ ] Know which path to follow (understand vs. reproduce vs. adapt)

**Ready to Run:**
- [ ] Data access clarified (preprocessed data in `Data/1_Preprocess/`)
- [ ] Jupyter notebook launched in `notebooks/` directory
- [ ] Starting with Notebook 1

**All set?** → 
1. Start Jupyter: `cd notebooks && jupyter notebook`
2. Open `01_initial_data_exploration.ipynb`
3. Run cells sequentially (Shift + Enter)
4. Follow through notebooks 1 → 2 → 3 → 4 → 5

---

## 🎯 Quick Reference

**5 Notebooks (run in order):**
1. Initial Data Exploration
2. Data Cleaning & Preprocessing  
3. Factor Analysis & Clustering
4. Susceptibility Models
5. Cluster Profiling & Interpretation

**5 Clusters identified:**
- Cluster 0 (n=22): High-Risk Early Initiators
- Cluster 1 (n=126): Abstinent/Uninitiated
- Cluster 2 (n=42): Safe & Experienced
- Cluster 3 (n=13): Private/Reluctant to Disclose
- Cluster 4 (n=25): Uninformed/Limited Knowledge

**Key Finding:** Social network position predicts behavior profiles more strongly than demographics alone.

---

*Repository organized: October 2025*  
*Original thesis analysis: 2021*  
*Thesis defense: December 7th, 2021*
