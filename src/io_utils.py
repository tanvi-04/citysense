import pandas as pd
from pathlib import Path
from . import config
def load_csv(path: Path, **kwargs) -> pd.DataFrame:
return pd.read_csv(path, low_memory=False, **kwargs)
def save_parquet(df: pd.DataFrame, path: Path) -> None:
path.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(path, index=False)
