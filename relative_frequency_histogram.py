import numpy as np
import matplotlib.pyplot as plt
from stat_data import stat_data

num_bins = 10
stat_frequencies, bin_edges = np.histogram(stat_data, bins=num_bins)
relative_stat_frequencies = stat_frequencies / len(stat_data) / np.diff(bin_edges)

print(relative_stat_frequencies)
print(sum(relative_stat_frequencies))

plt.figure(figsize=(8, 6))
plt.bar(bin_edges[:-1], relative_stat_frequencies, width=np.diff(bin_edges), alpha=0.75, color='b', align='edge')

plt.xlabel('Значение')
plt.ylabel('Относительная частота')
plt.title('Гистограмма относительных частот')
plt.grid(True)

plt.show()
