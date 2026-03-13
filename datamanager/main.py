# main.py
from __future__ import annotations

from typing import Any, Dict, List, Optional

from data_loader import load_rows_from_csv
from exporter import export_to_json
from processor import filter_rows, sort_rows, stats_summary


def prompt_float(msg: str, allow_empty: bool = False) -> Optional[float]:
    while True:
        raw = input(msg).strip()
        if allow_empty and raw == "":
            return None
        try:
            return float(raw)
        except ValueError:
            print("⚠️ Ingresa un número válido.")


def prompt_int(msg: str, allow_empty: bool = False) -> Optional[int]:
    while True:
        raw = input(msg).strip()
        if allow_empty and raw == "":
            return None
        try:
            return int(raw)
        except ValueError:
            print("⚠️ Ingresa un entero válido.")


def prompt_str(msg: str, allow_empty: bool = False) -> Optional[str]:
    raw = input(msg).strip()
    if allow_empty and raw == "":
        return None
    return raw


def print_rows(rows: List[Dict[str, Any]], limit: int = 15) -> None:
    print(f"\n📌 Mostrando {min(len(rows), limit)} de {len(rows)} filas:")
    for r in rows[:limit]:
        print(
            f"- id={r['id']:5d} | age={r['age']:5.1f} | edu={r['education']:<12s} | "
            f"hrs={r['hours_per_week']:4.0f} | gender={r['gender']:<6s} | gt50k={r['greater_than_50k']}"
        )
    if len(rows) > limit:
        print(f"... (+{len(rows) - limit} más)\n")


def main() -> None:
    rows: List[Dict[str, Any]] = []
    view: List[Dict[str, Any]] = []
    last_stats: Dict[str, Any] = {}

    while True:
        print(
            "\n=== DataManager CLI (Censo/Adult Income) ===\n"
            "1 - Cargar datos\n"
            "2 - Filtrar\n"
            "3 - Ordenar\n"
            "4 - Mostrar estadísticas\n"
            "5 - Exportar estadísticas (JSON)\n"
            "6 - Salir\n"
        )
        opt = input("Elige una opción: ").strip()

        if opt == "1":
            path = input("Ruta CSV (ej: data/datos_censo_pp.csv): ").strip()
            try:
                rows, errors = load_rows_from_csv(path)
                view = rows[:]
                print(f"✅ Cargadas {len(rows)} filas válidas.")
                if errors:
                    print(f"⚠️ Filas descartadas: {len(errors)}. Ejemplo:")
                    print(errors[0])
                print_rows(view)
            except (FileNotFoundError, ValueError) as e:
                print(f"❌ Error: {e}")

        elif opt == "2":
            if not rows:
                print("⚠️ Primero carga datos (opción 1).")
                continue

            min_age = prompt_float("min_age (enter para omitir): ", allow_empty=True)
            max_age = prompt_float("max_age (enter para omitir): ", allow_empty=True)
            min_hours = prompt_float("min_hours_per_week (enter para omitir): ", allow_empty=True)
            gender = prompt_str("gender (enter para omitir): ", allow_empty=True)
            race = prompt_str("race (enter para omitir): ", allow_empty=True)
            native_country = prompt_str("native_country (enter para omitir): ", allow_empty=True)
            target = prompt_int("greater_than_50k (0/1, enter para omitir): ", allow_empty=True)

            view = filter_rows(
                rows,
                min_age=min_age,
                max_age=max_age,
                min_hours=min_hours,
                gender=gender,
                race=race,
                native_country=native_country,
                target=target,
            )
            print("✅ Filtro aplicado.")
            print_rows(view)

        elif opt == "3":
            if not view:
                print("⚠️ No hay datos para ordenar (carga o filtra primero).")
                continue

            by = input("Ordenar por (id/age/education_num/hours_per_week/age_standarized/greater_than_50k): ").strip()
            if by not in {"id", "age", "education_num", "hours_per_week", "age_standarized", "greater_than_50k"}:
                print("⚠️ Clave inválida.")
                continue

            desc = input("¿Descendente? (s/n): ").strip().lower() == "s"
            view = sort_rows(view, by=by, descending=desc)
            print("✅ Orden aplicado.")
            print_rows(view)

        elif opt == "4":
            if not view:
                print("⚠️ No hay datos para estadísticas (carga o filtra primero).")
                continue

            last_stats = stats_summary(view)
            print("\n📊 Estadísticas:")
            for k, v in last_stats.items():
                print(f"- {k}: {v}")

        elif opt == "5":
            if not last_stats:
                print("⚠️ Primero calcula estadísticas (opción 4).")
                continue
            out = input("Ruta salida JSON (ej: output_stats.json): ").strip()
            try:
                export_to_json(last_stats, out)
                print(f"✅ Exportado a: {out}")
            except Exception as e:
                print(f"❌ Error exportando: {e}")

        elif opt == "6":
            print("👋 Saliendo...")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    main()