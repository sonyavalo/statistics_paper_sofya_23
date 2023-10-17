import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#The uploading data and calculating the averages for the pdf size IoT statistics
types_of_classic_iocs = pd.read_csv('classic-ioc-types-statistics.csv')
types_of_classic_iocs.columns = types_of_classic_iocs.columns.astype(int)
types_of_classic_iocs = types_of_classic_iocs.reindex(sorted(types_of_classic_iocs.columns), axis=1)
types_of_classic_iocs = types_of_classic_iocs.apply(pd.to_numeric, errors='coerce')
# Display the DataFrame with all columns converted to numeric
print("\nDataFrame with All Columns Converted to Numeric:")
# Convert all values in the DataFrame to integers
types_of_classic_iocs = types_of_classic_iocs.fillna(0).astype(int)
print(types_of_classic_iocs)

cpe = types_of_classic_iocs.iloc[::4].reset_index(drop=True)
cpe_mean = cpe.mean()
cpe_mean = round(cpe_mean)
print(cpe_mean, 'cpe')
cve = types_of_classic_iocs.iloc[1::4].reset_index(drop=True)
cve_mean = cve.mean()
cve_mean = round(cve_mean)
print(cve_mean, 'cve')
cwe = types_of_classic_iocs.iloc[2::4].reset_index(drop=True)
cwe_mean = cwe.mean()
cwe_mean = round(cwe_mean)
print(cwe_mean, 'cwe')
capec = types_of_classic_iocs.iloc[3::4].reset_index(drop=True)
capec_mean = capec.mean()
capec_mean = round(capec_mean)
print(capec_mean, 'capec')

x_array_num_nodes = capec_mean.index.to_numpy()
print(x_array_num_nodes)
y_cpe = cpe_mean.to_numpy()
y_cve = cve_mean.to_numpy()
y_cwe = cwe_mean.to_numpy()
y_capec = capec_mean.to_numpy()

plt.scatter(x_array_num_nodes, y_cpe, marker='o', color='b', s=5, label = 'CPE IoCs')
plt.scatter(x_array_num_nodes, y_cve, marker='o', color='r', s=5, label = 'CVE IoCs')
plt.scatter(x_array_num_nodes, y_cwe, marker='o', color='c', s=5, label = 'CWE IoCs')
plt.scatter(x_array_num_nodes, y_capec, marker='o', color='m', s=5, label = 'CAPEC IoCs')

# Define custom x-axis ticks with step size
x_custom_ticks = np.arange(3, 420, 20)  # Start at 1, end at 10, step by 2
x_custom_labels = [str(tick) for tick in x_custom_ticks]
y_custom_ticks = np.arange(0, 170, 20)  # Start at 1, end at 10, step by 2
y_custom_labels = [str(tick) for tick in y_custom_ticks]

# Set custom x-axis ticks and labels
plt.xticks(x_custom_ticks, x_custom_labels, fontsize=8)
plt.yticks(y_custom_ticks, y_custom_labels, fontsize=8)

plt.title("Traditional IoCs types distribution")
plt.xlabel("Number of extracted IoCs")
plt.ylabel("Number of IoCs of a particular type")
plt.tight_layout()
plt.legend()
plt.show()