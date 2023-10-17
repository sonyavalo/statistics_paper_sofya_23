import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_array_number_events = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
y_array_storage = [62.4, 124, 186, 249, 310, 374, 426, 496, 566, 635, 701, 769, 814, 859, 890, 921, 952]

#plotting section with settings
plt.plot(x_array_number_events, y_array_storage, 'o-b', ms=3, label = 'Visual and machine-readable output storage usage')

# Define custom x-axis ticks with step size
x_custom_ticks = np.arange(2, 36, 2)  # Start at 1, end at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(50, 1000, 100)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=8)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

plt.title("The output storage usage based on the amount of processed incidents")
plt.xlabel("Number of Incidents (x100)")
plt.ylabel("Storage Usage (MB)")
plt.tight_layout()
plt.legend()
plt.show()