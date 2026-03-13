# processor.py
from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Literal, Optional


SortKey = Literal[
    "id", "age", "education_num", "hours_per_week", "age_standarized", "greater_than_50k"
]


def filter_rows(
    rows: List[Dict[str, Any]],
    *,
    min_age: Optional[float] = None,
    max_age: Optional[float] = None,
    gender: Optional[str] = None,
    race: Optional[str] = None,
    native_country: Optional[str] = None,
    target: Optional[int] = None,
    min_hours: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """
    Filtros típicos de exploración.
    Todos son opcionales.
    """
    out: List[Dict[str, Any]] = []
    for r in rows:
        if min_age is not None and r["age"] < min_age:
            continue
        if max_age is not None and r["age"] > max_age:
            continue
        if min_hours is not None and r["hours_per_week"] < min_hours:
            continue
        if gender is not None and r["gender"].lower() != gender.lower():
            continue
        if race is not None and r["race"].lower() != race.lower():
            continue
        if native_country is not None and r["native_country"].lower() != native_country.lower():
            continue
        if target is not None and r["greater_than_50k"] != target:
            continue
        out.append(r)
    return out


def sort_rows(rows: List[Dict[str, Any]], *, by: SortKey = "age", descending: bool = False):
    return sorted(rows, key=lambda r: r[by], reverse=descending)


def mean(xs: List[float]) -> float:
    return 0.0 if not xs else sum(xs) / len(xs)


def stats_summary(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Estadísticas útiles para este dataset:
      - total filas
      - edad promedio / min / max
      - horas promedio
      - proporción >50k
      - conteos por education, gender, race, native_country (top-k)
    """
    n = len(rows)
    if n == 0:
        return {
            "n": 0,
            "age_mean": 0.0,
            "age_min": None,
            "age_max": None,
            "hours_mean": 0.0,
            "p_gt_50k": 0.0,
            "counts": {},
        }

    ages = [r["age"] for r in rows]
    hours = [r["hours_per_week"] for r in rows]
    p_gt = sum(r["greater_than_50k"] for r in rows) / n

    def top_counts(key: str, k: int = 10) -> Dict[str, int]:
        c = Counter(r[key] for r in rows)
        return dict(c.most_common(k))

    return {
        "n": n,
        "age_mean": round(mean(ages), 3),
        "age_min": min(ages),
        "age_max": max(ages),
        "hours_mean": round(mean(hours), 3),
        "p_gt_50k": round(p_gt, 4),
        "counts": {
            "education_top10": top_counts("education", 10),
            "gender": dict(Counter(r["gender"] for r in rows)),
            "race_top10": top_counts("race", 10),
            "native_country_top10": top_counts("native_country", 10),
            "occupation_top10": top_counts("occupation", 10),
        },
    }