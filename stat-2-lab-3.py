import numpy as np
from stat_data import stat_data
from scipy.stats import shapiro
from stat_data import stat_data
import statsmodels.api as sm
import matplotlib.pyplot as plt
from estimates import mean, std_deviation

# Критерий Шапиро-Уилка

# 1 ШАГ. Выдвижение гипотезы
# Гипотеза о принадлежности выборки нормальному распределению

sign_level = 0.01;

# 2 ШАГ. Расчет

# 2 и 3 ШАГ. Расчет критической области
# Двусторонняя критическая область
# Двусторонний критерий позволяет обнаруживать как положительные, так и отрицательные отклонения от нормальности.
# Это важно, так как в реальных данных отклонения могут проявляться в обоих направлениях.
# Например, в наборе данных могут быть как выбросы с очень большими значениями, так и выбросы с очень маленькими значениями, и оба эти случая могут сигнализировать о нарушении нормальности.


statistic, p_value = shapiro(stat_data)

# 4 шаг
if p_value < sign_level:
    print(f"Данные не имеют нормальное распределение. p_value: {p_value}")
else:
    print(f"Данные могут иметь нормальное распределение. p_value: {p_value} ",)


data = np.array(stat_data)
normed_data = (data - mean) / std_deviation
sm.qqplot(normed_data, line='45', alpha=0.5, marker='o', color='b')
plt.title('QQ Plot')
plt.xlabel('Квантили (0, 1)')
plt.ylabel('Выборочные квантили')
plt.show()

