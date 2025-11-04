#  Bank Transactions ETL Pipeline (Python + Power BI Style)

This project demonstrates a **complete ETL (Extract, Transform, Load)** pipeline built with Python, using a **synthetic bank transactions dataset**.  
The final output includes **Power BI–style dashboard visuals** generated using Matplotlib — making this project portfolio-ready for **Data Engineering** or **Data Analytics** roles.

---

##  Project Overview

The goal of this project is to:
-  Extract and clean raw transaction data
-  Transform data to calculate inflows, outflows, and net cash flow
-  Aggregate metrics by month, region, and merchant
-  Generate **professional-looking dashboards** ready for GitHub or resume

---

##  Tech Stack

- **Python 3**
- **Pandas / NumPy** – Data processing  
- **Matplotlib** – Power BI–style dashboards  
- **Jupyter Notebook / VS Code** – Development environment

---

##  Project Structure

bank_etl_project/
├── data/
│ ├── bank_transactions_raw.csv # Raw data
│ └── processed/ # Processed output data
│ ├── transactions_clean.csv
│ ├── monthly_summary.csv
│ ├── regional_summary.csv
│ └── top_merchants.csv
│
├── dashboards/ # Final charts
│ ├── monthly_trends.png
│ ├── regional_flows.png
│ └── top_merchants.png
│
├── scripts/
│ └── etl_pipeline.py # Main ETL script
│
├── bank_etl_pipeline.ipynb # Jupyter Notebook version
└── requirements.txt


---

##  How to Run the Project

###  Option 1: Command Line
```bash
cd bank_etl_project
pip install -r requirements.txt
python scripts/etl_pipeline.py

Option 2: Jupyter Notebook
jupyter notebook
# Open and run bank_etl_pipeline.ipynb

---

Outputs will be generated in:

data/processed/ → cleaned CSV files

dashboards/ → Power BI–style PNG charts

---

Dashboards Preview
1. Monthly Net Cash Flow

2. Net Flow by Region

3. Top 10 Merchants by Spend

---

Key Learnings

Built an end-to-end ETL pipeline in Python

Practiced data aggregation and transformation for financial data

Designed Power BI–style dashboards without external BI tools

Created a clean, portfolio-ready project structure suitable for GitHub

---

Future Enhancements

Add interactive dashboards with Power BI or Tableau

Deploy the pipeline with Airflow or Prefect

Automate daily/weekly refresh using scheduling



