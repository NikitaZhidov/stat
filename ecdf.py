import numpy as np
import matplotlib.pyplot as plt

from stat_data import stat_data

sorted_data = np.sort(stat_data)

# Делим выборку на 10 частей
num_bins = 10
_, ecdf_edges = np.histogram(sorted_data, bins=num_bins)

ecdf_edges_middles = [(ecdf_edges[i] + ecdf_edges[i + 1]) / 2 for i in range(len(ecdf_edges) - 1)]
stat_data_length = len(stat_data);

ecdf_relative_frequencies = [
  sum(1 for x in stat_data if x < right_edge)/stat_data_length
  for right_edge in np.append(ecdf_edges[1:], np.Infinity)
]


def ecdf(value):
  global ecdf_relative_frequencies
  global ecdf_edges

  for index, edge in enumerate(ecdf_edges):
    if (value < edge):
      if (index == 0):
        return 0;
      return ecdf_relative_frequencies[index - 1]

  return 1;

def ecdf_plot(plot, label):
  global ecdf_relative_frequencies
  global ecdf_edges

  for idx, f in enumerate(ecdf_relative_frequencies):
    xmaxIndex = min(len(ecdf_edges) - 1, idx + 1)
    plot.hlines(f, xmin=ecdf_edges[idx], xmax=ecdf_edges[xmaxIndex], color='blue')

  plot.scatter(ecdf_edges, ecdf_relative_frequencies, color='b', marker="o", label=label)

# Построение ECDF графика
# for idx, f in enumerate(ecdf_relative_frequencies):
#   xmaxIndex = min(len(ecdf_edges) - 1, idx + 1)
#   plt.hlines(f, xmin=ecdf_edges[idx], xmax=ecdf_edges[xmaxIndex], color='blue')

# plt.title('Эмпирическая функция распределения')
# plt.xlabel('Значения')
# plt.ylabel('Относительные частоты')

# Точки
# plt.scatter(ecdf_edges, ecdf_relative_frequencies, color='b', marker="o")
# plt.show()
