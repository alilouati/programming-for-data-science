"""Generate the synthetic teaching datasets used in Chapters 4 and 5.

All data here is SYNTHETIC. It is generated from fixed random seeds so every
student gets exactly the same files. Run from the repository root:

    python data/make_datasets.py

Files written to data/:
    students.csv          Ch 4-5  exam grades with realistic data problems
    courses.csv           Ch 4    course catalogue, used for merge examples

The Chapter 6 file alkharj_accidents_2022.csv is REAL data and is not
generated here.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Chapter 4-5: students and courses
# ---------------------------------------------------------------------------
def make_students(n=120, seed=7):
    rng = np.random.default_rng(seed)
    first = ["Abdullah", "Mohammed", "Fahad", "Khalid", "Omar", "Saad", "Faisal",
             "Nora", "Sara", "Reem", "Lama", "Huda", "Maha", "Aisha", "Yousef",
             "Turki", "Hessa", "Abeer", "Majed", "Dana"]
    ids = [f"S{2025000 + i}" for i in range(n)]
    gender = rng.choice(["M", "F"], size=n)
    names = rng.choice(first, size=n)
    program = rng.choice(["MDS", "MIS", "MCS"], size=n, p=[0.5, 0.3, 0.2])
    ability = rng.normal(0, 1, n)
    mid1 = np.clip(72 + 10 * ability + rng.normal(0, 7, n), 20, 100).round()
    mid2 = np.clip(70 + 11 * ability + rng.normal(0, 8, n), 15, 100).round()
    final = np.clip(68 + 12 * ability + rng.normal(0, 9, n), 10, 100).round()
    hours = np.clip(6 + 2.5 * ability + rng.normal(0, 2, n), 0, 20).round(1)
    df = pd.DataFrame({"student_id": ids, "name": names, "gender": gender,
                       "program": program, "study_hours_per_week": hours,
                       "midterm1": mid1, "midterm2": mid2, "final": final})
    # Planted data problems for the cleaning lesson
    df.loc[rng.choice(n, 6, replace=False), "midterm2"] = np.nan      # missing
    df.loc[rng.choice(n, 3, replace=False), "final"] = -1             # sentinel
    df.loc[rng.choice(n, 2, replace=False), "study_hours_per_week"] = 99  # typo
    df.loc[rng.choice(n, 4, replace=False), "program"] = "mds"        # casing
    df = pd.concat([df, df.iloc[[5, 17]]], ignore_index=True)         # duplicates
    return df


def make_courses():
    return pd.DataFrame({
        "program": ["MDS", "MIS", "MCS", "MBA"],
        "program_name": ["Master of Data Science", "Master of Information Systems",
                         "Master of Computer Science", "Master of Business Administration"],
        "credit_hours": [36, 36, 33, 42],
    })


def main():
    make_students().to_csv(OUT / "students.csv", index=False)
    make_courses().to_csv(OUT / "courses.csv", index=False)
    print(f"students: {len(make_students())} rows written")


if __name__ == "__main__":
    main()
