import pandas as pd
import os

from data import DataProvider, DataManager, DataFormatter

# Path the Apple health data 'Export.xml' file.
health_path = os.path.abspath(
    __file__ + f"/../apple_health_export/Export.xml")

# Create rows and columns from XML.
rows, columns = DataProvider.rows_and_columns_xml(health_path)

# Create dataframe from rows and columns
df = pd.DataFrame(rows, columns=columns)

# Create grouped dataframes
hr = DataManager.grouped_by_date_df(
    df, 'HKQuantityTypeIdentifierHeartRate', 'heartRate(BPM)', 'mean')

wd = DataManager.grouped_by_date_df(
    df, 'HKQuantityTypeIdentifierDistanceWalkingRunning', 'walkingRunningDistance(km)', 'sum')

aeb = DataManager.grouped_by_date_df(
    df, 'HKQuantityTypeIdentifierActiveEnergyBurned', 'activeEnergyBurned(kal)', 'sum')

sc = DataManager.grouped_by_date_df(
    df, 'HKQuantityTypeIdentifierStepCount', 'stepCount', 'sum')

st = DataManager.grouped_by_date_df(
    df, 'HKQuantityTypeIdentifierAppleStandTime', 'standTime(min)', 'sum')

# Format different columns in different dataframes
wd['walkingRunningDistance(m)'] = wd['walkingRunningDistance(km)'] * 1000.0

# Merge dataframes together
merged_df = DataManager.merge([hr, wd, aeb, sc, st])
merged_df = merged_df.reset_index()

# Format date
merged_df = DataFormatter.format_time_df(merged_df)

# Handle NaN values
merged_df = DataManager.handle_nan(merged_df)

# Get an overview
merged_df = merged_df[['date', 'startTime', 'weekday',
                       'heartRate(BPM)', 'standTime(min)', 'stepCount', 'activeEnergyBurned(kal)', 'walkingRunningDistance(m)', 'walkingRunningDistance(km)']]
print('Overview:')
print(merged_df.shape)
print(merged_df.head())
