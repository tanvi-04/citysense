# CitySense: The Python Data Analysis + AI  (End-to-End Project)

**CitySense** is a complete end-to-end data analysis and machine learning project.  
It predicts and explains **daily NYC 311 complaint volume** using weather, air quality, transit ridership, and holidays.  

This repo is structured as a portfolio-ready “bible” for Python data analysis: it covers **data loading, cleaning, feature engineering, visualization, modeling, evaluation, explainability, and delivery**.  

---

## 🚀 Project Overview
- **Goal:** Forecast NYC 311 daily complaints & uncover key drivers (weather, holidays, etc.)
- **Why it matters:**  
  Urban complaint data helps city agencies allocate resources (sanitation, noise enforcement, etc.).  
  Adding weather + holiday context improves predictions and storytelling.
- **Deliverables:**  
  1. Cleaned, feature-rich datasets (Parquet & CSV)  
  2. Baseline & ML models (Naive, Linear Regression, Random Forest)  
  3. Evaluation (MAE, RMSE, sMAPE)  
  4. **Interactive Tableau dashboard** for non-technical stakeholders  

---

## 📊 Interactive Dashboard
Explore the live Tableau dashboard here:  
👉 [NYC 311 Complaints: Actual vs Predicted & Drivers](https://public.tableau.com/app/profile/tanvi.patel1273/viz/NYC311ComplaintsAnalysis_17569472685230/NYC311ComplaintsActualvsPredictedDrivers?publish=yes)

Dashboard includes:
- Actual vs Predicted complaints over time  
- Holiday vs Non-Holiday comparison  
- Weather impact scatterplot with trendline  

---

## 🛠️ Tech Stack
**Python (core analysis & modeling):**
- `pandas`, `numpy` → data cleaning & wrangling  
- `matplotlib`, `seaborn`, `plotly` → EDA & visualization  
- `scikit-learn` → Linear Regression, Random Forest, metrics  
- `meteostat` → historical daily weather API  
- `holidays` → US/NY holiday calendar  

**Reproducibility & DevOps:**
- Virtual environment (`.venv`)  
- Git + GitHub (branching, commits, pushes)  
- `.gitignore` → ignores large datasets & models  

**Visualization / Delivery:**
- **Tableau Public** → interactive, shareable dashboard  
- Jupyter Notebook → reproducible EDA & model training  

---

## 📂 Project Structure
citysense/
├─ data/
│ ├─ raw/ # raw API pulls (311, weather, holidays)
│ ├─ interim/ # joined/intermediate datasets
│ └─ processed/ # model-ready + Tableau CSVs
├─ notebooks/
│ ├─ 10_eda.ipynb # EDA, baselines, models, exports for Tableau
├─ src/
│ ├─ api_311.py # fetch NYC 311 complaints (daily counts)
│ ├─ weather_api.py # fetch Meteostat daily weather
│ ├─ holiday_calendar.py # build holiday calendar
│ └─ make_features.py # join datasets into model_table
├─ models/ # trained models (.joblib) [gitignored]
├─ requirements.txt # dependencies
└─ README.md
