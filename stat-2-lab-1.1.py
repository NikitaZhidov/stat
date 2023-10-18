from ecdf import ecdf, ecdf_edges_middles, ecdf_edges, ecdf_plot
from stat_data import stat_data
from estimates import maximum, minimum
from scipy.stats import uniform
import numpy as np
from scipy.stats import kstest, ksone, uniform
import matplotlib.pyplot as plt

# 1 ШАГ. Выдвижение гипотезы
# Гипотеза о принадлежности выборки равномерному распределению

sign_level = 0.1;
null_hypothesis = uniform(minimum, maximum)

# 2 ШАГ. Считаем статистику критерия
# D = sup|F'() - F()| (теоретич - эмпирич)

# Значения ЭМПИРИЧЕСКОЙ и ТЕОРЕТИЧЕСКОЙ функций распределения
F_empiric_values = [ecdf(x) for x in ecdf_edges_middles]
F_theoretical_values = [null_hypothesis.cdf(x) for x in ecdf_edges_middles]

# Нахождение статистики Колмогорова
D = max([abs(F_empiric_values[i] - F_theoretical_values[i]) for i in range(0, len(F_empiric_values))])

# Визуализация
fg = plt.figure();
fg.suptitle('Принадлежность выборки равномерному распределению');

ax1 = fg.add_subplot(211)
ax2 = fg.add_subplot(212)

ecdf_plot(ax1, label="Эмпирическая функция распределения")
ax1.plot([x for x in ecdf_edges[:-1]], [x for x in F_theoretical_values], label="Теоретическая функция распределения")
ax1.legend();
ax2.scatter([x for x in ecdf_edges[:-1]], [null_hypothesis.ppf(x) for x in F_empiric_values], label="График квантиль-квантиль")

# 45 градусов линия
ax2.plot([0, ecdf_edges[-1]], [0, ecdf_edges[-1]], color='red', linestyle='--')

plt.legend();
plt.show();

# Пересчет автоматич средствавми
normalized_data = (np.array(stat_data) - min(stat_data)) / (max(stat_data) - min(stat_data))
kstest_uniform = kstest(normalized_data, 'uniform')

print(f"Статистика Колмогорова: 1) {D}  2) (Автоматич.) {kstest_uniform.statistic}")

# 3 ШАГ. Определение Критической области
# Правосторонняя критическая область sqrt(n) * N >= quantile | H0 ~ 1 - K(quantile) = sign_level

# Квантиль распределения Коломогорова
quantile = ksone.ppf(1 - sign_level, len(stat_data))
print(f"Квантиль распределения Коломогорова при уровне значимости {sign_level}: {quantile}")

# 4 ШАГ. Принятие решения
Z = (len(stat_data) ** 1/2) * D
print("sqrt(n) * статистика Колмогорова: ", Z)

if (Z >= quantile):
  print('Гипотеза отвергается', f"{Z} >= {quantile}")
else:
  print('Гипотеза отвергается', f"{Z} < {quantile}")
