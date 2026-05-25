import pandas as pd

INPUT_FILE = "311_SSOT_RAW.csv"
OUTPUT_FILE = "311_SSOT_Cleaned_Final.csv"

df = pd.read_csv(INPUT_FILE, low_memory=False)

# Keep only rows marked VALID in all check columns
filtered = df[
    (df["Created Date Check"] == "VALID") &
    (df["Closed Date Check"] == "VALID") &
    (df["Resolution Time Check"] == "OK") &
    (df["Coordinates Check"] == "VALID") &
    (df["ZIP Check"] == "VALID")
].copy()

filtered.to_csv(OUTPUT_FILE, index=False)

print(f"Original rows: {len(df)}")
print(f"Filtered rows: {len(filtered)}")
print(f"Saved file: {OUTPUT_FILE}")
