"""Shared helpers for the Education Insights Lab notebooks.

Keeping paths, plotting style and result-saving in one place means every
notebook behaves the same way and the project runs from any machine.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]

PATHS = {
    "raw": ROOT / "data" / "raw" / "us_education_system_dataset.csv",
    "clean_all": ROOT / "data" / "processed" / "institutions_clean.csv",
    "k12": ROOT / "data" / "processed" / "k12_analysis.csv",
    "figures": ROOT / "reports" / "figures",
    "results": ROOT / "reports" / "results",
    "docs": ROOT / "docs",
}

RANDOM_STATE = 42

# One consistent, colour-blind-friendly palette for the whole project.
PALETTE = {
    "primary": "#1f5f8b",
    "accent": "#e07a1f",
    "good": "#2a9d8f",
    "bad": "#c1403d",
    "grey": "#6b7280",
}


def set_style() -> None:
    """Apply the project-wide plotting style."""
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update(
        {
            "figure.dpi": 110,
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "axes.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def save_fig(name: str) -> None:
    """Save the current matplotlib figure into reports/figures."""
    PATHS["figures"].mkdir(parents=True, exist_ok=True)
    plt.savefig(PATHS["figures"] / f"{name}.png", dpi=150, bbox_inches="tight")


def _default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Cannot serialise {type(o)}")


def save_json(obj: dict, name: str) -> None:
    """Save a results dictionary to reports/results/<name>.json."""
    PATHS["results"].mkdir(parents=True, exist_ok=True)
    with open(PATHS["results"] / f"{name}.json", "w") as f:
        json.dump(obj, f, indent=2, default=_default)


def load_json(name: str) -> dict:
    """Load a results dictionary saved by save_json."""
    with open(PATHS["results"] / f"{name}.json") as f:
        return json.load(f)
