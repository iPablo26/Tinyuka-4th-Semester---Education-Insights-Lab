# Education Insights Lab — Individual Capstone

**AltSchool Africa · Data Science, Semester 4 (Tinyuka) · Part A — Individual Capstone**

A start-to-finish analysis of what shapes academic outcomes across 5,000 U.S. institutions, and what an education-equity organisation could do about it.

---

## The question
Across U.S. schools, which conditions — family income levels, funding, staffing, demographics and broadband access — line up most closely with maths proficiency, and how much of the gap between schools can those conditions actually explain?

## What I found
- **Poverty is the main fault line.** The share of students on free/reduced lunch correlates about **−0.62** with maths proficiency. High-poverty (Title I Schoolwide) schools average roughly **52%** proficiency against **72%** for the better-off ones.
- **Broadband is a real, separate lever.** Better-connected schools score about **13 points** higher, and that gap holds *inside every poverty band* — so connectivity isn't just standing in for wealth.
- **Opportunity conditions explain about a third of the variation** (R² ≈ 0.35), cutting the average prediction error from 13.4 to ~10.5 proficiency points. The rest sits in things the data can't see — teaching, leadership, what happens at home.
- **STEM certification is a red herring here.** It shows no link to Title I status (chi-square p ≈ 0.29), so it shouldn't be used to decide who gets support. I report that null result rather than force a model onto noise.

## How it's laid out
```
oluwatobi-education-insights-lab/
├── README.md                     # this file
├── requirements.txt              # dependencies
├── .gitignore
├── data/
│   ├── README.md                 # dataset description + missing-value note
│   └── us_education_system_dataset.csv
└── notebooks/
    └── Education_Insights_Lab_Capstone.ipynb   # the full analysis
```

## What the notebook covers
Problem definition → data understanding (with a data dictionary) → cleaning and sense-checks → exploratory analysis → three statistical tests → a regression model (Linear Regression vs Random Forest) → evaluation → interpretation → insights and recommendations → limitations and reflection.

## Running it
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Education_Insights_Lab_Capstone.ipynb
```
The random seed is fixed (`SEED = 42`), so the results reproduce exactly.

## A few honest caveats
This is a single snapshot, so every result is an association, not proof of cause. The test-score columns only exist for secondary schools, so the model sticks to conditions shared by every institution. And the data looks at least partly synthetic — read the numbers as relative signal, not official statistics.
