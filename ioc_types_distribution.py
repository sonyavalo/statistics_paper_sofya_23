import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#The uploading data and calculating the averages for the pdf size IoT statistics
types_of_iot_iocs = pd.read_csv('iot-ioc-types-statistics.csv')
types_of_iot_iocs.columns = types_of_iot_iocs.columns.astype(int)
types_of_iot_iocs = types_of_iot_iocs.reindex(sorted(types_of_iot_iocs.columns), axis=1)
types_of_iot_iocs = types_of_iot_iocs.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
# Convert all values in the DataFrame to integers
types_of_iot_iocs = types_of_iot_iocs.fillna(0).astype(int)
print(types_of_iot_iocs)

# Access every fifth row (0-based index) and create a new DataFrame
simulator_command = types_of_iot_iocs.iloc[::6].reset_index(drop=True)
print(simulator_command, 'simulator command')
simulator_command_mean = simulator_command.mean()
simulator_command_mean = round(simulator_command_mean)
print(simulator_command_mean, 'simulator command')
app_command = types_of_iot_iocs.iloc[1::6].reset_index(drop=True)
print(app_command, 'app command')
app_command_mean = app_command.mean()
app_command_mean = round(app_command_mean)
print(app_command_mean, 'app command')
app_subscribtion = types_of_iot_iocs.iloc[2::6].reset_index(drop=True)
print(app_subscribtion, 'app subscribtion')
app_subscribtion_mean = app_subscribtion.mean()
app_subscribtion_mean = round(app_subscribtion_mean)
print(app_subscribtion_mean, 'app subscribtion')
device_event = types_of_iot_iocs.iloc[3::6].reset_index(drop=True)
print(device_event, 'device event')
device_event_mean = device_event.mean()
device_event_mean = round(device_event_mean)
print(device_event_mean, 'device event')
mode_event = types_of_iot_iocs.iloc[4::6].reset_index(drop=True)
print(mode_event, 'mode event')
mode_event_mean = mode_event.mean()
mode_event_mean = round(mode_event_mean)
print(mode_event_mean, 'mode event')
command_event = types_of_iot_iocs.iloc[5::6].reset_index(drop=True)
print(command_event, 'command event')
command_event_mean = command_event.mean()
command_event_mean = round(command_event_mean)
print(command_event_mean, 'command event')

x_array_num_nodes = command_event_mean.index.to_numpy()
print(x_array_num_nodes)
y_simulator_command = simulator_command_mean.to_numpy()
y_app_command = app_command_mean.to_numpy()
y_app_subscribtion = app_subscribtion_mean.to_numpy()
y_device_event = device_event_mean.to_numpy()
y_mode_event = mode_event_mean.to_numpy()
y_command_event = command_event_mean.to_numpy()

# Set the width of each bar
bar_width = 1
delta = 3
# Create the clustered columns
# plt.bar(x_array_num_nodes - delta*3/6, y_simulator_command, bar_width, label='Value 1', color='b', align='center')
# plt.bar(x_array_num_nodes - delta*2/6, y_app_command, bar_width, label='Value 2', color='g', align='center')
# plt.bar(x_array_num_nodes - delta*1/6, y_app_subscribtion, bar_width, label='Value 2', color='r', align='center')
# plt.bar(x_array_num_nodes + delta*3/6, y_device_event, bar_width, label='Value 2', color='c', align='center')
# plt.bar(x_array_num_nodes + delta*2/6, y_mode_event, bar_width, label='Value 2', color='m', align='center')
# plt.bar(x_array_num_nodes + delta*1/6, y_command_event, bar_width, label='Value 2', color='y', align='center')

# plt.plot(x_array_num_nodes, y_simulator_command, 'o-b', ms=3)
plt.scatter(x_array_num_nodes, y_simulator_command, marker='o', color='b', s=5, label = 'User command IoCs')
plt.scatter(x_array_num_nodes, y_app_command, marker='o', color='r', s=5, label = 'Application command IoCs')
plt.scatter(x_array_num_nodes, y_app_subscribtion, marker='o', color='y', s=5, label = 'Application subscription IoCs')
plt.scatter(x_array_num_nodes, y_device_event, marker='o', color='m', s=5, label = 'Device event IoCs')
plt.scatter(x_array_num_nodes, y_mode_event, marker='o', color='k', s=5, label = 'Mode event IoCs')
# plt.scatter(x_array_num_nodes, y_command_event, marker='o', color='c', s=5)
# plt.plot(x_array_num_nodes, y_app_command, 'o-r', ms=3)
# plt.plot(x_array_num_nodes, y_app_subscribtion, 'o-y', ms=3)
# plt.plot(x_array_num_nodes, y_device_event, 'o-m', ms=3)
# plt.plot(x_array_num_nodes, y_mode_event, 'o-k', ms=3)
# plt.plot(x_array_num_nodes, y_command_event, 'o-c', ms=3)

# Define custom x-axis ticks with step size
x_custom_ticks = np.arange(3, 420, 20)  # Start at 1, end at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(0, 70, 5)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=8)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

# Show the plot
plt.title("IoT-specific IoCs types distribution")
plt.xlabel("Number of extracted IoCs")
plt.ylabel("Number of IoCs of a particular type")
plt.tight_layout()
plt.legend()
plt.show()
# # Access the first row of the DataFrame
# first_row = types_of_iot_iocs.iloc[0]
# print(first_row)
# for column in types_of_iot_iocs.columns:
#     column_data = df[column]