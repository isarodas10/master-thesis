# Migration Guide: Old → New Structure

This document maps the old repository structure to the new organized structure.

> 🕐 **Timeline Context:** The original analysis was conducted in **2021** for my master's thesis. This repository reorganization and documentation was completed in **October 2025** to create a professional showcase portfolio.

---

## 📁 Directory Structure Changes

### Before Reorganization (Original 2021 Structure)
```
master-thesis/
├── README.md (minimal)
├── LICENSE
├── Code/                              ← Original 2021 analysis
│   ├── Initial_data_exploration.ipynb
│   ├── Python/
│   │   ├── LCA Preprocessing.ipynb
│   │   └── lca.py
│   └── R/
│       ├── LCA.R
│       ├── missing_data_in_R.R
│       └── xgboost.R
├── Data/
│   ├── 0_Raw/ (various files)
│   ├── 1_Preprocess/ (various files)
│   └── Network_Gephi/
└── [thesis PDF]
```

### After Reorganization (2025 Professional Showcase)
```
master-thesis/
├── README.md ✨ (comprehensive with timeline)
├── SETUP.md ✨ (new)
├── MIGRATION_GUIDE.md ✨ (this file)
├── LICENSE
├── requirements.txt ✨ (new)
├── install_R_packages.R ✨ (new)
├── .gitignore ✨ (new)
│
├── original_code/ 📦 (preserved - original 2021 analysis)
│   └── [all original 2021 analysis files preserved]
│
├── Data/ (enhanced)
│   ├── README.md ✨ (new - data documentation)
│   ├── 0_Raw/
│   ├── 1_Preprocess/
│   └── Network_Gephi/
│
├── notebooks/ ✨ (new - cleaned versions)
│   ├── README.md
│   └── 01_data_exploration.ipynb
│
├── src/ ✨ (new - Python modules)
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── lca.py
│   └── visualization.py
│
├── scripts/ ✨ (new - organized R scripts)
│   ├── README.md
│   ├── LCA.R (copied from Code/R/)
│   ├── xgboost.R (copied from Code/R/)
│   └── missing_data_in_R.R (copied from Code/R/)
│
├── results/ ✨ (new - for outputs)
│   ├── figures/
│   ├── tables/
│   └── models/
│
├── docs/ ✨ (new - documentation)
│   ├── methodology.md
│   └── data_dictionary.md
│
└── [thesis PDF] (preserved)
```

**Legend:**
- ✨ = New or significantly enhanced
- (preserved) = Kept as-is from original
- (copied) = Duplicated for better organization

---

## 🔄 File Mapping

| Old Location (2021) | New Location (2025) | Status | Purpose |
|---------------------|---------------------|--------|---------|
| `README.md` (basic) | `README.md` (comprehensive with timeline) | **Enhanced** | Main project overview |
| N/A | `SETUP.md` | **New** | Quick start guide |
| N/A | `MIGRATION_GUIDE.md` | **New** | This file |
| N/A | `requirements.txt` | **New** | Python dependencies |
| N/A | `install_R_packages.R` | **New** | R package installer |
| N/A | `.gitignore` | **New** | Privacy protection |
| `Code/` | `original_code/` | **Renamed** | Preserved 2021 analysis |
| `Code/Initial_data_exploration.ipynb` | `original_code/` (preserved) + `notebooks/01_*.ipynb` | **Preserved + New** | Original + cleaned version |
| `Code/Python/lca.py` | `original_code/Python/` + `src/lca.py` | **Preserved + Copied** | Module for import |
| `Code/R/*.R` | `original_code/R/` + `scripts/*.R` | **Preserved + Copied** | Better discoverability |
| N/A | `src/preprocessing.py` | **New** | Extracted reusable code |
| N/A | `src/clustering.py` | **New** | Extracted reusable code |
| N/A | `src/visualization.py` | **New** | Extracted reusable code |
| N/A | `Data/README.md` | **New** | Data documentation |
| N/A | `notebooks/README.md` | **New** | Notebook guide |
| N/A | `scripts/README.md` | **New** | R script guide |
| N/A | `docs/methodology.md` | **New** | Detailed methods |
| N/A | `docs/data_dictionary.md` | **New** | Variable descriptions |

---

## 🎯 Why These Changes?

### 1. **Better Organization**
- **Before (2021):** Code scattered in `Code/Python/` and `Code/R/`
- **After (2025):** Clear separation: `notebooks/` (analysis), `src/` (modules), `scripts/` (R)
- **Original preserved:** All 2021 analysis in `original_code/`
- **Benefit:** Easy to find what you need

### 2. **Reproducibility**
- **Before:** No dependency specification
- **After:** `requirements.txt`, `install_R_packages.R`
- **Benefit:** Anyone can set up environment

### 3. **Documentation**
- **Before:** Minimal README
- **After:** Comprehensive README, methodology, data dictionary, setup guide
- **Benefit:** Professional showcase, easier for others to understand

### 4. **Code Reusability**
- **Before:** All code in notebooks
- **After:** Extracted to `src/` modules
- **Benefit:** Import functions, avoid code duplication

### 5. **Privacy & Ethics**
- **Before:** No .gitignore, data exposure risk
- **After:** `.gitignore` excludes sensitive data
- **Benefit:** Safe to share publicly

### 6. **Professional Presentation**
- **Before:** Research project structure
- **After:** Showcase portfolio structure
- **Benefit:** Impresses potential employers/collaborators

---

## 🔀 Workflow Changes

### Old Workflow (2021)
```
1. Open Code/Initial_data_exploration.ipynb
2. Run all cells
3. Switch to R, run Code/R/LCA.R
4. Back to Python, continue analysis
5. Results scattered, no documentation
```

### New Workflow (2025)
```
1. Read README.md (understand project + timeline)
2. Follow SETUP.md (install dependencies)
3. Run notebooks/01_*.ipynb (or use original_code/ files)
4. Run scripts/LCA.R (R analysis)
5. Results saved to results/
6. Documentation in docs/
```

---

## 📚 How to Use Python & R Together

### The Polyglot Advantage

**Python strengths used for:**
- Data cleaning & preprocessing (pandas)
- Exploratory clustering (K-modes, DBSCAN)
- Visualization (matplotlib, seaborn)
- Missing data imputation (sklearn)

**R strengths used for:**
- Latent Class Analysis (poLCA - gold standard)
- Statistical modeling (better stats packages)
- XGBoost (excellent R implementation)
- LASSO regression (glmnet)

### Integration Points

**1. Python → R (Data Export)**
```python
# In Python notebook
df.to_csv('../Data/1_Preprocess/datos_preprocesados_lca.csv', index=False)
```

**2. R Analysis**
```r
# In scripts/LCA.R
data <- read_csv("../Data/1_Preprocess/datos_preprocesados_lca.csv")
lca_model <- poLCA(formula, data, nclass=4)
write_csv(data, '../Data/1_Preprocess/data_clustered.csv')
```

**3. R → Python (Data Import)**
```python
# Back in Python
df = pd.read_csv('../Data/1_Preprocess/data_clustered.csv')
# Continue with new cluster assignments
```

---

## 🎓 For Employers/Reviewers

### What This Reorganization Demonstrates

1. **Software Engineering Skills**
   - Modular code design (`src/` modules)
   - Version control (.gitignore)
   - Dependency management (requirements.txt)
   - Documentation (comprehensive README)

2. **Data Science Best Practices**
   - Reproducible research
   - Clean code principles
   - Proper data handling
   - Ethical considerations

3. **Communication Skills**
   - Clear documentation
   - Data dictionary
   - Methodology write-up
   - User guides (SETUP.md)

4. **Polyglot Programming**
   - Python + R integration
   - Choosing right tool for the job
   - Cross-language workflows

---

## 🚀 Next Steps After Reorganization

### Immediate
- [ ] Update GitHub repository
- [ ] Test all paths and imports
- [ ] Run end-to-end workflow to verify
- [ ] Update README with your contact info

### Short-term
- [ ] Add sample visualizations to README
- [ ] Create example notebook with synthetic data
- [ ] Add GitHub Actions for CI/CD (optional)
- [ ] Create CONTRIBUTING.md if open-sourcing

### Long-term
- [ ] Publish paper from thesis
- [ ] Add to portfolio website
- [ ] Present at conferences
- [ ] Open-source (if approved)

---

## 💡 Tips for Showcasing

### On GitHub
1. **Pin this repository** to your profile
2. **Add topics/tags:** data-science, latent-class-analysis, python, r, thesis
3. **Enable GitHub Pages** (optional) for documentation
4. **Add screenshots** of visualizations to README

### On Resume/CV
```
• Developed mixed-methods analysis pipeline combining Python (pandas, 
  scikit-learn) and R (poLCA, XGBoost) to identify behavioral profiles 
  among N=242 adolescents
• Implemented reproducible research workflow with modular code design, 
  comprehensive documentation, and version control
• Published research code and methodology as open-source GitHub repository
```

### In Interviews
- Show the organized structure
- Explain Python/R integration decisions
- Discuss ethical data handling
- Demonstrate documentation quality

---

## ❓ FAQ

**Q: Should I delete the old `original_code/` directory?**  
A: No! Keep it as a record of your original 2021 analysis. It shows authenticity and research timeline.

**Q: Can I still use my original notebooks?**  
A: Absolutely! They're preserved in `original_code/`. The new `notebooks/` are for showcase.

**Q: What if I need to update the analysis?**  
A: Work in the new structure (`notebooks/`, `src/`), keep `original_code/` as historical record from 2021.

**Q: How do I handle updates to the data?**  
A: Place new data in `Data/0_Raw/`, rerun preprocessing, document changes.

**Q: Can others reproduce my analysis without raw data?**  
A: Partially - they can use processed data in `Data/1_Preprocess/` and see methodology.

---

## 📞 Support

If you have questions about the reorganization:
1. Review this guide
2. Check `SETUP.md` for quick start
3. See individual README files in each directory
4. Contact: [your.email@example.com]

---

*Congratulations on completing your thesis and organizing it professionally! 🎉*
