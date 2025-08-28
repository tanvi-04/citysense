from pathlib import Path
import pandas as pd
import holidays
from .config import DATA_RAW, START_DATE, END_DATE
def build_holiday_table() -> Path:
    rng = pd.date_range(START_DATE, END_DATE, freq="D")
    cal = pd.DataFrame({"date":rng})
    us_ny = holidays.US(years=range(START_DATE.year, END_DATE.year + 1), subdiv = "NY")
    cal["is_holiday"] = cal["date"].dt.date.astype(object).isin(set(us_ny))
    cal["holiday_name"] = cal["date"].dt.date.map(lambda d: us_ny.get(d, None))
    out = DATA_RAW / "calendar_holidays.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    cal.to_parquet(out, index=False)
    return out
    
if __name__ == "__main__":
    p = build_holiday_table()
    print(f"Saved \u2129 {p}")
