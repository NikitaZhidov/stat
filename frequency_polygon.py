import numpy as np
import matplotlib.pyplot as plt
from stat_data import stat_data

# Делим выборку на 10 частей
num_bins = 10
stat_frequencies, bin_edges = np.histogram(stat_data, bins=num_bins)

# Центры интервалов
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.figure(figsize=(8, 6))
plt.plot(bin_centers, stat_frequencies, marker='o')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Полигон частот')
plt.grid(True)
plt.show()
