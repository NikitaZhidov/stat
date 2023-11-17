from stat_data2 import stat_data_1, stat_data_2
import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau, t, norm, rankdata

sign_level = 0.1

data1 = stat_data_1
data2 = stat_data_2

def manual_spearman(ranks1, ranks2):
  m1 = ranks1 - np.mean(ranks1)
  m2 = ranks2 - np.mean(ranks2)

  numerator = np.sum(m1 * m2)
  denominator = np.sqrt(np.sum(m1**2) * np.sum(m2**2))

  return numerator/denominator

def kendall_statistics_manual(ranks1, ranks2):
    n = len(ranks1)
    tau = 0

    for i in range(n):
        for j in range(i + 1, n):
            sgn1 = 0
            sgn2 = 0

            if ranks1[i] < ranks1[j]:
                sgn1 = 1
            elif ranks1[i] > ranks1[j]:
                sgn1 = -1

            if ranks2[i] < ranks2[j]:
                sgn2 = 1
            elif ranks2[i] > ranks2[j]:
                sgn2 = -1

            tau += sgn1 * sgn2

    tau *= 2 / (n * (n - 1))

    return tau

def kendall_tau_variance(n):
    return (2 * (2 * n + 5)) / (9 * n * (n - 1))

# Вычисляем ранги
ranks = rankdata(data1 + data2)

# Разделяем ранги обратно на две выборки
ranks_data1 = ranks[:len(data1)]
ranks_data2 = ranks[len(data1):]

data1_mean = np.mean(data1)
data2_mean = np.mean(data2)

# Ручной расчет
num_bins = 10

DATA_LENGTH = len(data1)

print(f"УРОВЕНЬ ЗНАЧИМОСТИ: {sign_level}")
print(" ")

# Гипотеза Коэфициент = 0
# Коэф корреляции Пирсона

# Рассчитываем числитель
numerator = np.sum((data1 - data1_mean) * (data2 - data2_mean))

# Рассчитываем знаменатель
denominator = np.sqrt(np.sum((data1 - data1_mean) ** 2) * np.sum((data2 - data2_mean) ** 2))

# Рассчитываем коэффициент корреляции Пирсона
c_pearson_manual = (numerator / denominator)

c_pearson, pvalue_pearson = pearsonr(data1, data2)
print(f"Пирсон: Коэффициент = {c_pearson}, (ручн.): {c_pearson_manual}, pvalue = {pvalue_pearson}")

statistics_pearson = (c_pearson_manual * np.sqrt(len(data1) - 2))/(1 - c_pearson_manual ** 2);
print(f"Пирсон: статистика = {statistics_pearson}, квантиль (Стьюдента) = {t.ppf(1 - sign_level, len(data1) - 2)}")

print(" ")

# Коэф корреляции Спирмена
c_spearman, pvalue_spearman = spearmanr(data1, data2)
print(f"Спирмен: Коэффициент = {c_spearman}, ручн.: {manual_spearman(ranks_data1, ranks_data2)} pvalue = {pvalue_spearman}")
statistics_spearman = np.sqrt(DATA_LENGTH) * np.abs(c_spearman)
print(f"Спирмен: статистика = {statistics_spearman}, квантиль (Норм распределение) = {norm.ppf(1 - sign_level/2)}");

print(" ")


# Коэф корреляции Кэндалла
c_kendall, pvalue_kendall = kendalltau(data1, data2)
print(f"Кэндалла: Коэффициент = {c_kendall}, pvalue = {pvalue_kendall}")

d_varaince = np.sqrt(kendall_tau_variance(len(data1)));
print(f"Кэндалл: статистика = {kendall_statistics_manual(ranks_data1, ranks_data2)}, квантиль (Норм распределения (0, {round(d_varaince, 5)})) = {norm.ppf(1 - sign_level/2, scale=d_varaince)}");
