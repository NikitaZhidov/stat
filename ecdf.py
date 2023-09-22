import numpy as np
import matplotlib.pyplot as plt

from stat_data import stat_data

sorted_data = np.sort(stat_data)

# Делим выборку на 10 частей
num_bins = 10
_, bin_edges = np.histogram(sorted_data, bins=num_bins)

stat_data_length = len(stat_data);

ecdf_relative_frequencies = [
  sum(1 for x in stat_data if x < right_edge)/stat_data_length
  for right_edge in np.append(bin_edges[1:], np.Infinity)
]

# Построение ECDF графика
for idx, f in enumerate(ecdf_relative_frequencies):
  xmaxIndex = min(len(bin_edges) - 1, idx + 1)
  plt.hlines(f, xmin=bin_edges[idx], xmax=bin_edges[xmaxIndex], color='blue')

plt.title('Эмпирическая функция распределения')
plt.xlabel('Значения')
plt.ylabel('Относительные частоты')

# Точки
plt.scatter(bin_edges, ecdf_relative_frequencies, color='b', marker="o")
plt.show()
