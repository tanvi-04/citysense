from pathlib import Path
import pandas as pd

from .config import DATA_INTERIM, DATA_RAW

def make_feature_table() -> Path:
    # --- Load datasets ---
    complaints = pd.read_parquet(DATA_INTERIM / "complaints_city_daily.parquet")
    weather    = pd.read_parquet(DATA_RAW / "weather_daily.parquet")
    holidays   = pd.read_parquet(DATA_RAW / "calendar_holidays.parquet")

    # --- Ensure date columns are datetime.date ---
    complaints["date"] = pd.to_datetime(complaints["date"]).dt.date
    weather["date"]    = pd.to_datetime(weather["date"]).dt.date
    holidays["date"]   = pd.to_datetime(holidays["date"]).dt.date

    # --- Merge step by step ---
    df = complaints.merge(weather, on="date", how="left")
    df = df.merge(holidays, on="date", how="left")

    # --- Save ---
    out = DATA_INTERIM / "feature_table.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return out

if __name__ == "__main__":
    p = make_feature_table()
    print(f"Saved feature table -> {p}")
