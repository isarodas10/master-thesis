# Data Directory

This directory contains data used in the master thesis research on adolescent sexual behavior profiles and social network predictors.

> **Research Context:** Original data collection and analysis: 2021 | Repository organization: October 2025

---

## ⚠️ Privacy & Ethics

This research involves **sensitive data from adolescent participants** (ages 13-17) in a rural area of Colombia. All data collection followed appropriate ethical protocols with IRB approval.

### Ethical Protections:
- ✅ **Parental consent** + adolescent assent obtained
- ✅ **Complete anonymization** (no personally identifiable information)
- ✅ **Participant IDs** (codes like i1, i2, etc. - no names)
- ✅ **Aggregated network data** only
- ✅ **Raw data files** excluded from public repository (see `.gitignore`)
- ✅ **Secure storage** of original data

**IMPORTANT:** Raw participant survey data is NOT included in public repositories for privacy protection. Preprocessed, anonymized data is available for reproducibility.

---

## 📂 Directory Structure

```
Data/
├── README.md (this file)
├── 0_Raw/          # Original data (git-ignored)
├── 1_Preprocess/   # Analysis-ready data (anonymized)
└── Network_Gephi/  # Social network files
```

---

### `0_Raw/` - Original Survey Data (Protected)

**⚠️ NOT included in GitHub** (protected by `.gitignore`)

**Files:**
- `2. Participants attributes.xlsx` - Original survey responses (242 participants)
- `schoolanonymFINALAgosto2.csv` - School attendance data

**Access:** Contact repository owner for data access requests (subject to ethical review and approval).

**Who Can Access:**
- Researchers with appropriate IRB approval
- Collaborators with data use agreements
- Must demonstrate ethical research protocols

---

### `1_Preprocess/` - Analysis-Ready Data ✅

**Included in repository** - Cleaned, anonymized, ready for analysis.

**Files:**

| File | Description | Used In | Size |
|------|-------------|---------|------|
| `datos_preprocesados_FA.csv` | Clean data for Factor Analysis | Notebook 3 | 230 participants |
| `data_clustered.csv` | Data with cluster assignments + demographics | Notebooks 4 & 5 | 230 participants |
| `x_train.csv` | Training features (31 variables) | Notebook 4 | 172 participants |
| `x_test.csv` | Test features (31 variables) | Notebook 4 | 58 participants |
| `y_train.csv` | Training target (cluster labels) | Notebook 4 | 172 participants |
| `y_test.csv` | Test target (cluster labels) | Notebook 4 | 58 participants |

**Note:** 
- Original sample: 242 participants
- After filtering (>50% missing): 230 participants
- Train/test split: 70/30 stratified

**Data Composition:**
- **23 behavioral questions** (selected from literature)
- **8 social network variables** (from Gephi analysis)
- **5 cluster labels** (from Factor Analysis + clustering)

---

### `Network_Gephi/` - Social Network Data

**Files:**
- `red_positiva.gexf` - Friendship network graph (for Gephi visualization)

**Network Metrics Extracted (used in analysis):**
1. `community_louvain` - Community membership
2. `In_degree` - Popularity (incoming friendship nominations)
3. `Out_degree` - Sociability (outgoing nominations)
4. `eigenvector_centrality` - Influence score
5. `clustering_coef` - Friend interconnectedness
6. `average_neigh` - Average neighbor popularity
7. `closeness` - Network reach
8. `betweenness` - Brokerage position

**Analysis Software:** Gephi (open-source network visualization platform)

---

## 📊 Data Variables Overview

### Demographics (3 variables)
- `ID` - Participant identifier (anonymous codes: i1, i2, etc.)
- `Sex` - Gender (1=Male, 2=Female, 3=Other)
- `Age` - Age in years (13-17)

### Sexual Behavior Questions (12 variables)
1. **Understanding:** Do you understand what sexual intercourse is?
2. **Experience:** Have you had sexual intercourse?
3. **Intentions:** Will you have sex in the next year?
4. **Age at debut:** How old were you at first intercourse?
5. **Contraception:** Used protection at first time?
6. **Substance use:** Under influence at first time?
7. **Partner sex:** Had sex with current partner?
8. **Relationship impact:** Does sex strengthen relationship?
9. **STD concern:** Worried about sexually transmitted diseases?
10. **Pregnancy concern:** Worried about unwanted pregnancy?
11. **Partnership status:** Do you have a boyfriend/girlfriend?
12. **Current contraception:** Currently avoiding pregnancy?

**For complete variable descriptions:** See `docs/data_dictionary.md`

### Social Network Variables (8 variables)
Network position metrics from Gephi analysis (see above).

### Cluster Labels (1 variable)
- **5 clusters identified** through Factor Analysis + clustering:
  - Cluster 0 (n=22): High-Risk Early Initiators
  - Cluster 1 (n=126): Abstinent/Uninitiated
  - Cluster 2 (n=42): Safe & Experienced
  - Cluster 3 (n=13): Private/Reluctant to Disclose
  - Cluster 4 (n=25): Uninformed/Limited Knowledge

---

## 🔄 Data Processing Workflow

The complete data workflow is documented in **5 Jupyter notebooks**:

### Notebook 1: Initial Data Exploration
- Loads: `0_Raw/2. Participants attributes.xlsx`
- Explores: Missing patterns, demographics, correlations

### Notebook 2: Data Cleaning & Preprocessing
- **Inputs:** Raw survey data (242 participants)
- **Process:**
  1. Filter participants with >50% missing (12 removed)
  2. Apply skip logic (10 rules, negative coding)
  3. Recode categorical variables (12 operations)
  4. MICE imputation for remaining missing
- **Outputs:** `datos_preprocesados_FA.csv` (230 participants)

### Notebook 3: Factor Analysis & Clustering
- **Inputs:** `datos_preprocesados_FA.csv`
- **Process:**
  1. Factor Analysis (Bartlett's, KMO, factor extraction)
  2. 8 clustering algorithms tested
  3. 3 evaluation metrics
  4. Select optimal: 5 clusters
- **Outputs:** Cluster assignments, factor scores

### Notebook 4: Susceptibility Models
- **Inputs:** Pre-prepared train/test data
  - `x_train.csv`, `x_test.csv` (features)
  - `y_train.csv`, `y_test.csv` (cluster labels)
- **Process:**
  1. 4 predictive models (DT, RF, LASSO, XGBoost)
  2. Feature importance extraction
- **Shows:** How behavioral + network + cluster data were integrated

### Notebook 5: Cluster Profiling & Interpretation
- **Inputs:** Train/test data + cluster data
- **Process:**
  1. Consolidate feature importance
  2. Profile each of 5 clusters
  3. Demographics, behaviors, network by cluster
- **Outputs:** Complete cluster characterizations with intervention recommendations

**See:** `notebooks/README.md` for detailed workflow guide

---

## 🚀 Usage Guidelines

### For Reproducibility (with raw data access):

1. **Place raw data** in `0_Raw/`:
   ```
   Data/0_Raw/2. Participants attributes.xlsx
   ```

2. **Run notebooks sequentially:**
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

3. **Check outputs** saved to `1_Preprocess/`

### For Using Preprocessed Data Only:

The repository includes anonymized preprocessed data in `1_Preprocess/`. You can:
- Start from **Notebook 3** (Factor Analysis)
- Or start from **Notebook 4** (using pre-split train/test data)
- Or start from **Notebook 5** (explore final cluster profiles)

### For Adapting to Your Data:

1. Review preprocessing steps in Notebook 2
2. Adapt variable names and skip logic to your survey
3. Follow same workflow: Clean → Factor Analysis → Clustering → Modeling → Profiling
4. See `docs/methodology.md` for conceptual approach

---

## 📈 Key Findings from This Data

### Sample Characteristics
- **N = 230** adolescents (after filtering)
- **Ages:** 13-17 years
- **Location:** Rural schools in Barú, Colombia
- **Survey:** 15 questions on sexual behavior and attitudes

### Main Results
- **5 distinct behavioral profiles** identified
- **Social network position** predicts profiles better than demographics alone
- **8 of top 15 predictors** are network variables
- **Heterogeneous population** requires cluster-specific interventions

**See:** `README.md` for detailed cluster descriptions

---

## 📖 Citation

If you use this data structure or methodology, please cite:

```bibtex
@mastersthesis{rodas2021sexual,
  author  = {Isabella Rodas},
  title   = {Individual Attributes and Social Network Predictors for Sexual 
             Behaviour Profiles Among Adolescents in a Rural Area},
  school  = {Universidad de los Andes},
  year    = {2021},
  address = {Bogotá, Colombia},
  url     = {https://github.com/isarodas10/predictors-for-sexual-behaviour-profiles}
}
```

---

## 📧 Contact & Data Access

**For questions about:**
- Data access requests (with IRB approval)
- Methodology questions
- Collaboration opportunities
- Ethical protocols

**Contact:**
- **Isabella Rodas**
- Email: isabella.rodas.arango@gmail.com
- GitHub: [@isarodas10](https://github.com/isarodas10)
- LinkedIn: [Isabella Rodas Arango](https://www.linkedin.com/in/isabella-rodas-arango/)

**Institution:** Universidad de los Andes, Colombia  
**Thesis Defense:** December 7th, 2021

---

## 🔐 Data Security Reminder

**If you have access to raw data:**
- ✅ Store securely (encrypted if possible)
- ✅ Never commit to version control
- ✅ Follow IRB protocols
- ✅ Respect participant privacy
- ✅ Delete when project complete (as per data use agreement)

**The `.gitignore` file protects:** `0_Raw/*.xlsx`, `0_Raw/*.csv`

---

*Data collected: 2021 | Analysis: 2021 | Repository organized: October 2025*