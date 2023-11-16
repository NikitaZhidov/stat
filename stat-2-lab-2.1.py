import numpy as np
from stat_data import stat_data
from estimates import stat_data_length, minimum, maximum
from scipy.stats import uniform, chisquare, chi2

# Критерий Пирсона

# 1 ШАГ. Выдвижение гипотезы
# Гипотеза о принадлежности выборки равномерному распределению

sign_level = 0.1;
null_hypothesis = uniform(minimum, maximum);

# 2 ШАГ. Выбор критической области

num_bins = 10

frequences, bins = np.histogram(stat_data, bins=num_bins)


def cdf(left, right):
  global minimum
  global maximum
  return null_hypothesis.cdf(right) - null_hypothesis.cdf(left);

X = 0
expected_frequencies = np.zeros(num_bins)

for index, value in enumerate(bins[:-1]):
  left_border = bins[index]
  right_border = bins[index + 1]

  v = frequences[index]
  np = stat_data_length * cdf(left_border, right_border) # сколько ожидаем в границах данных при условии H0

  X += ((v - np) ** 2)/np
  expected_frequencies[index] = np

# hAck
expected_frequencies += (sum(frequences) - sum(expected_frequencies)) / len(expected_frequencies)

chi, p = chisquare(f_obs=frequences, f_exp=expected_frequencies)

print(f"Статистика Хи квадрат: 1) {X} 2) (Автоматич.) {chi}");

# 3 ШАГ. Выбор критической области
# Правосторонняя критическая область Х^2 >= quantile | H0 = sign_level

quantile = chi2.ppf(1 - sign_level, len(stat_data) - 1)
print(f"Квантиль распределения Хи квадрат с уровне значимости {sign_level} и со степенями свободы {len(stat_data) - 1}: {quantile}")

# ШАГ 4. Принятие решения
if (X >= quantile):
  print('Гипотеза отвергается', f"{X} >= {quantile}, p_value: {p}")
else:
  print('Гипотеза не отвергается', f"{X} < {quantile}")
