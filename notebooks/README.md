# Analysis Notebooks

This directory contains Jupyter notebooks for data analysis.

## Notebooks Overview

### `01_data_exploration.ipynb`
**Initial Data Exploration & Visualization**

Exploratory data analysis of adolescent sexual behavior survey data.

**Contents:**
- Data loading and initial inspection
- Missing data visualization
- Demographic distributions
- Correlation analysis (Spearman)
- Key variable summaries

**Outputs:** Initial insights, visualizations

---

## Original Analysis Notebooks (2021)

The complete, detailed analysis notebooks from the original 2021 research are preserved in `/original_code/`:

- `/original_code/Initial_data_exploration.ipynb` - Full exploratory analysis
- `/original_code/Python/LCA Preprocessing.ipynb` - Complete LCA preprocessing pipeline

These contain the full analysis workflow including:
- Detailed missing data categorization and imputation
- Survey response recoding and transformation
- K-modes clustering (Cao and Huang initialization)
- DBSCAN clustering with Gower distance
- Comprehensive visualizations

**Note:** The notebooks in this `notebooks/` directory provide cleaned, streamlined versions for reproducibility. Refer to `/original_code/` for the complete original 2021 analysis.

---

## Workflow

### Python Analysis (Notebooks)
1. **Data Exploration** → `01_data_exploration.ipynb`
2. **Preprocessing** → Original: `/original_code/Python/LCA Preprocessing.ipynb`
3. **Clustering** → Original: `/original_code/Initial_data_exploration.ipynb`

### R Analysis (Scripts)
4. **Latent Class Analysis** → `scripts/LCA.R`
5. **Predictive Modeling** → `scripts/xgboost.R`

---

## Running the Notebooks

### Setup
```bash
# Install Python dependencies
pip install -r ../requirements.txt

# Launch Jupyter
jupyter notebook
```

### Execution Order
Run notebooks sequentially (01 → 02 → 03...). Each notebook assumes previous steps are complete.

### Path Configuration
Notebooks assume this directory structure:
```
master-thesis/
├── notebooks/          # You are here
├── Data/
│   ├── 0_Raw/
│   └── 1_Preprocess/
├── src/                # Python modules
└── results/
```

---

## Using Custom Modules

Notebooks can import utility functions from `src/`:

```python
import sys
sys.path.append('..')

from src.preprocessing import iterative_impute, map_age_codes
from src.clustering import fit_kmodes, evaluate_kmodes_range
from src.visualization import plot_correlation_heatmap
```

---

## Outputs

Results are saved to `../results/`:
- **Figures:** `results/figures/`
- **Tables:** `results/tables/`
- **Models:** `results/models/`
