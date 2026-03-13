# tests/test_processor.py
from processor import stats_summary, filter_rows, sort_rows


def test_stats_empty():
    s = stats_summary([])
    assert s["n"] == 0
    assert s["age_mean"] == 0.0
    assert s["p_gt_50k"] == 0.0


def test_filter_target():
    rows = [
        {"id": 1, "age": 30.0, "education": "Bachelors", "education_num": 13, "marital_status": "",
         "occupation": "", "relationship": "", "race": "", "gender": "Male", "hours_per_week": 40.0,
         "native_country": "United-States", "greater_than_50k": 0, "age_standarized": 0.0},
        {"id": 2, "age": 45.0, "education": "HS-grad", "education_num": 9, "marital_status": "",
         "occupation": "", "relationship": "", "race": "", "gender": "Female", "hours_per_week": 50.0,
         "native_country": "United-States", "greater_than_50k": 1, "age_standarized": 0.0},
    ]
    out = filter_rows(rows, target=1)
    assert len(out) == 1
    assert out[0]["id"] == 2


def test_sort_by_age_desc():
    rows = [
        {"id": 1, "age": 30.0, "education_num": 13, "hours_per_week": 40.0, "age_standarized": 0.0, "greater_than_50k": 0},
        {"id": 2, "age": 45.0, "education_num": 9, "hours_per_week": 50.0, "age_standarized": 0.0, "greater_than_50k": 1},
    ]
    out = sort_rows(rows, by="age", descending=True)
    assert out[0]["id"] == 2