# data_loader.py
from __future__ import annotations

import csv
from typing import Any, Dict, List, Tuple

from utils import normalize_row, validate_row


def load_rows_from_csv(path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Lee el CSV y devuelve:
      - rows_validos: dicts normalizados
      - errors: filas descartadas con razón

    Misma lógica del proyecto original: robusto y trazable.
    """
    rows: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []

    try:
        with open(path, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for line_num, row in enumerate(reader, start=2):
                ok, reason = validate_row(row)
                if not ok:
                    errors.append({"line": line_num, "row": row, "reason": reason})
                    continue
                rows.append(normalize_row(row))

    except FileNotFoundError as e:
        raise FileNotFoundError(f"No se encontró el archivo: {path}") from e
    except Exception as e:
        raise ValueError(f"Error leyendo CSV: {e}") from e

    return rows, errors