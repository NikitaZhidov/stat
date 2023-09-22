from estimates import mean, std_deviation, stat_data_length
from scipy.stats import norm

def get_mean_confidence_delta(confidence_level):
  critical_z = norm.ppf((1 + confidence_level) / 2)
  return critical_z * std_deviation / (stat_data_length ** (1/2));

def print_conf_interval(confidence_level):
  delta = get_mean_confidence_delta(confidence_level);
  print(f"Доверительный интервал: [{mean - delta}, {mean + delta}] с уровнем доверия {int(confidence_level * 100)}%")

print_conf_interval(0.95)
print_conf_interval(0.99)
