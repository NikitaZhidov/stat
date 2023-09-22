from stat_data import stat_data
import numpy as np
import scipy.stats as stats

def calculate_first_stat_data_moment(moment_order):
  return np.mean(np.array(stat_data) ** moment_order)

def calculate_central_stat_data_moment(moment_order):
  return np.mean((np.array(stat_data) - mean) ** moment_order)

def print_calculated_estimates():
  print(f"Мат ожидание: {round(mean, 2)}");
  print(f"Дисперсия (несмещенная): {round(variance, 2)}");
  print(f"Среднеквадратическое отклонение: {round(std_deviation, 2)}")

  for moment_order, moment in enumerate(first_moments, 1):
    print(f"Начальный момент {moment_order} порядка: {round(moment, 2)}")

  for moment_order, moment in enumerate(central_moments, 1):
    print(f"Центральный {moment_order} порядка: {round(moment, 2)}")

  print(f"Эксцесс: {kurtosis_value} (пр.: {stats.kurtosis(stat_data)})")
  print(f"Коэффициент ассиметрии: {skewness} (пр.: {stats.skew(stat_data)})")

  print(f"Медиана: {median}")

stat_data_length = len(stat_data)

# Мат ожидание
mean = calculate_first_stat_data_moment(1)

# Дисперсия (несмещенная)
variance = np.var(stat_data, ddof=1)

# Среднеквадратическое отклонение
std_deviation = variance ** (1/2)

# Начальные моменты
first_moments = [calculate_first_stat_data_moment(i) for i in range(1, 5)]
[first_moment_1, first_moment_2, first_moment_3, first_moment_4] = first_moments

# Центральные моменты
central_moments = [calculate_central_stat_data_moment(i) for i in range(1, 5)]
[central_moment_1, central_moment_2, central_moment_3, central_moment_4] = central_moments;

# Эксцесс
kurtosis_value = central_moment_4 / (central_moment_2 ** 2) - 3;

# Коэффициент ассиметрии
skewness = central_moment_3 / (std_deviation ** 3)

# Медиана
median = np.median(stat_data)

printCalculatedEstimates = False

if printCalculatedEstimates:
  print_calculated_estimates()
