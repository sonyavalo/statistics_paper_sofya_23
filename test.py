# import matplotlib.pyplot as plt
# import numpy as np
#
# # Sample data for clustered columns
# categories = ['Category A', 'Category B', 'Category C']
# values1 = [15, 25, 30]
# values2 = [10, 20, 25]
#
# # Create an array for the x-axis positions
# x = np.arange(len(categories))
#
# # Set the width of each bar
# bar_width = 0.35
#
# # Create the clustered columns
# plt.bar(x - bar_width/2, values1, bar_width, label='Value 1', color='b', align='center')
# plt.bar(x + bar_width/2, values2, bar_width, label='Value 2', color='g', align='center')
#
# # Add labels and legend
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Clustered Column Bar Chart')
# plt.xticks(x, categories)
# plt.legend()
#
# # Show the plot
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
memory_overhead = [100, 105, 98, 110, 115, 112, 120, 130, 128, 132]

# Window size for the moving average (adjust as needed)
window_size = 4

# Calculate the moving average
smoothed_memory_overhead = np.convolve(memory_overhead, np.ones(window_size)/window_size, mode='same')

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the original data
ax.plot(time, memory_overhead, label='Memory Overhead', marker='o')

# Plot the smoothed data
ax.plot(time, smoothed_memory_overhead, label='Smoothed Memory Overhead', linestyle='--')

# Set labels and legend
ax.set_xlabel('Time')
ax.set_ylabel('Memory Overhead')
ax.legend()

# Show the plot
plt.show()

