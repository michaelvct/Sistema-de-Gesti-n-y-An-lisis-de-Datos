# exporter.py
from __future__ import annotations

import json
from typing import Any, Dict


def export_to_json(data: Dict[str, Any], path: str) -> None:
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)