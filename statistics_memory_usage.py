import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#The uploading data and calculating the averages for the memory usage IoT statistics
memory_iot = pd.read_csv('memory-usage-IoT-statistics.csv')
memory_iot.columns = memory_iot.columns.astype(int)
memory_iot = memory_iot.reindex(sorted(memory_iot.columns), axis=1)
memory_iot = memory_iot.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(memory_iot)

column_averages_memory_iot = memory_iot.mean()
# Format the mean values to display with 2 decimal places
column_averages_memory_iot = column_averages_memory_iot.apply(lambda x: '{:.2f}'.format(x))
# Convert the Series to float data type
column_averages_memory_iot = column_averages_memory_iot.astype(float)
print(column_averages_memory_iot)

#The uploading data and calculating the averages for the memory usage classic statistics
memory_classic = pd.read_csv('memory-usage-Classic-statistics.csv')
memory_classic.columns = memory_classic.columns.astype(int)
memory_classic = memory_classic.reindex(sorted(memory_classic.columns), axis=1)
memory_classic = memory_classic.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(memory_classic)
column_averages_memory_classic = memory_classic.mean()
# Format the mean values to display with 2 decimal places
column_averages_memory_classic = column_averages_memory_classic.apply(lambda x: '{:.2f}'.format(x))
# Convert the Series to float data type
column_averages_memory_classic = column_averages_memory_classic.astype(float)
print(column_averages_memory_classic)

#The uploading data and calculating the averages for the memory usage both statistics
memory_both = pd.read_csv('memory-usage-Both-statistics.csv')
memory_both.columns = memory_both.columns.astype(int)
memory_both = memory_both.reindex(sorted(memory_both.columns), axis=1)
memory_both = memory_both.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(memory_both)
column_averages_memory_both = memory_both.mean()
# Format the mean values to display with 2 decimal places
column_averages_memory_both = column_averages_memory_both.apply(lambda x: '{:.2f}'.format(x))
# Convert the Series to float data type
column_averages_memory_both = column_averages_memory_both.astype(float)
print(column_averages_memory_both)

# # get a summary of the time spent on classic + iot-specific IOCs retreival
# summary = mean_values_time_classic_float + mean_values_time_iot_float
# print(summary)
x_array_memory = column_averages_memory_both.index.to_numpy()
print(x_array_memory, len(x_array_memory))
y_memory_both = column_averages_memory_both.to_numpy()
print(y_memory_both)
# # Window size for the moving average (adjust as needed)
# window_size = 2
# # Calculate the moving average
# smoothed_memory_overhead_both = np.convolve(y_memory_both, np.ones(window_size)/window_size, mode='same')

y_memory_iot_ioc = column_averages_memory_iot.to_numpy()
print(y_memory_iot_ioc)
y_memory_classic_ioc = column_averages_memory_classic.to_numpy()
print(y_memory_classic_ioc)
# Create a new array by selecting values at every 3rd position
new_memory_both = y_memory_both[::10]
new_memory_iot_ioc = y_memory_iot_ioc[::10]
new_memory_classic_ioc = y_memory_classic_ioc[::10]
new_x_array = x_array_memory[::10]

#plotting section with settings
# plt.plot(x_array_memory, y_memory_iot_ioc, 'o-b', ms=3, label = 'IoT-specific IoCs extraction memory usage')
# plt.plot(x_array_memory, y_memory_classic_ioc, 'o-y', ms=3, label = 'Traditional IoCs extraction memory usage')
# plt.plot(x_array_memory, y_memory_both, 'o-r', ms=3, label = 'Total IoCs memory usage')

plt.plot(new_x_array, new_memory_iot_ioc, 'o-b', ms=3, label = 'IoT-specific IoCs extraction memory usage')
plt.plot(new_x_array, new_memory_classic_ioc, 'o-y', ms=3, label = 'Traditional IoCs extraction memory usage')
plt.plot(new_x_array, new_memory_both, 'o-r', ms=3, label = 'Total IoCs memory usage')
# plt.plot(x_array_memory, smoothed_memory_overhead_both, 'o-r', ms=3, label = 'Total IoCs memory usage', linestyle = 'dotted')

# Define custom x-axis ticks with step size
x_custom_ticks = np.arange(3, 420, 25)  # Start at 1, end at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(80, 150, 10)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=7)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)
plt.title("Memory Overhead")
plt.xlabel("Number of extracted IoCs")
plt.ylabel("Memory Usage, MiB")
# Add a legend with custom labels
# plt.subplots_adjust(top=0.5)  # Adjust the top margin (0.9 means 10% crop from the top)
plt.legend()
plt.show()