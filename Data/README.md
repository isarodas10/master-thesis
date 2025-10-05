# Data Directory

This directory contains data used in the master thesis research on adolescent sexual behavior profiles and social network predictors.

## ⚠️ Privacy & Ethics

This research involves **sensitive data from adolescent participants** in a rural area. All data collection followed appropriate ethical protocols and IRB approval.

### Data Protection Measures:
- ✅ Participant anonymization
- ✅ No personally identifiable information (PII)
- ✅ Aggregated network data only
- ✅ Raw data files excluded from version control (see `.gitignore`)

**IMPORTANT:** Raw participant data (`0_Raw/*.xlsx`, `0_Raw/*.csv`) is NOT included in public repositories for privacy protection.

---

## Directory Structure

### `0_Raw/`
Contains original survey data and participant attributes.

**Files** (excluded from git):
- `2. Participants attributes.xlsx` - Original survey responses
- `schoolanonymFINALAgosto2.csv` - School network data

**Access:** Contact repository owner for data access requests (subject to ethical approval).

---

### `1_Preprocess/`
Preprocessed and analysis-ready datasets.

**Files:**
- `datos_preprocesados_lca.csv` - Cleaned data for Latent Class Analysis
- `datos_preprocesados_FA.csv` - Data prepared for factor analysis
- `data_clustered.csv` - Data with LCA cluster assignments
- `x_train.csv`, `x_test.csv` - Predictor variables (train/test split)
- `y_train.csv`, `y_test.csv` - Target variables (LCA classes)
- `data_t.xlsx` - Transformed data with text labels

**Note:** These files contain de-identified, aggregated data suitable for analysis.

---

### `Network_Gephi/`
Social network data exported for visualization in Gephi.

**Files:**
- `red_positiva.gexf` - Positive social network graph (friendship ties)

---

## Data Variables

### Survey Topics Covered:
1. **Demographics:** Age, sex/gender
2. **Relationship status:** Partnership status
3. **Sexual behavior:** 
   - Understanding of sexual intercourse
   - Sexual activity history
   - Age of first sexual experience
   - Context of first experience (substance use, contraception)
4. **Partner relationships:**
   - Sexual activity with current partner
   - Relationship quality perceptions
5. **Risk perceptions:**
   - STD concerns
   - Pregnancy concerns
   - Contraceptive use
6. **Future intentions:** Likelihood of sexual activity in next year

### Social Network Data:
- Friendship nominations
- Network centrality measures
- Community structure

---

## Usage Guidelines

### For Reproducibility:
If you have authorized access to the raw data:

1. Place raw data files in `0_Raw/`
2. Run preprocessing notebooks (in order):
   ```
   notebooks/01_data_exploration.ipynb
   notebooks/02_lca_preprocessing.ipynb
   ```
3. Run R scripts for LCA:
   ```r
   Rscript scripts/LCA.R
   ```

### For External Researchers:
If you wish to replicate this analysis with your own data:
- Review the preprocessing steps in the notebooks
- Adapt variable names and transformations to your dataset
- Ensure your data follows similar structure (see data dictionary in `docs/`)

---

## Citation

If you use this data structure or methodology, please cite:

```
Rodas, I. (2025). Individual Attributes and Social Network Predictors 
for Sexual Behaviour Profiles Among Adolescents in a Rural Area. 
Master's Thesis. [University Name].
```

---

## Contact

For questions about data access, methodology, or ethical approval:
**Isabella Rodas** - [Add contact information]
