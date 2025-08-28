from __future__ import annotations
from datetime import datetime, date, time
from pathlib import Path
import pandas as pd
import requests
from typing import Dict, Any

from .config import DATA_INTERIM, START_DATE, END_DATE

BASE = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

def _iso_range(d0: date, d1: date) -> tuple[str, str]:
    """Inclusive start to inclusive end-of-day in ISO for the API."""
    start = datetime.combine(d0, time.min).isoformat()
    end   = datetime.combine(d1, time.max).isoformat()
    return start, end

def fetch_daily_counts(start: date = START_DATE, end: date = END_DATE) -> pd.DataFrame:
    """
    Use SoQL to aggregate daily counts *on the server*.
    Returns a DataFrame with columns: date, complaints_city
    """
    start_iso, end_iso = _iso_range(start, end)

    # SoQL params: group by truncated date, count rows
    params: Dict[str, Any] = {
        "$select": "date_trunc_ymd(created_date) AS date, count(1) AS complaints_city",
        "$where":  f"created_date between '{start_iso}' and '{end_iso}'",
        "$group":  "date",
        "$order":  "date",
        "$limit":  50000  # well above the number of days returned
    }

    resp = requests.get(BASE, params=params, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    # Convert to DataFrame and types
    df = pd.DataFrame(data)
    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["complaints_city"] = pd.to_numeric(df["complaints_city"])
    return df

def save_daily_counts(df: pd.DataFrame, out: Path | None = None) -> Path:
    if out is None:
        out = DATA_INTERIM / "complaints_city_daily.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return out

if __name__ == "__main__":
    df = fetch_daily_counts()
    p = save_daily_counts(df)
    print(f"Rows: {len(df)}  Saved → {p}")
