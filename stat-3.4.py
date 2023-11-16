from stat_data2 import stat_data_1, stat_data_2
from scipy.stats import norm
import numpy as np
from statsmodels.sandbox.stats.runs import runstest_1samp, runstest_2samp


sign_level = 0.1

# Гипотеза: H0 выборки принадлежат одному распределению

# Критерий серий
data1 = stat_data_1
data2 = stat_data_2

_d1 = list(map(lambda x: dict(sample=0, data=x), data1));
_d2 = list(map(lambda x: dict(sample=1, data=x), data2));

_merged = _d1 + _d2

_merged_sorted = sorted(_merged, key=lambda x: x['data'])

series = np.array(list(map(lambda x: x['sample'], _merged_sorted)))

series_count = 1
for i in range(1, len(series)):
    if series[i] != series[i - 1]:
        series_count += 1


statistics, pvalue = runstest_1samp(series, correction=False)
statistics2, pvalue2 = runstest_2samp(data1, data2, correction=False)

quantile = norm.ppf(1 - sign_level)

print(f"1) Статистика: {statistics}, pvalue: {pvalue}")
print(f"2) Статистика: {statistics2}, pvalue: {pvalue2}")
print(f"Квантиль для уровня значимости {sign_level}, {quantile}")

print(f"Гипотеза {'принимается' if statistics <= quantile else 'отвергается'}")
