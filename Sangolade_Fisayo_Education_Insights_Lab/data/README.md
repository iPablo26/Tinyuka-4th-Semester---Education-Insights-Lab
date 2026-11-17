# Data

## `raw/us_education_system_dataset.csv`
The dataset provided by AltSchool Africa for the Semester 4 capstone.
5,000 institutions x 35 columns. **Never edit this file by hand.**

## `processed/` (generated, not committed)
Created by running:

```bash
python src/data_cleaning.py
```

| File | Rows | Description |
|---|---|---|
| `institutions_clean.csv` | 5,000 | All institutions after cleaning, with flags and engineered features |
| `k12_analysis.csv` | 4,642 | K-12 schools only (the analysis scope), plus a poverty-tertile label |

All cleaning decisions are justified in `notebooks/02_data_cleaning.ipynb` and logged in `docs/cleaning_log.csv`.
The column definitions are in `docs/data_dictionary.csv`.
