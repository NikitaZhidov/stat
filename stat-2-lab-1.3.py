from ecdf import ecdf, ecdf_edges_middles, ecdf_edges, ecdf_plot, ecdf_exact
from stat_data import stat_data
from estimates import maximum, minimum, std_deviation, mean
from scipy.stats import norm
import numpy as np
from scipy.stats import kstest, ksone
from scipy.stats import kstwobign

import matplotlib.pyplot as plt


# 1 ШАГ. Выдвижение гипотезы
# Гипотеза о принадлежности выборки нормальному распределению

sign_level = 0.1;
null_hypothesis = norm(loc=mean, scale=std_deviation)

y1 = null_hypothesis.pdf(0.5);
y2 = np.exp((-1/2)*((0.5 - std_deviation)/std_deviation) ** 2) / (std_deviation * (2 * np.pi) ** 0.5)

# 2 ШАГ. Считаем статистику критерия
# D = sup|F'() - F()| (теоретич - эмпирич)

# Значения ЭМПИРИЧЕСКОЙ и ТЕОРЕТИЧЕСКОЙ функций распределения
F_empiric_values = [ecdf_exact(x) for x in ecdf_edges_middles]
F_theoretical_values = [null_hypothesis.cdf(x) for x in ecdf_edges_middles]

# Нахождение статистики Колмогорова
D = max([abs(F_empiric_values[i] - F_theoretical_values[i]) for i in range(0, len(F_empiric_values))])

# Визуализация
fg = plt.figure();
fg.suptitle('Принадлежность выборки нормальному распределению');
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
print(f"Квантиль распределения Коломогорова при уровне значимости {sign_level}: {quantile}")

# 4 ШАГ. Принятие решения
Z = (len(stat_data) ** 1/2) * D
print("sqrt(n) * статистика Колмогорова: ", Z)

if (Z >= quantile):
  print('Гипотеза отвергается', f"{Z} >= {quantile}, {kstest_expon.pvalue}")
else:
  print('Гипотеза отвергается', f"{Z} < {quantile}")
