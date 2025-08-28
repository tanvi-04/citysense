from datetime import datetime
from pathlib import Path
import pandas as pd
from meteostat import Daily, Point

from .config import DATA_RAW, START_DATE, END_DATE

def fetch_weather() -> Path:
    # Define NYC coordinates
    nyc = Point(40.7128, -74.0060)

    # Convert config dates (date) to datetime
    start = datetime(START_DATE.year, START_DATE.month, START_DATE.day)
    end   = datetime(END_DATE.year, END_DATE.month, END_DATE.day)

    # Fetch daily weather between START_DATE and END_DATE
    df = Daily(nyc, start, end).fetch().reset_index()

    # Rename columns for clarity
    df = df.rename(columns={
        'time':'date',
        'tavg':'temp_avg_c',
        'tmin':'temp_min_c',
        'tmax':'temp_max_c',
        'prcp':'precip_mm',
        'snow':'snow_mm',
        'wspd':'wind_kmh',
        'pres':'pressure_hpa'
    })

    # Save to raw data folder
    out = DATA_RAW / "weather_daily.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return out

if __name__ == "__main__":
    p = fetch_weather()
    print(f"Saved → {p}")
