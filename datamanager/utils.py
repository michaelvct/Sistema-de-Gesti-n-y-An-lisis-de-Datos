# utils.py
from __future__ import annotations

from typing import Any, Dict, Tuple


def _strip_or_none(x: Any) -> str:
    return str(x).strip()


def validate_row(row: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Valida un registro del dataset tipo Adult Income.

    Reglas prácticas:
      - id: int > 0
      - age: float/int en [0, 120]
      - education: no vacío
      - education_num: int en [1, 16]
      - gender: no vacío
      - hours_per_week: float/int en [0, 99] (típico en este dataset)
      - greater_than_50k: 0 o 1
      - age_standarized: float (puede ser cualquier real)

    Nota: Si tu dataset tiene NA, esto los captura.
    """
    # id
    try:
        rid = int(row.get("id"))
    except (TypeError, ValueError):
        return False, "id no es entero"
    if rid <= 0:
        return False, "id debe ser > 0"

    # age
    try:
        age = float(row.get("age"))
    except (TypeError, ValueError):
        return False, "age no es numérico"
    if not (0 <= age <= 120):
        return False, "age fuera de rango [0,120]"

    # education
    education = _strip_or_none(row.get("education", ""))
    if education == "" or education.lower() == "nan":
        return False, "education vacío"

    # education_num
    try:
        edn = int(float(row.get("education_num")))
    except (TypeError, ValueError):
        return False, "education_num no es entero"
    if not (1 <= edn <= 16):
        return False, "education_num fuera de rango [1,16]"

    # gender
    gender = _strip_or_none(row.get("gender", ""))
    if gender == "" or gender.lower() == "nan":
        return False, "gender vacío"

    # hours_per_week
    try:
        hpw = float(row.get("hours_per_week"))
    except (TypeError, ValueError):
        return False, "hours_per_week no es numérico"
    if not (0 <= hpw <= 99):
        return False, "hours_per_week fuera de rango [0,99]"

    # target
    try:
        gt = int(row.get("greater_than_50k"))
    except (TypeError, ValueError):
        return False, "greater_than_50k no es entero"
    if gt not in (0, 1):
        return False, "greater_than_50k debe ser 0/1"

    # age_standarized
    try:
        _ = float(row.get("age_standarized"))
    except (TypeError, ValueError):
        return False, "age_standarized no es numérico"

    return True, ""


def normalize_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Limpieza + casteo consistente.
    Asume que validate_row ya pasó.
    """
    return {
        "id": int(row["id"]),
        "age": float(row["age"]),
        "education": str(row["education"]).strip(),
        "education_num": int(float(row["education_num"])),
        "marital_status": str(row.get("marital_status", "")).strip(),
        "occupation": str(row.get("occupation", "")).strip(),
        "relationship": str(row.get("relationship", "")).strip(),
        "race": str(row.get("race", "")).strip(),
        "gender": str(row.get("gender", "")).strip(),
        "hours_per_week": float(row["hours_per_week"]),
        "native_country": str(row.get("native_country", "")).strip(),
        "greater_than_50k": int(row["greater_than_50k"]),
        "age_standarized": float(row["age_standarized"]),
    }