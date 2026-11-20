# Data

## `us_education_system_dataset.csv`
The dataset provided for the Semester 4 capstone. It holds **5,000 U.S. institutions** across **35 columns** — location, level, control, Title I status, enrolment, staffing, socioeconomic indicators, demographics, spending, funding mix, academic outcomes, graduation, absenteeism, STEM certification, broadband access, and (for secondary schools only) SAT/ACT/AP-IB/postsecondary figures.

A full data dictionary sits inside the notebook (section 3).

## A note on missing values
Four columns — `avg_sat_score`, `avg_act_score`, `ap_ib_participation_pct`, `postsecondary_enrollment_pct` — are blank for most rows. This isn't messy data: those tests only apply to secondary and tertiary institutions, so elementary and middle schools have nothing to report. The notebook keeps these columns but leaves them out of the model rather than filling them with zeros.

## Generated file
Running the notebook writes `us_education_cleaned.csv` (the tidied, analysis-ready version). It's git-ignored because the notebook recreates it on demand.
