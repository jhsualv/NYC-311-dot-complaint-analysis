import pandas as pd

# Change this to your actual cleaned CSV filename
input_file = "311_SSOT_Cleaned_Final.csv"
output_file = "311_SSOT_Cleaned_Final_v2.csv"

# Load the CSV
df = pd.read_csv(input_file)

# Convert date columns to datetime
df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
df["Closed Date"] = pd.to_datetime(df["Closed Date"], errors="coerce")

# Create resolution time columns
time_diff = df["Closed Date"] - df["Created Date"]
df["Resolution Time (Days)"] = time_diff.dt.total_seconds() / 86400
df["Resolution Time (Hours)"] = time_diff.dt.total_seconds() / 3600

# Remove rows with invalid or negative resolution times
df = df.dropna(subset=["Resolution Time (Days)", "Resolution Time (Hours)"])
df = df[df["Resolution Time (Days)"] >= 0]

# Save updated CSV
df.to_csv(output_file, index=False)

print(f"Done. Saved updated file as: {output_file}")
print(df[["Created Date", "Closed Date", "Resolution Time (Days)", "Resolution Time (Hours)"]].head())
