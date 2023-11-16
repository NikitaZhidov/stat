from stat_data2 import stat_data_1, stat_data_2
from scipy.stats import chi2_contingency, chi2, chisquare
import numpy as np

sign_level = 0.1

# Гипотеза: H0 выборки принадлежат одному распределению

# Критерий Хи квадрат
data1 = stat_data_1
data2 = stat_data_2

# Ручной расчет

num_bins = 10
freq_1, _ = np.histogram(data1, bins=10)
freq_2, _ = np.histogram(data2, bins=10)

epsilon = 1
freq_1 += epsilon
freq_2 += epsilon

TOTAL = freq_1 + freq_2
TOTAL_sums = np.sum(TOTAL);

expected_freq_1 = (TOTAL / TOTAL_sums) * np.sum(freq_1)
expected_freq_2 = (TOTAL / TOTAL_sums) * np.sum(freq_2)

statistics = np.sum((freq_1 - expected_freq_1) ** 2 / expected_freq_1)

print(f"STATISTICS: {statistics}")

chi_square_statistic = np.sum((freq_1 / len(stat_data_1) - freq_2 / len(stat_data_2))**2 / (freq_1 + freq_2))

# Автоматический
# Статистика хи квадрат
statistics2, pvalue2 = chisquare(freq_2, expected_freq_2)

quantile = chi2.ppf(1 - sign_level, num_bins - 1)

print(f"2) Статистика: {statistics2}, pvalue: {pvalue2}, уровень значимости: {sign_level}, квантиль: {quantile}")
print(f"Гипотеза: {'отвергается' if statistics2 > quantile else 'не отвергается'} ")
