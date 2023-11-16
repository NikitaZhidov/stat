from stat_data2 import stat_data_1, stat_data_2
from scipy.stats import ks_2samp
import numpy as np
from ecdf import ecdf_for_sample
from scipy.stats import kstwobign

sign_level = 0.01

# Гипотеза: H0 выборки принадлежат одному распределению

# Критерий Колмогорова-Смирнова
data1 = stat_data_1
data2 = stat_data_2

f = (len(data1) * len(data2) / (len(data1) + len(data2))) ** 0.5
my_statistics = max([abs(ecdf_for_sample(data1, x) - ecdf_for_sample(data2, x)) for x in data1]) * f

statistics, pvalue = ks_2samp(data1, data2)

quantile = kstwobign.ppf(1 - sign_level)

print(f"Ручная статистика: {my_statistics}, Статистика: {statistics * f}, pvalue: {pvalue}, уровень значимости: {sign_level}")
print(f"Квантиль: {quantile}")

print(f"Гипотеза: {'верна' if quantile > my_statistics else 'неверна'} ")
