import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "bank_transactions_raw.csv"
PROCESSED_DIR = BASE / "data" / "processed"
DASH_DIR = BASE / "dashboards"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DASH_DIR.mkdir(parents=True, exist_ok=True)

def extract():
    df = pd.read_csv(RAW, parse_dates=["date"])
    return df

def transform(df: pd.DataFrame):
    df = df.copy()
    df["merchant"] = df["merchant"].fillna("—")
    df["txn_type"] = df["txn_type"].str.title()
    df["year_month"] = df["date"].dt.to_period("M").astype(str)
    df["inflow"] = np.where(df["amount"]>0, df["amount"], 0.0)
    df["outflow"] = np.where(df["amount"]<0, -df["amount"], 0.0)
    df["net"] = df["amount"]
    monthly = (df.groupby("year_month", as_index=False)
                 .agg(total_inflow=("inflow","sum"),
                      total_outflow=("outflow","sum"),
                      net_flow=("net","sum"),
                      txn_count=("transaction_id","count")))
    regional = (df.groupby("region", as_index=False)
                  .agg(total_inflow=("inflow","sum"),
                       total_outflow=("outflow","sum"),
                       net_flow=("net","sum"),
                       txn_count=("transaction_id","count"))
                  .sort_values("net_flow", ascending=False))
    top_merchants = (df[df["merchant"]!="—"]
                       .groupby("merchant", as_index=False)
                       .agg(spend=("outflow","sum"), txns=("transaction_id","count"))
                       .sort_values("spend", ascending=False)
                       .head(10))
    return df, monthly, regional, top_merchants

def load(df, monthly, regional, top_merchants):
    df.to_csv(PROCESSED_DIR / "transactions_clean.csv", index=False)
    monthly.to_csv(PROCESSED_DIR / "monthly_summary.csv", index=False)
    regional.to_csv(PROCESSED_DIR / "regional_summary.csv", index=False)
    top_merchants.to_csv(PROCESSED_DIR / "top_merchants.csv", index=False)

def visualize(monthly, regional, top_merchants):
    plt.figure(figsize=(10,4))
    plt.plot(monthly["year_month"], monthly["net_flow"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Monthly Net Cash Flow")
    plt.ylabel("Net Flow")
    plt.tight_layout()
    plt.savefig(DASH_DIR / "monthly_trends.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7,4))
    plt.bar(regional["region"], regional["net_flow"])
    plt.title("Net Cash Flow by Region")
    plt.ylabel("Net Flow")
    plt.tight_layout()
    plt.savefig(DASH_DIR / "regional_flows.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8,5))
    plt.barh(top_merchants["merchant"], top_merchants["spend"])
    plt.gca().invert_yaxis()
    plt.xlabel("Spend")
    plt.title("Top 10 Merchants by Spend")
    plt.tight_layout()
    plt.savefig(DASH_DIR / "top_merchants.png", dpi=150)
    plt.close()

def main():
    df = extract()
    df_clean, monthly, regional, top_merchants = transform(df)
    load(df_clean, monthly, regional, top_merchants)
    visualize(monthly, regional, top_merchants)
    print("ETL complete. Outputs saved in data/processed and dashboards/.")

if __name__ == "__main__":
    main()
