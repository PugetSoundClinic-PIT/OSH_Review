import pandas as pd
import os
from glob import glob

def read_csv_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Remove any leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Convert column names to lowercase for consistency
    df.columns = df.columns.str.lower()
    
    return df

# Specify the directory containing your CSV files
directory = "Desktop/data/max"

# Get a list of all CSV files in the directory
csv_files = glob(os.path.join(directory, "*.csv"))

# Read and process all CSV files
dataframes = [read_csv_file(file) for file in csv_files]

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Remove any duplicate rows
combined_df = combined_df.drop_duplicates()

# Sort the DataFrame by a specific column if needed
# For example, sort by the 'cites' column in descending order
combined_df = combined_df.sort_values(by='cites', ascending=False)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("combined_output.csv", index=False)

print(f"Combined {len(csv_files)} CSV files into 'combined_output.csv'")
print(f"Total rows in combined DataFrame: {len(combined_df)}")