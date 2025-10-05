# Data Dictionary

Complete variable descriptions for the adolescent sexual behavior study.

---

## Demographic Variables

| Variable | Spanish | Type | Values | Description |
|----------|---------|------|--------|-------------|
| `ID` | ID | String | i1-i242 | Unique participant identifier (anonymized) |
| `Sex` | Sexo | Categorical | 1=Male, 2=Female, 3=Other | Participant sex/gender |
| `Age` | Edad | Ordinal | 13-17 years | Participant age |

---

## Sexual Behavior Variables

### Understanding & Experience

| Variable | Question Code | Type | Values | Description |
|----------|--------------|------|--------|-------------|
| `Understand` | Q11.39 | Binary | 1=Yes, 2=No | "Do you understand what sexual intercourse is?" |
| `Had sex` | Q11.40 | Categorical | 1=Yes, 2=No, 3=Refuse, 4=Don't know, 5=Don't understand | "Have you had sexual intercourse?" |
| `Age sex` | Q11.41 | Ordinal | 1-8 (years), -3=N/A | "How old were you when you had your first sexual intercourse?" |

### First Sexual Experience

| Variable | Question Code | Type | Values | Description |
|----------|--------------|------|--------|-------------|
| `Sex under influence` | Q11.44 | Binary | 1=Yes, 2=No, -3=N/A | "The first time you had sex, was it under the influence of alcohol or drugs?" |
| `Pregnancy prevention` | Q11.42 | Binary | 1=Yes, 2=No, 3=Don't know, 4=Refuse, -3=N/A | "The first time you had sex, did you or your partner do anything to prevent pregnancy?" |

### Partner Relationships

| Variable | Question Code | Type | Values | Description |
|----------|--------------|------|--------|-------------|
| `Partner status` | Q11.11 | Categorical | 1-6=Various partnership types, 7-11=No partner/Other | "What is your partnership status?" |
| `Sex with partner` | Q11.45 | Binary | 1=Yes, 2=No, 3=Refuse, 4=Don't know, -3=N/A | "Have you had sex with your partner?" |
| `Sex strengthen relationship` | Q11.46 | Ordinal | 1-4 (Likert scale), -3=N/A | "Do you feel that having sex with your partner allows you to have a closer relationship?" |

### Risk Perceptions

| Variable | Question Code | Type | Values | Description |
|----------|--------------|------|--------|-------------|
| `STD preocupation` | Q11.47 | Ordinal | 1-6 (Not at all → Very concerned) | "How concerned are you about getting a sexually transmitted disease from your partner?" |
| `Pregnancy preocupation` | Q11.48 | Ordinal | 1-6 (Not at all → Very concerned) | "How concerned are you about getting pregnant with your partner?" |
| `Avoid pregnancy` | Q11.49 | Binary | 1=Yes, 2=No, 3=Don't know, -3=N/A | "Are you or your partner doing something to avoid pregnancy?" |

### Future Intentions

| Variable | Question Code | Type | Values | Description |
|----------|--------------|------|--------|-------------|
| `Sex within a year` | Q11.53 | Ordinal | 1-7 (Definitely no → Definitely yes) | "Do you think you are going to have sex with someone in the next year?" |

---

## Missing Data Codes

Special codes used for missing or non-applicable data:

| Code | Meaning | Context |
|------|---------|---------|
| `-1` | Does not understand sexual intercourse | Systematic skip |
| `-2` | Refused to answer / Don't know about understanding | Missing category |
| `-3` | Has not had sex | Systematic skip for sex-related questions |
| `-4` | Refused / Don't know about sexual activity | Missing category |
| `-5` | Had sex but not with partner | Systematic skip |
| `-6` | Refused about partner sex | Missing category |
| `-7` | No partner or complex partnership | Systematic skip |
| `NaN` | True missing data | Various reasons |

---

## Derived Variables

### Cluster Assignments

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `cluster_predicted_cao` | Categorical | 0-9 | K-modes cluster (Cao initialization) |
| `cluster_predicted_huang` | Categorical | 0-9 | K-modes cluster (Huang initialization) |
| `cluster_DBSCAN` | Categorical | -1, 0-9 | DBSCAN cluster (-1 = noise) |
| `Class_LCA` | Categorical | 1-4 | Latent class from poLCA model |

### Cluster Interpretation (LCA - 4 Classes)

| Class | Label | Size | Description |
|-------|-------|------|-------------|
| 1 | **Inexperienced/No Understanding** | ~XX | Does not understand or engage with sexual activity |
| 2 | **Abstinent/Cautious** | ~XX | Understands but has not engaged in sexual activity |
| 3 | **Active/Protected** | ~XX | Sexually active with consistent protective behaviors |
| 4 | **Active/Risk-Taking** | ~XX | Sexually active with inconsistent protection or risk behaviors |

*(Exact sizes and descriptions based on analysis results)*

---

## Social Network Variables

Variables derived from friendship nomination data (analyzed in Gephi):

| Variable | Type | Description |
|----------|------|-------------|
| `Degree` | Numeric | Number of friendship connections |
| `In-degree` | Numeric | Number of incoming friendship nominations |
| `Out-degree` | Numeric | Number of outgoing friendship nominations |
| `Betweenness` | Numeric | Bridging position in network |
| `Closeness` | Numeric | Average distance to all other nodes |
| `Eigenvector` | Numeric | Connection to well-connected peers |
| `Community` | Categorical | Detected community membership |

---

## Recoded Variables (for Analysis)

Some variables were recoded to reduce categories for analysis:

### Age of First Sex (Recoded)
- Original: 1-8+ (specific ages)
- Recoded: `7.0` = "Not applicable or age >7"

### STD & Pregnancy Preocupation (Recoded)
- Original: 6-point scale
- Recoded: 
  - `1.0` = Low concern (1-2 original)
  - `2.0` = Moderate concern (3-4 original)
  - `3.0` = High concern or N/A

### Partner Status (Recoded)
- Original: 11 categories
- Recoded:
  - `1.0` = In relationship (1-6 original)
  - `2.0` = No partner (7-8 original)
  - `3.0` = Other/Refuse

---

## Data Quality Notes

### Missingness Patterns
- Questions about sexual experience have high missingness (~74%) among those who haven't had sex (systematic skip)
- Partnership questions have ~5% missing
- Future intentions have ~49% missing

### Imputation Strategy
- **Systematic skips:** Coded with negative values (see Missing Data Codes)
- **True missingness:** Iterative imputation using sklearn's IterativeImputer
- **Method:** MICE (Multivariate Imputation by Chained Equations)

### Data Transformations
1. Age codes mapped to actual ages (13-17)
2. Response categories collapsed for parsimony
3. Missing data categorized before imputation
4. Text responses recoded to numeric

---

## Usage Examples

### Loading Data
```python
import pandas as pd

# Load clustered data
data = pd.read_csv('Data/1_Preprocess/data_clustered.csv')

# View variable types
print(data.dtypes)
```

### Filtering by Sexual Activity
```python
# Only sexually active participants
active = data[data['Had sex'] == 1]

# Only those who understand sexual intercourse
understands = data[data['Understand'] == 1]
```

### Analyzing by Cluster
```python
# Summary by LCA class
summary = data.groupby('Class_LCA').agg({
    'Age': 'mean',
    'Sex': lambda x: x.mode()[0],
    'STD preocupation': 'mean'
})
```

---

## References

Survey questions adapted from:
- [Add survey source/citation if applicable]
- Developed in consultation with adolescent health experts
- IRB approved protocol #XXXX

---

*For questions about variable definitions or data access, see main README.md*
