from stat_data2 import stat_data_1, stat_data_2
from scipy.stats import chi2_contingency, chi2
import numpy as np

sign_level = 0.1

# Гипотеза: H0 - выборки НЕЗАВИСИМЫ

# Критерий Хи квадрат
data1 = stat_data_1
data2 = stat_data_2

# Ручной расчет

num_bins = 10
freq_1, borders_1 = np.histogram(data1, bins=10)
freq_2, borders_2 = np.histogram(data2, bins=10)

freq_1+=1
freq_2+=1

def get_bin_num(x, borders):
    if (x < borders[1]):
        return 0
    for i in range(len(borders) - 1):
        if x > borders[i] and x <= borders[i + 1]:
            return i


# Ручная статистика
def chi_square_test_manual(observed):
    # сумма по строкам
    row_totals = np.sum(observed, axis=1)
    # сумма по столбцам
    col_totals = np.sum(observed, axis=0)

    total_observed = np.sum(observed)

    print(f"[TOTAL OBSERVED]: {total_observed}")
    # Ожидаемые частоты
    expected = np.outer(row_totals, col_totals) / total_observed

    expected[expected == 0] = 1e-10

    chi2_stat = np.sum((observed - expected)**2 / expected)

    print(f"chi2_stat: {chi2_stat}");

    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)

    quantile = chi2.ppf(1 - sign_level, df)
    print(f"Критическое значение: {quantile}")

    # Compare chi-square statistic to critical value
    if chi2_stat > quantile:
        print("Ручн.: зависимы")
    else:
        print("Ручн.: независимы")


table = np.zeros((10, 10));

for x, y in zip(data1, data2):
    i = get_bin_num(x, borders_1)
    j = get_bin_num(y, borders_2)

    table[i, j] += 1

print(np.sum(table))


chi_square_test_manual(table)

table[table == 0] += 0.00000001

# Автоматический
# Статистика хи квадрат
statistics2, pvalue2, dof, _ = chi2_contingency(table)

quantile = chi2.ppf(1 - sign_level, dof)

print(f"Статистика: {statistics2}, pvalue: {pvalue2}, уровень значимости: {sign_level}, квантиль: {quantile}")
print(f"Гипотеза: {'отвергается' if statistics2 > quantile else 'не отвергается'} ")
