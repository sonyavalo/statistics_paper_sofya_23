import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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
# Convert the Series to float data type
mean_values_time_iot_float = mean_values_time_iot_formatted.astype(float)
print(mean_values_time_iot_float)

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
# Convert the Series to float data type
mean_values_time_classic_float = mean_values_time_classic_formatted.astype(float)
print(mean_values_time_classic_float)
# get a summary of the time spent on classic + iot-specific IOCs retreival
summary = mean_values_time_classic_float + mean_values_time_iot_float
print(summary)
x_array_time = summary.index.to_numpy()
print(x_array_time)
y_summary_time = summary.to_numpy()
print(y_summary_time)
y_iot_ioc_time = mean_values_time_iot_float.to_numpy()
print(y_iot_ioc_time)
y_classic_ioc_time = mean_values_time_classic_float.to_numpy()
print(y_classic_ioc_time)

#plotting section with settings
plt.plot(x_array_time, y_iot_ioc_time, 'o-b', ms=3)
plt.plot(x_array_time, y_classic_ioc_time, 'o-y', ms=3)
plt.plot(x_array_time, y_summary_time, 'o-r', ms=3)
plt.title("Time Overhead")
plt.xlabel("Number of IoCs")
plt.ylabel("Time spent to extract IoCs, ms")

plt.show()

# for sum in range(1 , summary):
#     print(summary[sum])


