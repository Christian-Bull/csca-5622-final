import pandas as pd

# Read the CSV file
bikeshare_data = pd.read_csv("data/london_merged_hour.csv")

bikeshare_data['timestamp'] = pd.to_datetime(bikeshare_data['timestamp'])

# Set the date (without time) as a new column
bikeshare_data['date'] = bikeshare_data['timestamp'].dt.date

# Aggregate the data by day
daily_bikeshare_data = bikeshare_data.groupby('date').agg({
    'cnt': 'sum',
    't1': 'mean',
    't2': 'mean',
    'hum': 'mean',
    'wind_speed': 'mean',
    'weather_code': lambda x: x.mode()[0] if not x.mode().empty else x.iloc[0],
    'is_holiday': 'max',
    'is_weekend': 'max',
    'season': 'max'
}).reset_index()

