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
y_summary_time = [round(x / 1000, 2) for x in y_summary_time]
print(y_summary_time)

upward_trend_values_summary = []
counter_summary = []
previous_biggest = y_summary_time[0]
upward_trend_values_summary.insert(0, y_summary_time[0])
counter_summary.append(0)
# Start from the second element (index 1) and compare with the previous element
for index, time in enumerate(y_summary_time):
    if time > previous_biggest:
        upward_trend_values_summary.append(time)
        previous_biggest = time
        counter_summary.append(index)
print(counter_summary, len(counter_summary))
print(upward_trend_values_summary, len(upward_trend_values_summary))

y_iot_ioc_time = mean_values_time_iot_float.to_numpy()
y_iot_ioc_time = [round(x / 1000, 2) for x in y_iot_ioc_time]
print(y_iot_ioc_time)
#script for the upward trend of time
# Initialize a list to store the upward trend values
upward_trend_values_iot = []
for i in counter_summary:
    upward_trend_values_iot.append(y_iot_ioc_time[i])
print(upward_trend_values_iot, len(upward_trend_values_iot))
# Initialize a list to store the upward trend values
# upward_trend_values_iot = []
# counter = []
# previous_biggest = y_iot_ioc_time[0]
# upward_trend_values_iot.insert(0, y_iot_ioc_time[0])
# counter.append(0)
# # Start from the second element (index 1) and compare with the previous element
# for index, time in enumerate(y_iot_ioc_time):
#     if time > previous_biggest:
#         upward_trend_values_iot.append(time)
#         previous_biggest = time
#         counter.append(index)
# for i in range(1, len(y_iot_ioc_time)):
#     if y_iot_ioc_time[i] > y_iot_ioc_time[i - 1]:
#         upward_trend_values_iot.append(y_iot_ioc_time[i])
#         counter.append(i)
# # Include the first value as it has no previous value for comparison
# upward_trend_values_iot.insert(0, y_iot_ioc_time[0])
# counter.append(0)
# print(counter, len(counter))
# print(upward_trend_values_iot, len(upward_trend_values_iot))

y_classic_ioc_time = mean_values_time_classic_float.to_numpy()
y_classic_ioc_time = [round(x / 1000, 2) for x in y_classic_ioc_time]
print(y_classic_ioc_time)

upward_trend_values_classic = []
for i in counter_summary:
    upward_trend_values_classic.append(y_classic_ioc_time[i])
print(upward_trend_values_classic, len(upward_trend_values_classic))

# upward_trend_values_classic = []
# for i in counter:
#     upward_trend_values_classic.append(y_classic_ioc_time[i])
# print(upward_trend_values_classic, len(upward_trend_values_classic))

# upward_trend_values_classic = []
# counter_classic = []
# previous_biggest = y_classic_ioc_time[0]
# upward_trend_values_classic.insert(0, y_classic_ioc_time[0])
# counter_classic.append(0)
# # Start from the second element (index 1) and compare with the previous element
# for index, time in enumerate(y_classic_ioc_time):
#     if time > previous_biggest:
#         upward_trend_values_classic.append(time)
#         previous_biggest = time
#         counter_classic.append(index)
# print(counter_classic, len(counter_classic))
# print(upward_trend_values_classic, len(upward_trend_values_classic))
upward_trend_x_array =[]
for i in counter_summary:
    upward_trend_x_array.append(x_array_time[i])
print(upward_trend_x_array, len(upward_trend_x_array))
# Create a new array by selecting values at every 3rd position
new_x_array = upward_trend_x_array[::3]
new_time_values_iot = upward_trend_values_iot[::3]
new_time_values_classic = upward_trend_values_classic[::3]
new_time_values_summary = upward_trend_values_summary[::3]

# #plotting section with settings
# plt.plot(upward_trend_x_array, upward_trend_values_iot, 'o-b', ms=3, label = 'IoT-specific IoCs extraction time')
# plt.plot(upward_trend_x_array, upward_trend_values_classic, 'o-y', ms=3, label = 'Traditional IoCs extraction time')
# plt.plot(upward_trend_x_array, upward_trend_values_summary, 'o-r', ms=3, label = 'Total IoCs extraction time')

#plotting section with settings
plt.plot(new_x_array, new_time_values_iot, 'o-b', ms=3, label = 'IoT-specific IoCs extraction time')
plt.plot(new_x_array, new_time_values_classic, 'o-y', ms=3, label = 'Traditional IoCs extraction time')
plt.plot(new_x_array, new_time_values_summary, 'o-r', ms=3, label = 'Total IoCs extraction time')

# # Define custom x-axis ticks with step size
x_custom_ticks = np.arange(3, 420, 25)  # Start at 1, end
# # x_custom_ticks = new_x_array  # Start at 1, end at 10, step by 2 at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(0, 35, 5)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=7)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

plt.title("Time Overhead")
plt.xlabel("Number of extracted IoCs")
plt.ylabel("Time spent to extract IoCs, sec")
# Add a legend with custom labels
plt.legend(loc='upper left')
# Crop the figure from the top (adjust top margin)
# plt.subplots_adjust(top=0.7)  # Adjust the top margin (0.9 means 10% crop from the top)

plt.show()

# for sum in range(1 , summary):
#     print(summary[sum])


