from stat_data2 import stat_data_1, stat_data_2
from scipy.stats import mannwhitneyu

sign_level = 0.01

# Гипотеза: H0 выборки принадлежат одному распределению

# Критерий Вилкоксона (Манна Уитни)
data1 = stat_data_1
data2 = stat_data_2

# Выполнение критерия Уилкоксона
statistics, pvalue = mannwhitneyu(data1, data2, alternative="two-sided")

print(f"Статистика: {statistics}, pvalue: {pvalue}, уровень значимости: {sign_level}")
print(f"Гипотеза: {'верна' if pvalue > sign_level else 'неверна'} ")
