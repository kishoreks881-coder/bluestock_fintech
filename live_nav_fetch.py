"""
live_nav_fetch.py
Bluestock Fintech Internship - Day 1
Fetches live NAV data from mfapi.in for key mutual fund schemes
"""

import requests
import pandas as pd
import json
import os
from datetime import datetime

# Output path
RAW_PATH = "data/raw"
os.makedirs(RAW_PATH, exist_ok=True)

# 5 Key Schemes to fetch
SCHEMES = {
    "SBI_Bluechip":        119551,
    "ICICI_Bluechip":      120503,
    "Nippon_Large_Cap":    118632,
    "Axis_Bluechip":       119092,
    "Kotak_Bluechip":      120841,
    "HDFC_Top100_Direct":  125497,  # bonus from task
}

BASE_URL = "https://api.mfapi.in/mf"

def fetch_nav(scheme_name, scheme_code):
    """Fetch NAV history for a given scheme and save as CSV"""
    url = f"{BASE_URL}/{scheme_code}"
    print(f"\n📥 Fetching: {scheme_name} (Code: {scheme_code})")
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        meta = data.get("meta", {})
        nav_records = data.get("data", [])

        print(f"   Fund House : {meta.get('fund_house', 'N/A')}")
        print(f"   Scheme Name: {meta.get('scheme_name', 'N/A')}")
        print(f"   Category   : {meta.get('scheme_category', 'N/A')}")
        print(f"   Total NAV Records: {len(nav_records)}")

        # Convert to DataFrame
        df = pd.DataFrame(nav_records)
        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")
        df["scheme_code"] = scheme_code
        df["scheme_name"] = meta.get("scheme_name", scheme_name)
        df["fund_house"] = meta.get("fund_house", "N/A")
        df["category"] = meta.get("scheme_category", "N/A")

        # Sort by date ascending
        df = df.sort_values("date").reset_index(drop=True)

        # Save raw CSV
        filename = f"{RAW_PATH}/{scheme_name}_nav.csv"
        df.to_csv(filename, index=False)
        print(f"   ✅ Saved to: {filename}")
        print(f"   Latest NAV : {df.iloc[-1]['nav']} on {df.iloc[-1]['date'].date()}")

        return df

    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection Error — Check internet or API availability")
    except requests.exceptions.Timeout:
        print(f"   ❌ Timeout — API took too long")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    return None


def fetch_fund_master():
    """Fetch full fund master list from mfapi"""
    print("\n📋 Fetching Fund Master List...")
    url = "https://api.mfapi.in/mf"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        master = response.json()
        df = pd.DataFrame(master)
        df.columns = ["scheme_code", "scheme_name"]
        df.to_csv(f"{RAW_PATH}/fund_master.csv", index=False)
        print(f"   ✅ Fund Master saved — Total Schemes: {len(df)}")
        print(df.head())
        return df
    except Exception as e:
        print(f"   ❌ Error fetching fund master: {e}")
        return None


def data_quality_summary(all_dfs):
    """Print data quality summary for all fetched data"""
    print("\n" + "="*60)
    print("📊 DATA QUALITY SUMMARY")
    print("="*60)
    for name, df in all_dfs.items():
        if df is not None:
            missing = df.isnull().sum().sum()
            print(f"\n{name}:")
            print(f"  Shape       : {df.shape}")
            print(f"  Date Range  : {df['date'].min().date()} → {df['date'].max().date()}")
            print(f"  NAV Range   : {df['nav'].min():.2f} → {df['nav'].max():.2f}")
            print(f"  Missing Val : {missing}")
            print(f"  Dtypes      : date={df['date'].dtype}, nav={df['nav'].dtype}")


if __name__ == "__main__":
    print("=" * 60)
    print("  BLUESTOCK FINTECH — LIVE NAV FETCH")
    print(f"  Run Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 1. Fetch Fund Master
    fetch_fund_master()

    # 2. Fetch NAV for all 6 key schemes
    all_dfs = {}
    for name, code in SCHEMES.items():
        df = fetch_nav(name, code)
        all_dfs[name] = df

    # 3. Data Quality Summary
    fetched = {k: v for k, v in all_dfs.items() if v is not None}
    if fetched:
        data_quality_summary(fetched)

    print("\n✅ Day 1 - Live NAV Fetch Complete!")
    print("📁 Check data/raw/ folder for all CSV files")
