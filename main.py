import pandas as pd

# Read the CSV file
bikeshare_data = pd.read_csv("data/london_merged_hour.csv")

# View the first 5 rows
print(bikeshare_data.head(20))