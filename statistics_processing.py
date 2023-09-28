import pandas as pd

#The uploading data and calculating the averages for the investigation time IoT statistics
time_iot = pd.read_csv('investigation-time-IoT-statistics.csv')
time_iot.columns = time_iot.columns.astype(int)
time_iot = time_iot.reindex(sorted(time_iot.columns), axis=1)
print(time_iot)

time_iot = time_iot.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(time_iot)

column_averages_time_iot = time_iot.mean()
# Format the mean values to display with 2 decimal places
mean_values_time_iot_formatted = column_averages_time_iot.apply(lambda x: '{:.2f}'.format(x))
print(mean_values_time_iot_formatted)

#The uploading data and calculating the averages for the investigation time classic statistics
time_classic = pd.read_csv('investigation-time-Classic-statistics.csv')
time_classic.columns = time_classic.columns.astype(int)
time_classic = time_classic.reindex(sorted(time_classic.columns), axis=1)
print(time_classic)

time_classic = time_classic.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(time_classic)

column_averages_time_classic = time_classic.mean()
# Format the mean values to display with 2 decimal places
mean_values_time_classic_formatted = column_averages_time_classic.apply(lambda x: '{:.2f}'.format(x))
print(mean_values_time_classic_formatted)
# get a summary of the time spent on classic + iot-specific IOCs retreival

