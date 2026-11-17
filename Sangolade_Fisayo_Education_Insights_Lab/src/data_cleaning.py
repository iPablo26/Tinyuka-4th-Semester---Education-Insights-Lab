"""Reproducible cleaning pipeline for the US Education System dataset.

Run from the project root:

    python src/data_cleaning.py

This reproduces the two processed files that notebooks 03-06 consume:
    data/processed/institutions_clean.csv   (all 5,000 institutions, with flags)
    data/processed/k12_analysis.csv         (K-12 schools only: the analysis scope)

Every decision here is justified in notebooks/02_data_cleaning.ipynb.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent))
from utils import PATHS  # noqa: E402

K12_LEVELS = ["Elementary School", "Middle School", "High School", "K-12 Combined"]
HIGHER_ED = ["2-Year College", "4-Year University"]
NO_GRADUATION_LEVELS = ["Elementary School", "Middle School"]

PCT_COLS = [
    "percent_free_reduced_lunch",
    "racial_white_pct",
    "racial_black_pct",
    "racial_hispanic_pct",
    "racial_asian_pct",
    "racial_native_pct",
    "racial_two_or_more_pct",
    "special_education_pct",
    "english_learner_pct",
    "federal_funding_pct",
    "state_funding_pct",
    "local_funding_pct",
    "math_proficiency_pct",
    "reading_proficiency_pct",
    "graduation_rate_pct",
    "chronic_absenteeism_pct",
    "ap_ib_participation_pct",
    "postsecondary_enrollment_pct",
    "broadband_access_pct",
]

RACE_COLS = [c for c in PCT_COLS if c.startswith("racial_")]
FUNDING_COLS = ["federal_funding_pct", "state_funding_pct", "local_funding_pct"]


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all cleaning decisions and return a new DataFrame.

    Missing values in SAT / ACT / AP-IB / postsecondary columns are deliberately
    LEFT AS NaN: they are structurally missing (the metric does not exist for
    that school level), so imputing or zero-filling would invent data.
    """
    out = df.copy()

    # 1. Text hygiene: strip whitespace from text columns only (missing values stay missing,
    #    they are NOT turned into the string "nan").
    for col in out.select_dtypes(include=["object", "string"]).columns:
        out[col] = out[col].str.strip()

    # 2. Scope flags.
    out["is_k12"] = out["level"].isin(K12_LEVELS)
    out["is_higher_ed"] = out["level"].isin(HIGHER_ED)

    # 3. Graduation rate is not meaningful for elementary / middle schools
    #    (they do not graduate students), so set it to NaN there.
    out.loc[out["level"].isin(NO_GRADUATION_LEVELS), "graduation_rate_pct"] = np.nan

    # 4. Consistency flag for student-teacher ratio.
    out["str_calculated"] = out["total_enrollment"] / out["number_of_teachers"]
    out["str_mismatch_flag"] = (
        (out["str_calculated"] - out["student_teacher_ratio"]).abs() > 0.5
    )

    # 5a. Fixed funding mix. Every Private Non-Profit and Private Religious institution has
    #     exactly 0% federal / 2% state / 98% local funding. This is a structural pattern tied to
    #     school control, NOT a reporting cap (see notebook 02, section 3.7).
    out["private_fixed_funding_flag"] = (
        (out["federal_funding_pct"] == 0)
        & (out["state_funding_pct"] == 2)
        & (out["local_funding_pct"] == 98)
    )

    # 5b. Genuine ceilings (censored values) in the two proficiency outcomes.
    out["reading_capped_flag"] = out["reading_proficiency_pct"] >= 98
    out["math_capped_flag"] = out["math_proficiency_pct"] >= 96

    # 6. Outlier flag for per-pupil expenditure (Tukey fences, 1.5 x IQR).
    q1, q3 = out["per_pupil_expenditure_usd"].quantile([0.25, 0.75])
    iqr = q3 - q1
    out["ppe_outlier_flag"] = (
        (out["per_pupil_expenditure_usd"] < q1 - 1.5 * iqr)
        | (out["per_pupil_expenditure_usd"] > q3 + 1.5 * iqr)
    )

    # 7. Engineered features used in analysis / modelling.
    out["ppe_k"] = out["per_pupil_expenditure_usd"] / 1000  # $ thousands per pupil
    out["log_enrollment"] = np.log(out["total_enrollment"])
    out["stem_certified"] = (out["stem_certified_flag"] == "Yes").astype(int)
    out["locale_group"] = out["nces_locale"].str.split(" - ").str[0]

    return out


def make_k12(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Return the K-12 analysis scope with a poverty tertile label."""
    k12 = df_clean[df_clean["is_k12"]].copy()
    k12["poverty_tertile"] = pd.qcut(
        k12["percent_free_reduced_lunch"],
        q=3,
        labels=["Low poverty", "Mid poverty", "High poverty"],
    )
    return k12.reset_index(drop=True)


TERTILES = ["Low poverty", "Mid poverty", "High poverty"]


def load_k12() -> pd.DataFrame:
    """Load the processed K-12 analysis file and restore the ordered tertile."""
    k12 = pd.read_csv(PATHS["k12"])
    k12["poverty_tertile"] = pd.Categorical(
        k12["poverty_tertile"], categories=TERTILES, ordered=True
    )
    return k12


def main() -> None:
    raw = pd.read_csv(PATHS["raw"])
    df_clean = clean(raw)
    k12 = make_k12(df_clean)
    PATHS["clean_all"].parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(PATHS["clean_all"], index=False)
    k12.to_csv(PATHS["k12"], index=False)
    print(f"Raw rows:          {len(raw):,}")
    print(f"Clean rows (all):  {len(df_clean):,} -> {PATHS['clean_all']}")
    print(f"K-12 analysis set: {len(k12):,} -> {PATHS['k12']}")


if __name__ == "__main__":
    main()
