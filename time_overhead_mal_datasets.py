import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_array_datasets = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', ]
y_array_time = [8.78, 12.42, 9.03, 23.18, 12.58, 10.5, 14.02, 12.85, 19.1, 40.5, 7.08]                   #in minutes
x_array_datasets_2 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
y_array_time_to_find = [13.32, 2.87, 15.47, 3.14, 3.99, 4.37, 8.89, 13.43, 36.70, 12.42]

#plotting section with settings
# plt.plot(x_array_datasets, y_array_time, 'o-b', ms=3, label = 'Visual and machine-readable output storage usage')
plt.bar(x_array_datasets_2, y_array_time_to_find, label='Value 1', color='c', width = 0.8)

# Define custom x-axis ticks with step size
# x_custom_ticks = np.arange(2, 36, 2)  # Start at 1, end at 10, step by 2
# x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(0, 50, 5)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
# plt.xticks(x_custom_ticks, x_custom_labels, fontsize=8)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

plt.title("IOCs extraction time for 10 different attack datasets")
plt.xlabel("Attack Datasets")
plt.ylabel("IoCs extraction time (Seconds)")
plt.tight_layout()
# plt.legend()
plt.show()