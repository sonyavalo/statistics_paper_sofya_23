import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#The uploading data and calculating the averages for the pdf size IoT statistics
number_of_iot_iocs = pd.read_csv('graph-nodes-number-statistics.csv')
number_of_iot_iocs.columns = number_of_iot_iocs.columns.astype(int)
number_of_iot_iocs= number_of_iot_iocs.reindex(sorted(number_of_iot_iocs.columns), axis=1)
print(number_of_iot_iocs)

number_of_iot_iocs = number_of_iot_iocs.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
# Convert all values in the DataFrame to integers
number_of_iot_iocs = number_of_iot_iocs.fillna(0).astype(int)
print(number_of_iot_iocs)

# Extract the first row as a NumPy array
number_of_iot_ioc_array = number_of_iot_iocs.iloc[0].to_numpy()
print(number_of_iot_ioc_array)

total_number_iocs = number_of_iot_iocs.columns.to_numpy()
print(total_number_iocs)

number_of_classic_iocs_array = total_number_iocs - number_of_iot_ioc_array
print(number_of_classic_iocs_array)

percentage_iot_iocs = (number_of_iot_ioc_array/total_number_iocs)*100
print(percentage_iot_iocs)

percentage_classic_iocs = (number_of_classic_iocs_array/total_number_iocs)*100
print(percentage_classic_iocs)

# Create the stacked columns
plt.bar(total_number_iocs, percentage_iot_iocs, label='IoT-specific IoCs', color='b', width = 2)
plt.bar(total_number_iocs, percentage_classic_iocs, label='Traditional IoCs', bottom=percentage_iot_iocs, color='y', width = 2)

plt.title("  ")
plt.xlabel("Total number of extracted IoCs")
plt.ylabel("Percent of total amount of IoCs, %")
plt.legend()
plt.show()

