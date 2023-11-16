from ecdf import ecdf, ecdf_edges_middles, ecdf_edges, ecdf_plot, ecdf_exact
from stat_data import stat_data
from estimates import mean, minimum
from scipy.stats import expon
import numpy as np
from scipy.stats import kstest, ksone
from scipy.stats import kstwobign

import matplotlib.pyplot as plt


# 1 ШАГ. Выдвижение гипотезы
# Гипотеза о принадлежности выборки экспоненциальному распределению

sign_level = 0.1;
null_hypothesis = expon(scale=mean, loc=minimum)

y1 = null_hypothesis.cdf(ecdf_edges_middles[0])
y2 = 1 - np.exp(-(1/mean) * ecdf_edges_middles[0])

print(f"y1: {y1}, y2: {y2}");

# 2 ШАГ. Считаем статистику критерия
# D = sup|F'() - F()| (теоретич - эмпирич)


# Значения ЭМПИРИЧЕСКОЙ и ТЕОРЕТИЧЕСКОЙ функций распределения
F_empiric_values = [ecdf_exact(x) for x in ecdf_edges_middles]
F_theoretical_values = [null_hypothesis.cdf(x) for x in ecdf_edges_middles]

# Нахождение статистики Колмогорова
D = max([abs(F_empiric_values[i] - F_theoretical_values[i]) for i in range(0, len(F_empiric_values))])

# Визуализация
fg = plt.figure();
fg.suptitle('Принадлежность выборки экспоненциальному распределению');

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
kstest_expon = kstest(stat_data, null_hypothesis.cdf)

print(f"Статистика Колмогорова: 1) {D}  2) (Автоматич.) {kstest_expon.statistic}")

# 3 ШАГ. Определение Критической области
# Правосторонняя критическая область sqrt(n) * N >= quantile | H0 ~ 1 - K(quantile) = sign_level

# Квантиль распределения Коломогорова
quantile = kstwobign.ppf(1 - sign_level)
print(f"Квантиль распределения Коломогорова при уровне значимости {sign_level}: {quantile}, p_value: {kstest_expon.pvalue}")

# 4 ШАГ. Принятие решения
Z = (len(stat_data) ** 0.5) * kstest_expon.statistic
print("sqrt(n) * статистика Колмогорова: ", Z)

if (Z >= quantile):
  print('Гипотеза отвергается', f"{Z} >= {quantile}")
else:
  print('Гипотеза принимается', f"{Z} < {quantile}")
