import pandas as pd
import glob
import os

print("Current folder:", os.getcwd())

# Get all the CSV files in the folder
files = glob.glob("*.csv")
print("Files found:", files)

# Load and combine as a dataframe
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# If there are duplicates, remove based on Unique Key
df = df.drop_duplicates(subset="Unique Key")

# Save merged file
df.to_csv("311_SSOT.csv", index=False)

print("Merge complete. File saved as 311_SSOT.csv")
