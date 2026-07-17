SYSTEM_NAME = "Casino AI Decision System"
VERSION = "0.1"

print("=" * 50)
print(SYSTEM_NAME)
print(f"Version {VERSION}")
print("=" * 50)

print()
print("System Status")
print()

print("[OK] Python Environment Ready")
print("[OK] Git Repository Ready")
print("[OK] Project Structure Ready")

print()
print("Next Step:")
print("Load Excel Data")
print()

print("=" * 50)

import pandas as pd

print()
print("=" * 50)
print("Reading Excel File...")
print("=" * 50)

excel_path = "data/raw/数据表1.xlsx"

df = pd.read_excel(excel_path)

print("Read Successfully!")
print()

print(df)
print()

print("Rows :", len(df))
print("Columns :", len(df.columns))
print()

print("Column List")

print(df.columns)

print()

print("Preview")

print(df.head())
print()
print("Data Types")
print("-" * 30)

print(df.dtypes)
print()
print("Missing Values")
print("-" * 30)

print(df.isnull().sum())