import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#The uploading data and calculating the averages for the pdf size IoT statistics
pdf_size_iot = pd.read_csv('graph-size-IoT-statistics.csv')
pdf_size_iot.columns = pdf_size_iot.columns.astype(int)
pdf_size_iot = pdf_size_iot.reindex(sorted(pdf_size_iot.columns), axis=1)
pdf_size_iot = pdf_size_iot.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(pdf_size_iot)

column_averages_pdf_size_iot = pdf_size_iot.mean()
# Format the mean values to display with 2 decimal places
column_averages_pdf_size_iot = column_averages_pdf_size_iot.apply(lambda x: '{:.2f}'.format(x))
# Convert the Series to float data type
column_averages_pdf_size_iot = column_averages_pdf_size_iot.astype(float)
print(column_averages_pdf_size_iot)

#The uploading data and calculating the averages for the pdf size IoT + classic statistics
pdf_size_total = pd.read_csv('graph-size-Total-statistics.csv')
pdf_size_total .columns = pdf_size_total.columns.astype(int)
pdf_size_total = pdf_size_total.reindex(sorted(pdf_size_total.columns), axis=1)
pdf_size_total = pdf_size_total.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
print(pdf_size_total)

column_averages_pdf_size_total = pdf_size_total.mean()
# Format the mean values to display with 2 decimal places
column_averages_pdf_size_total = column_averages_pdf_size_total.apply(lambda x: '{:.2f}'.format(x))
# Convert the Series to float data type
column_averages_pdf_size_total = column_averages_pdf_size_total.astype(float)
print(column_averages_pdf_size_total)

# get a size of classic IoC pdf file
pdf_size_classic = column_averages_pdf_size_total - column_averages_pdf_size_iot
print(pdf_size_classic)

x_array_num_nodes = pdf_size_classic.index.to_numpy()
print(x_array_num_nodes)
y_pdf_size_total = column_averages_pdf_size_total.to_numpy()
print(y_pdf_size_total)
y_pdf_size_iot_ioc = column_averages_pdf_size_iot.to_numpy()
print(y_pdf_size_iot_ioc)
upward_trend_values_iot = []
counter_summary = []
previous_biggest = y_pdf_size_iot_ioc[0]
upward_trend_values_iot.insert(0, y_pdf_size_iot_ioc[0])
counter_summary.append(0)
# Start from the second element (index 1) and compare with the previous element
for index, time in enumerate(y_pdf_size_iot_ioc):
    if time > previous_biggest:
        upward_trend_values_iot.append(time)
        previous_biggest = time
        counter_summary.append(index)
print(counter_summary, len(counter_summary))
print(upward_trend_values_iot, len(upward_trend_values_iot))

y_pdf_size_classic_ioc = pdf_size_classic.to_numpy()
print(y_pdf_size_classic_ioc)

upward_trend_values_classic = []
for i in counter_summary:
    upward_trend_values_classic.append(y_pdf_size_classic_ioc[i])
upward_trend_values_classic = [round(number, 2) for number in upward_trend_values_classic]
print(upward_trend_values_classic, len(upward_trend_values_classic))

upward_trend_x_array =[]
for i in counter_summary:
    upward_trend_x_array.append(x_array_num_nodes[i])
print(upward_trend_x_array, len(upward_trend_x_array))

# Define custom x-axis ticks with step size
x_custom_ticks = np.arange(3, 420, 20)  # Start at 1, end at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(0, 90, 10)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=7)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

#plotting section with settings
# plt.plot(x_array_num_nodes, y_pdf_size_iot_ioc, 'o-b', ms=3, label = 'visual representation of IoT-specific IoCs')
# plt.plot(x_array_num_nodes, y_pdf_size_classic_ioc, 'o-y', ms=3, label = 'visual representation of traditional IoCs')

plt.plot(upward_trend_x_array, upward_trend_values_iot, 'o-b', ms=3, label = 'visual representation of IoT-specific IoCs')
plt.plot(upward_trend_x_array, upward_trend_values_classic, 'o-y', ms=3, label = 'visual representation of traditional IoCs')
# plt.plot(x_array_time, y_summary_time, 'o-r', ms=3)
plt.title("PDF size")
plt.xlabel("Number of extracted IoCs")
plt.ylabel("PDF graph size, KB")
plt.legend()
plt.show()