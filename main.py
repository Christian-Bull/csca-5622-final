import numpy as np
import scipy as sp
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Set color map to have light blue background
sns.set()
import statsmodels.formula.api as smf
import statsmodels.api as sm

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

print(bikeshare_data.head(10))

test_data = daily_bikeshare_data[:100]

best_guess_predictor = {}

predictors = test_data.columns.tolist()

print(predictors)
for predictor in predictors:
    model = smf.ols(formula=f'cnt ~ {predictor}', data=test_data)
    results = model.fit()
    best_guess_predictor[predictor] = results.rsquared

best_guess_pred_sorted = {k: v for k, v in sorted(best_guess_predictor.items(), key=lambda item: item[1])}

print(best_guess_pred_sorted)

print(test_data.head())