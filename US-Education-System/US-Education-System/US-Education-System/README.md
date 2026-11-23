# Education Insights Lab: Understanding the Factors Associated with Mathematics Proficiency in US Institutions

## 1. Project Overview

This project investigates institutional, socioeconomic, staffing, funding, and technological characteristics associated with mathematics proficiency across educational institutions in the United States.

Using a dataset containing 5,000 educational institutions, the project applies exploratory data analysis, statistical analysis, data visualization, and machine learning to identify factors associated with mathematics proficiency.

The goal is to understand how institutional and socioeconomic characteristics relate to educational outcomes and identify factors that may help inform educational improvement strategies.

## 2. Research Question

What institutional, socioeconomic, staffing, funding, and technological characteristics are associated with mathematics proficiency across educational institutions in the United States?

## 3. Project Objectives

- Examine the characteristics of educational institutions across the United States.
- Explore the distribution of mathematics proficiency.
- Investigate relationships between mathematics proficiency and socioeconomic factors.
- Analyze the relationships between academic performance and institutional characteristics.
- Develop machine learning models to predict mathematics proficiency.
- Identify the most influential features associated with mathematics proficiency.

## 4. Dataset Description

The dataset contains 5,000 records and 35 columns representing educational institutions in the United States.

The dataset includes:

- Institution information and location.
- Institution level and control type.
- Student enrollment and teacher information.
- Socioeconomic indicators.
- Student demographic characteristics.
- Institutional expenditure and funding sources.
- Mathematics and reading proficiency.
- Graduation rate and chronic absenteeism.
- Technology access and STEM certification.

**Dataset source:** https://drive.google.com/file/d/18p441Sg7Y5uJIu7p0qU5EvaZGAMFD7Dx/view?usp=sharing

## 5. Tools and Technologies

The following tools and libraries were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Kaggle Notebooks
- GitHub

## 6. Methodology

The project followed these major stages:

1. Data loading and inspection.
2. Data cleaning and preprocessing.
3. Exploratory data analysis.
4. Descriptive statistical analysis.
5. Data visualization.
6. Correlation analysis.
7. Multiple linear regression modelling.
8. Permutation feature importance.
9. Model evaluation and interpretation.

## 7. Key Findings

### 7.1 Mathematics Proficiency

The average mathematics proficiency across the institutions was approximately 60%.

Most institutions recorded mathematics proficiency levels between 50% and 70%.

### 7.2 Socioeconomic Factors

The percentage of students receiving free or reduced-price lunch had a moderately strong negative correlation with mathematics proficiency (-0.624).

This suggests that institutions serving larger proportions of economically disadvantaged students tended to record lower mathematics proficiency.

### 7.3 Reading and Mathematics Proficiency

Reading proficiency had a strong positive correlation with mathematics proficiency (0.770).

This indicates a strong relationship between reading and mathematics performance across the institutions.

### 7.4 Chronic Absenteeism

Chronic absenteeism had a negative correlation with mathematics proficiency (-0.448), suggesting that institutions with higher absenteeism tended to have lower mathematics proficiency.

### 7.5 Broadband Access

Broadband access had a positive correlation with mathematics proficiency (0.487).

## 8. Machine Learning Models

Two multiple linear regression models were developed to examine the factors associated with mathematics proficiency.

- **Model 1:** Included reading proficiency as a predictor.
- **Model 2:** Excluded reading proficiency to examine the contribution of other institutional and socioeconomic characteristics.

### Model Performance

| Evaluation Metric | Model 1 (Including Reading) | Model 2 (Excluding Reading) |
|---|---:|---:|
| R² Score | 0.627 | 0.420 |
| Mean Absolute Error (MAE) | 8.11 | 10.04 |
| Root Mean Squared Error (RMSE) | 10.02 | 12.50 |

### Feature Importance

Reading proficiency was the strongest predictor in Model 1.

When reading proficiency was excluded, the percentage of students receiving free or reduced-price lunch became the most influential predictor, followed by chronic absenteeism.

These findings highlight the importance of socioeconomic conditions and attendance when examining mathematics proficiency.

## 9. Recommendations

Based on the findings, the following recommendations are proposed:

1. **Targeted Academic Support:** Provide additional academic support to institutions serving economically disadvantaged student populations.
2. **Attendance Improvement:** Strengthen strategies to reduce chronic absenteeism.
3. **Integrated Learning:** Support literacy and mathematics development together.
4. **Resource Allocation:** Review institutional funding and expenditure to identify opportunities for more effective resource allocation.
5. **Digital Access:** Continue improving broadband and digital learning access across educational institutions.

## 10. Limitations

- The analysis is based on observational data and does not establish causal relationships.
- Some variables contain substantial missing values.
- The machine learning models do not explain all variation in mathematics proficiency.
- Relationships between predictors may influence model interpretation.
- Results may not generalize to every educational institution.

## 11. Conclusion

This project explored institutional and socioeconomic factors associated with mathematics proficiency across educational institutions in the United States.

The analysis identified reading proficiency, socioeconomic conditions, and chronic absenteeism as important factors associated with mathematics proficiency.

The machine learning results further demonstrated that socioeconomic and institutional characteristics provide useful information for understanding educational outcomes.

Overall, the findings emphasize the importance of considering both student circumstances and institutional conditions when examining mathematics proficiency.

## 12. Project Files

The project includes:

- `README.md` – Project documentation.
- `education_insights_lab.ipynb` – Jupyter Notebook containing the complete analysis, visualizations, statistical findings, and machine learning models.

## 13. Author

**Bello Muhammed**

AltSchool Africa  
Semester 4 Data Science Capstone Project
