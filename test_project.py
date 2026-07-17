import os
import pandas as pd
from project import is_csv, clean_column_name, numeric_summary


def test_is_csv():
    assert is_csv("data.csv") is True
    assert is_csv("DATA.CSV") is True
    assert is_csv("notes.txt") is False


def test_clean_column_name():
    assert clean_column_name(" Price ") == "Price"
    assert clean_column_name("Spending Score 1-100") == "Spending_Score_1-100"
    assert clean_column_name("CustomerID") == "CustomerID"


def test_numeric_summary():
    df = pd.DataFrame({
        "age": [20, 30, 40],
        "income": [1000, 2000, 3000],
        "gender": ["M", "F", "F"]
    })

    result = numeric_summary(df)

    assert "age" in result
    assert "income" in result
    assert "count" in result
    assert "mean" in result
