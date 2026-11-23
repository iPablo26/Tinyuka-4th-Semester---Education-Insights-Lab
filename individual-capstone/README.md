Education Insights Lab: Diagnosing Educational Opportunity and Outcomes

AltSchool Africa | Semester 4 | Part A: Individual Data Science Capstone

Project: US Education Performance Analysis

Author: Sadiq Oni

Project Overview

This individual Data Science capstone investigates institutional factors associated with mathematics proficiency across educational institutions in the United States.

Working in the role of a Junior Data Scientist / Education Data Analyst, I analyze the US Education System dataset to explore relationships between educational resources, socioeconomic conditions, staffing, broadband access, and academic performance.

The project follows a structured data science workflow, from problem definition and data preparation through exploratory analysis, statistical investigation, machine learning, model evaluation, interpretation, and evidence-based recommendations.

The objective is to provide meaningful insights that can support educational planning, resource allocation, and further investigation into differences in academic outcomes.

Because the dataset is observational, the analysis distinguishes statistical associations and predictive relationships from causal conclusions.

Project Objectives

The primary objective is to investigate the institutional factors associated with mathematics proficiency and assess how accurately institutional characteristics can predict this outcome.

The specific objectives are to:

1. Understand the dataset's structure, variables, completeness, and quality.
2. Identify and appropriately address missing values, duplicates, inconsistent categories, and potential outliers.
3. Explore institutional characteristics, educational resources, socioeconomic indicators, and academic outcomes.
4. Apply appropriate statistical methods to investigate relationships and assess supporting evidence.
5. Develop and compare machine learning regression models for predicting mathematics proficiency.
6. Evaluate predictive performance using suitable regression metrics.
7. Interpret model predictions and identify influential institutional characteristics.
8. Translate analytical findings into evidence-based business and policy insights.
9. Develop practical recommendations while acknowledging limitations and uncertainty.
10. Document the analytical process clearly and reproducibly.

1. Problem Definition

1.1 Problem Statement

Educational institutions across the United States differ in financial resources, staffing capacity, socioeconomic conditions, access to technology, and academic outcomes.

However, the presence of these differences does not automatically explain which institutional factors are most strongly associated with mathematics proficiency.

This project investigates these relationships using exploratory analysis, statistical methods, and machine learning to provide evidence that can support informed educational decisions.

1.2 Stakeholder Identification

The primary stakeholder is an education-focused organization interested in understanding differences in educational opportunities and academic performance across US institutions.

Other potential stakeholders include:

- Education policymakers responsible for resource allocation.
- School administrators seeking to understand institutional performance.
- Education researchers investigating academic outcomes.
- Educational funding organizations interested in identifying areas of disadvantage.

1.3 Why the Problem Matters

Understanding relationships between institutional resources and mathematics proficiency can help stakeholders identify educational disparities, investigate potential barriers to academic achievement, and prioritize areas requiring additional attention.

The analysis supports evidence-based planning without assuming that observed relationships establish causation.

1.4 Primary Research Question

How are institutional funding, student-teacher ratios, socioeconomic conditions, and broadband access associated with mathematics proficiency across US educational institutions, and how accurately can mathematics proficiency be predicted using institutional characteristics?

Primary outcome variable: "math_proficiency_pct"

Initial explanatory variables:

- Per-pupil expenditure: "per_pupil_expenditure_usd"
- Student-teacher ratio: "student_teacher_ratio"
- Socioeconomic disadvantage: "percent_free_reduced_lunch"
- Broadband access: "broadband_access_pct"

Additional institutional characteristics may be considered where relevant and supported by the analysis.

1.5 Supporting Research Questions

1. How does mathematics proficiency vary across institutions and educational levels?
2. What relationship exists between per-pupil educational expenditure and mathematics proficiency?
3. How are student-teacher ratios associated with mathematics proficiency?
4. Is socioeconomic disadvantage associated with differences in mathematics proficiency?
5. What relationship exists between broadband access and academic performance?
6. Do relationships between institutional resources and mathematics proficiency remain evident when other relevant institutional characteristics are considered?
7. How accurately can machine learning models predict mathematics proficiency using available institutional characteristics?
8. Which institutional characteristics contribute most strongly to the model's predictions?

1.6 Assumptions

- Each dataset record represents an educational institution.
- Mathematics proficiency is recorded on an interpretable percentage scale.
- Institutional resources and socioeconomic indicators provide relevant information for the research question.
- Differences between educational levels may require additional consideration.
- Available institutional data can support statistical investigation and predictive modelling.

1.7 Limitations

- Observational data: Identified relationships do not establish causation.
- Missing information: Some indicators may be unavailable or inapplicable to particular educational levels.
- Institutional differences: Institutions at different educational levels may not be directly comparable.
- Unobserved factors: Some influences on academic performance may not be captured.
- Generalizability: Findings may not apply to institutions outside the dataset.

These limitations are considered when interpreting findings and developing recommendations.

2. Data Understanding

The dataset was examined to establish its structure, content, completeness, and suitability for the research question.

The investigation covered:

- Dataset dimensions and initial inspection.
- Numerical and categorical variables.
- Missing values and completeness.
- Duplicate records and institution identifiers.
- Categorical values and coverage.
- Descriptive statistics and potential anomalies.
- Target and explanatory variables.
- Data dictionary development.
- Expected relationships between variables.

3. Data Cleaning and Preparation

A structured data-cleaning process was undertaken to improve data quality and prepare the dataset for analysis.

The process covered:

- Missing-value identification and investigation.
- Assessment of appropriate missing-data treatments.
- Duplicate detection.
- Validation of numerical ranges and percentages.
- Investigation of inconsistent categorical values.
- Outlier identification and assessment.
- Consideration of institution-level applicability.
- Documentation and justification of cleaning decisions.

Cleaning decisions were guided by the meaning of each variable and the analytical objectives rather than applying automatic replacements indiscriminately.

4. Exploratory Data Analysis (EDA)

Exploratory analysis was conducted to understand distributions, institutional differences, and relationships relevant to mathematics proficiency.

Univariate analysis: Examined individual variable distributions and descriptive statistics.

Bivariate analysis: Investigated relationships between mathematics proficiency and institutional funding, staffing, socioeconomic conditions, and broadband access.

Multivariate analysis: Considered relationships involving multiple institutional characteristics to provide a broader understanding of academic performance.

Appropriate visualizations and descriptive summaries were used to support interpretation.

5. Statistical Analysis

Statistical methods were applied to investigate selected relationships and assess the evidence supporting the research questions.

The analysis considered:

- The suitability of statistical methods for the variables involved.
- Relationships between institutional characteristics and academic outcomes.
- Statistical evidence and interpretation.
- Practical relevance and analytical limitations.

Statistical conclusions were interpreted within the observational nature of the dataset.

6. Machine Learning

The machine learning component focuses on predicting mathematics proficiency using institutional characteristics.

Problem type: Supervised regression

Target variable: "math_proficiency_pct"

The modelling workflow covers:

- Selection of relevant predictor variables.
- Preparation of modelling data.
- Separation of training and testing data.
- Development of regression models.
- Comparison of predictive approaches.

The objective is to assess whether institutional characteristics provide useful predictive information about mathematics proficiency.

7. Model Evaluation

Regression model performance was assessed using appropriate evaluation metrics, including:

- Mean Absolute Error (MAE): Measures the average absolute prediction error.
- Root Mean Squared Error (RMSE): Measures prediction error while giving greater weight to larger errors.
- R-squared (R²): Measures the proportion of outcome variation explained by the model on the evaluated data.

Model performance was considered in relation to predictive accuracy, error magnitude, and the limitations of the available data.

8. Model Interpretation

Model interpretation focused on understanding how institutional characteristics contributed to predictions of mathematics proficiency.

The investigation considered:

- Influential predictor variables.
- Model coefficients or feature importance, where appropriate.
- Relationships between predictors and model outputs.
- Practical interpretation of predictive findings.
- Limitations of model-based conclusions.

Predictive importance was not treated as proof of a causal relationship.

9. Business and Policy Insights

Analytical findings were translated into evidence-based insights relevant to educational stakeholders.

The insights were structured around:

- The finding and its practical meaning.
- Supporting analytical evidence.
- Possible explanations.
- Limitations and uncertainty.
- Implications for further stakeholder investigation.

The objective was to connect statistical and predictive findings to real educational decision-making.

10. Recommendations and Conclusion

Recommendations were developed to support evidence-informed educational planning and investigation.

Each recommendation considers:

- Finding: The identified issue or relationship.
- Evidence: Analytical results supporting the finding.
- Recommendation: A proposed stakeholder action.
- Expected impact: The potential benefit of the action.
- Caveat: Important limitations or uncertainties.

The project concludes by summarizing the analytical investigation, its contribution to understanding mathematics proficiency, and the importance of interpreting observational evidence responsibly.

Methodology and Project Workflow

The individual capstone follows the ten required stages:

No.| Project Stage| Status
1| Problem Definition| Complete
2| Data Understanding and Data Dictionary| Complete
3| Data Cleaning and Preparation| Complete
4| Exploratory Data Analysis| Complete
5| Statistical Analysis| Complete
6| Machine Learning| Complete
7| Model Evaluation| Complete
8| Model Interpretation| Complete
9| Business and Policy Insights| Complete
10| Recommendations and Conclusion| Complete

Tools and Technologies

- Python: Data analysis and machine learning.
- Jupyter Notebook: Analytical documentation and code execution.
- PyCharm: Development environment.
- Git: Version control.
- GitHub: Project documentation, repository management, and pull request submission.

The notebook contains the analytical implementation and supporting outputs.

Project Files

The individual capstone submission is organized under:

"individual-capstone/"

The submission includes:

- A Jupyter Notebook containing the individual capstone analysis.
- This README documenting the project's objectives, methodology, workflow, and scope.

The project uses the provided US Education System dataset. Access to the dataset is required to reproduce analyses that depend on the original CSV file.

Reproducibility

To reproduce the analysis:

1. Obtain the US Education System dataset provided for the capstone.
2. Download the submitted Jupyter Notebook.
3. Open the notebook in a Python environment supporting Jupyter.
4. Install the Python packages imported by the notebook.
5. Make the dataset available at the file path expected by the notebook, adjusting the path if necessary.
6. Execute the notebook cells sequentially and review the outputs.

Reproducibility depends on access to the required dataset, packages, and compatible Python environment.

Project Scope

This repository submission covers Part A: Individual Capstone of the AltSchool Africa Semester 4 Data Science Capstone Project.

The group project, collaborative dashboard, and group-specific deliverables are outside the scope of this submission.

Conclusion

This capstone demonstrates the application of a structured data science workflow to investigate educational opportunity and mathematics proficiency across US institutions.

By combining data preparation, exploratory analysis, statistical reasoning, machine learning, model evaluation, interpretation, and evidence-based recommendations, the project aims to support a clearer understanding of institutional factors associated with academic performance.

The findings are intended to inform further investigation and responsible educational decision-making rather than establish causal conclusions.
