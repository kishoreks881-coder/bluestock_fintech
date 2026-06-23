# Bluestock Fintech — Data Analyst Internship Capstone

**Intern:** kishoreks881  
**Cohort:** 2025 | Fintech Division  
**Program:** Data Analyst Internship

---

## 📁 Project Structure

```
bluestock_fintech/
├── data/
│   ├── raw/              # Raw CSV datasets (10 files)
│   └── processed/        # Cleaned, transformed data
├── notebooks/            # Jupyter EDA notebooks
├── sql/                  # PostgreSQL queries
├── dashboard/            # Visualizations & dashboards
├── reports/              # Data quality summaries & reports
├── data_ingestion.py     # Day 1: Load & inspect all datasets
├── live_nav_fetch.py     # Day 1: Fetch live NAV from mfapi.in
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🚀 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/bluestock_fintech.git
cd bluestock_fintech

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run data ingestion
python data_ingestion.py

# 4. Fetch live NAV data
python live_nav_fetch.py
```

---

## 📊 Day 1 Deliverables

| File | Description |
|------|-------------|
| `data_ingestion.py` | Loads all 10 CSVs, prints shape/dtypes/head, detects anomalies, validates AMFI codes |
| `live_nav_fetch.py` | Fetches live NAV from mfapi.in for 6 key schemes, saves raw CSVs |
| `requirements.txt` | All Python dependencies |
| `reports/day1_data_quality_summary.txt` | Automated data quality report |

---

## 🔑 Key Datasets

| Dataset | Rows | Description |
|---------|------|-------------|
| nav_history | 1000 | NAV history for mutual fund schemes |
| fund_master | 50 | Master list of all AMFI schemes |
| stock_prices | 500 | OHLCV data for key stocks |
| sip_transactions | 200 | SIP investment transactions |
| investor_profile | 50 | Investor demographics & KYC |
| portfolio_holdings | 300 | Current fund holdings per investor |
| redemptions | 100 | Fund redemption records |
| market_index | 1000 | NIFTY 50 daily index data |
| expense_ratio | 50 | Fund expense ratios & exit loads |
| dividends | 100 | Dividend payout history |

---

## 🔗 Data Sources
- Live NAV API: https://api.mfapi.in
- Stock Data: yfinance / NSE India
- Reference: Zerodha Varsity, AMFI India
