"""
data_ingestion.py
Bluestock Fintech Internship - Day 1
Load, inspect, and validate all 10 CSV datasets
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"
os.makedirs(RAW_PATH, exist_ok=True)
os.makedirs(PROCESSED_PATH, exist_ok=True)


# ─────────────────────────────────────────────
# STEP 1: Generate Sample Datasets
# (Replace this with actual CSV loading when mentor provides datasets)
# ─────────────────────────────────────────────

def generate_sample_datasets():
    """Generate 10 realistic Fintech sample CSV files for Day 1 practice"""
    print("\n📁 Generating sample datasets in data/raw/ ...\n")
    np.random.seed(42)
    dates = pd.date_range("2020-01-01", "2024-12-31", freq="B")

    datasets = {}

    # 1. NAV History
    df1 = pd.DataFrame({
        "date": dates[:1000],
        "scheme_code": np.random.choice([119551, 120503, 118632], 1000),
        "nav": np.round(np.random.uniform(20, 120, 1000), 4)
    })
    datasets["nav_history"] = df1

    # 2. Fund Master
    df2 = pd.DataFrame({
        "scheme_code": range(100001, 100051),
        "scheme_name": [f"Scheme {i}" for i in range(50)],
        "fund_house": np.random.choice(["SBI MF", "ICICI MF", "HDFC MF", "Axis MF", "Nippon MF"], 50),
        "category": np.random.choice(["Equity", "Debt", "Hybrid", "Index"], 50),
        "sub_category": np.random.choice(["Large Cap", "Mid Cap", "Small Cap", "Liquid"], 50),
        "risk_grade": np.random.choice(["Low", "Moderate", "High", "Very High"], 50),
    })
    datasets["fund_master"] = df2

    # 3. Stock Prices (OHLCV)
    df3 = pd.DataFrame({
        "date": dates[:500],
        "symbol": np.random.choice(["RELIANCE", "TCS", "INFY", "HDFCBANK"], 500),
        "open": np.round(np.random.uniform(1000, 3000, 500), 2),
        "high": np.round(np.random.uniform(1100, 3100, 500), 2),
        "low": np.round(np.random.uniform(900, 2900, 500), 2),
        "close": np.round(np.random.uniform(950, 3050, 500), 2),
        "volume": np.random.randint(100000, 5000000, 500),
    })
    datasets["stock_prices"] = df3

    # 4. SIP Transactions
    df4 = pd.DataFrame({
        "transaction_id": range(1, 201),
        "investor_id": np.random.randint(1000, 1050, 200),
        "scheme_code": np.random.choice([119551, 120503, 118632], 200),
        "amount": np.random.choice([500, 1000, 2000, 5000], 200),
        "date": np.random.choice(dates[:500], 200),
        "units_allotted": np.round(np.random.uniform(1, 50, 200), 3),
        "nav_at_purchase": np.round(np.random.uniform(20, 100, 200), 4),
    })
    datasets["sip_transactions"] = df4

    # 5. Investor Profile
    df5 = pd.DataFrame({
        "investor_id": range(1000, 1050),
        "name": [f"Investor_{i}" for i in range(50)],
        "age": np.random.randint(22, 65, 50),
        "city": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"], 50),
        "risk_appetite": np.random.choice(["Low", "Moderate", "High"], 50),
        "kyc_status": np.random.choice(["Verified", "Pending", None], 50),
    })
    datasets["investor_profile"] = df5

    # 6. Portfolio Holdings
    df6 = pd.DataFrame({
        "investor_id": np.random.randint(1000, 1050, 300),
        "scheme_code": np.random.choice([119551, 120503, 118632, 119092, 120841], 300),
        "units_held": np.round(np.random.uniform(10, 500, 300), 3),
        "avg_nav": np.round(np.random.uniform(20, 100, 300), 4),
        "current_nav": np.round(np.random.uniform(25, 130, 300), 4),
    })
    datasets["portfolio_holdings"] = df6

    # 7. Redemptions
    df7 = pd.DataFrame({
        "redemption_id": range(1, 101),
        "investor_id": np.random.randint(1000, 1050, 100),
        "scheme_code": np.random.choice([119551, 120503], 100),
        "units_redeemed": np.round(np.random.uniform(1, 50, 100), 3),
        "nav_at_redemption": np.round(np.random.uniform(30, 120, 100), 4),
        "date": np.random.choice(dates[:500], 100),
    })
    datasets["redemptions"] = df7

    # 8. Market Index (NIFTY 50)
    df8 = pd.DataFrame({
        "date": dates[:1000],
        "index_name": "NIFTY50",
        "open": np.round(np.random.uniform(14000, 22000, 1000), 2),
        "close": np.round(np.random.uniform(14000, 22000, 1000), 2),
        "returns_pct": np.round(np.random.uniform(-3, 3, 1000), 4),
    })
    datasets["market_index"] = df8

    # 9. Expense Ratio
    df9 = pd.DataFrame({
        "scheme_code": range(100001, 100051),
        "expense_ratio": np.round(np.random.uniform(0.1, 2.5, 50), 2),
        "exit_load_pct": np.round(np.random.uniform(0, 1, 50), 2),
        "lock_in_days": np.random.choice([0, 90, 180, 365], 50),
    })
    datasets["expense_ratio"] = df9

    # 10. Dividends
    df10 = pd.DataFrame({
        "scheme_code": np.random.choice([119551, 120503, 118632], 100),
        "dividend_date": np.random.choice(dates[:500], 100),
        "dividend_per_unit": np.round(np.random.uniform(0.5, 5.0, 100), 4),
        "record_nav": np.round(np.random.uniform(20, 100, 100), 4),
    })
    datasets["dividends"] = df10

    # Save all to raw
    for name, df in datasets.items():
        path = f"{RAW_PATH}/{name}.csv"
        df.to_csv(path, index=False)
        print(f"  ✅ Saved: {path}  ({df.shape[0]} rows x {df.shape[1]} cols)")

    return datasets


# ─────────────────────────────────────────────
# STEP 2: Load & Inspect Each Dataset
# ─────────────────────────────────────────────

def load_and_inspect(datasets):
    print("\n" + "="*60)
    print("📊 DATASET INSPECTION REPORT")
    print("="*60)

    anomaly_log = []

    for name, df in datasets.items():
        print(f"\n{'─'*50}")
        print(f"📂 Dataset : {name.upper()}")
        print(f"{'─'*50}")
        print(f"  Shape    : {df.shape}")
        print(f"  Dtypes   :\n{df.dtypes.to_string()}")
        print(f"\n  Head(3)  :\n{df.head(3).to_string()}")

        missing = df.isnull().sum()
        if missing.any():
            print(f"\n  ⚠️  Missing Values:\n{missing[missing > 0].to_string()}")
            anomaly_log.append(f"{name}: {missing[missing > 0].to_dict()}")
        else:
            print(f"\n  ✅ No missing values")

        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"  ⚠️  Duplicate Rows: {duplicates}")
            anomaly_log.append(f"{name}: {duplicates} duplicate rows")
        else:
            print(f"  ✅ No duplicates")

    return anomaly_log


# ─────────────────────────────────────────────
# STEP 3: Validate AMFI Codes
# ─────────────────────────────────────────────

def validate_amfi_codes(datasets):
    print("\n" + "="*60)
    print("🔍 AMFI CODE VALIDATION")
    print("="*60)

    fund_master = datasets.get("fund_master")
    nav_history = datasets.get("nav_history")

    if fund_master is None or nav_history is None:
        print("  ⚠️  fund_master or nav_history not loaded.")
        return

    master_codes = set(fund_master["scheme_code"].astype(str))
    nav_codes = set(nav_history["scheme_code"].astype(str))

    missing_in_nav = master_codes - nav_codes
    extra_in_nav = nav_codes - master_codes

    print(f"  Fund Master Schemes : {len(master_codes)}")
    print(f"  NAV History Schemes : {len(nav_codes)}")
    print(f"  Codes in master but NOT in nav_history: {len(missing_in_nav)}")
    print(f"  Codes in nav_history but NOT in master : {len(extra_in_nav)}")

    if not missing_in_nav:
        print("  ✅ All AMFI codes validated — every master code exists in NAV history")
    else:
        print(f"  ⚠️  Missing codes (sample): {list(missing_in_nav)[:5]}")

    print("\n  📋 Fund Master — Unique Categories:")
    if "fund_house" in fund_master.columns:
        print("    Fund Houses     :", fund_master["fund_house"].unique().tolist())
    if "category" in fund_master.columns:
        print("    Categories      :", fund_master["category"].unique().tolist())
    if "sub_category" in fund_master.columns:
        print("    Sub-Categories  :", fund_master["sub_category"].unique().tolist())
    if "risk_grade" in fund_master.columns:
        print("    Risk Grades     :", fund_master["risk_grade"].unique().tolist())


# ─────────────────────────────────────────────
# STEP 4: Save Summary Report
# ─────────────────────────────────────────────

def save_summary(datasets, anomaly_log):
    lines = ["DATA QUALITY SUMMARY — Day 1\n", "="*50 + "\n"]
    for name, df in datasets.items():
        lines.append(f"\nDataset: {name}")
        lines.append(f"  Rows       : {df.shape[0]}")
        lines.append(f"  Columns    : {df.shape[1]}")
        lines.append(f"  Columns    : {list(df.columns)}")
        missing = df.isnull().sum().sum()
        lines.append(f"  Missing Val: {missing}")
        lines.append(f"  Duplicates : {df.duplicated().sum()}")

    lines.append("\n\nANOMALIES DETECTED:")
    if anomaly_log:
        for a in anomaly_log:
            lines.append(f"  - {a}")
    else:
        lines.append("  None detected")

    report_path = "reports/day1_data_quality_summary.txt"
    os.makedirs("reports", exist_ok=True)
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    print(f"\n📄 Summary saved to: {report_path}")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  BLUESTOCK FINTECH — DATA INGESTION (DAY 1)")
    print("=" * 60)

    # Step 1: Generate/Load datasets
    datasets = generate_sample_datasets()

    # Step 2: Inspect
    anomaly_log = load_and_inspect(datasets)

    # Step 3: Validate AMFI codes
    validate_amfi_codes(datasets)

    # Step 4: Save report
    save_summary(datasets, anomaly_log)

    print("\n✅ Day 1 Data Ingestion Complete!")
    print("📁 Files in data/raw/ :")
    for f in sorted(os.listdir(RAW_PATH)):
        print(f"   {f}")
