# Quick Setup Guide

Get started with this repository in 5 minutes.

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/master-thesis.git
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

### 3. Install R Packages
```R
# Open R or RStudio
source("install_R_packages.R")
```

### 4. Verify Installation
```bash
# Python
python -c "import pandas, numpy, sklearn, kmodes; print('✓ Python packages OK')"

# R (in R console)
library(poLCA); library(xgboost); cat("✓ R packages OK\n")
```

---

## 📂 What's Where?

| What You Want | Where To Go |
|---------------|-------------|
| **Understand the project** | Read `README.md` (includes timeline) |
| **Run analysis** | `notebooks/01_data_exploration.ipynb` |
| **Original 2021 code** | `original_code/Initial_data_exploration.ipynb` |
| **R analysis** | `scripts/LCA.R` |
| **Understand variables** | `docs/data_dictionary.md` |
| **Methods details** | `docs/methodology.md` |
| **Data info** | `Data/README.md` |
| **Use functions** | `src/preprocessing.py`, `src/clustering.py` |

---

## 🔍 Repository Organization

This repository handles **both Python and R**:

```
Python (Notebooks)        →    R (Scripts)
------------------            ---------------
Data preprocessing     →      Latent Class Analysis
K-modes clustering     →      XGBoost modeling
Exploratory analysis   ←      Export clustered data
```

**Workflow:**
1. Python: Clean data, explore, cluster
2. R: Run LCA, get final classes
3. Python: Load classes, continue analysis
4. R: Predict classes with new data

---

## 🗺️ Typical Usage Paths

### Path 1: "I want to understand the research"
1. Read `README.md` (main overview with timeline)
2. Look at `docs/methodology.md` (detailed methods)
3. Browse `notebooks/01_data_exploration.ipynb` or `original_code/` (see analysis)

### Path 2: "I want to reproduce the analysis"
1. Install dependencies (above)
2. Get data access (see `Data/README.md`)
3. Run notebooks in `notebooks/` (01 → 02 → ...)
4. Run R scripts in `scripts/` (LCA.R → xgboost.R)

### Path 3: "I want to use the methods on my data"
1. Study `docs/methodology.md`
2. Look at `src/*.py` for reusable functions
3. Adapt `scripts/*.R` for your variables
4. See `docs/data_dictionary.md` for variable structure

### Path 4: "I want to cite or build on this work"
1. See citation in `README.md`
2. Check `LICENSE` for usage terms
3. Contact author (details in `README.md`)

---

## ⚠️ Common Issues

### Issue: "Cannot find data files"
**Solution:** Raw data is not included (privacy). See `Data/README.md` for:
- How to access data (if authorized)
- How to use processed data only
- How to adapt to your own data

### Issue: "Import errors in notebooks"
**Solution:** Add parent directory to path:
```python
import sys
sys.path.append('..')
from src import preprocessing
```

### Issue: "R scripts can't find files"
**Solution:** R scripts set working directory automatically if using RStudio. From command line:
```R
setwd("path/to/master-thesis/scripts")
source("LCA.R")
```

### Issue: "Package version conflicts"
**Solution:** Use virtual environments:
```bash
# Python
python -m venv venv
source venv/bin/activate

# R
install.packages("renv")
renv::init()
```

---

## 📧 Need Help?

1. **Check documentation:**
   - `README.md` - Overview
   - `docs/methodology.md` - Methods details
   - `Data/README.md` - Data questions
   - `notebooks/README.md` - Notebook info
   - `scripts/README.md` - R script info

2. **Review original code:**
   - Full 2021 analysis in `original_code/` directory
   - Includes all original notebooks with outputs

3. **Contact:**
   - Email: [your.email@example.com]
   - GitHub Issues: Open an issue on this repo

---

## ✅ Checklist: Ready to Start?

- [ ] Repository cloned
- [ ] Python dependencies installed
- [ ] R packages installed
- [ ] Read `README.md`
- [ ] Understand data access requirements
- [ ] Know which analysis path to follow

**All set?** → Start with `README.md` then `notebooks/01_data_exploration.ipynb`

---

*Last updated: October 2025*
