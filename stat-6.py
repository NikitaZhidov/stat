import pandas as pd
import statsmodels.api as sm
from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./Samples_3.csv")

X = data[['X1', 'X2', 'X3', 'X4']]
y = data['Y']

n = len(data)
d = 4 #X1, X2, X3, X4
p = d + 1

# Решение методом наименьших квадратов
result = np.linalg.lstsq(X, y, rcond=None)

# Линейная регрессия. Коэффиуиенты
x_coeffs = result[0]

y_pred = np.dot(X, x_coeffs)

# Ковариационная матрица
cov_matrix = np.cov(y, y_pred);

RSS = np.sum((y - y_pred) ** 2)
TSS = np.sum((y - np.mean(y)) ** 2)

# Коэффициент детерминации. Представляет собой меру того, насколько хорошо модель соответствует данным
det_coef = 1 - RSS / TSS

print(f"Коэффициент детерминации: {det_coef}, множественный коэффициент корреляции: {np.sqrt(det_coef)}")
r_squared = np.square(cov_matrix[0, 1]) / (cov_matrix[0, 0] * cov_matrix[1, 1])
print(f"Множественный коэффициент корреляции (через матрицу): {np.sqrt(r_squared)}")

RSE = RSS / (n - p); # Этот показатель измеряет разброс фактических значений от предсказанных значений и служит мерой того, насколько хорошо модель соответствует данным.
print(f"RSE, дисперсия ошибки: {RSE}")

# ЗНАЧИМОСТЬ УРОВНЕНИЯ РЕГРЕССИИ
# H0 - коэффициенты регрессии = 0 (т.е. гипотеза о НЕЗНАЧИМОСТИ)
sign_level = 0.1

fisher_statistics = det_coef / (1 - det_coef) * (n - p)/(p - 1)

model = sm.OLS(y, X).fit()
# F-тест (критерий Фишера)
f_statistic_auto = model.fvalue
p_value = model.f_pvalue

quantile = f.ppf(1 - sign_level, p - 1, n - p)
print(f"Статистика Фишера. Ручная: {fisher_statistics}, Автоматическая: {f_statistic_auto}. квантиль: {quantile}, p_value: {p_value}")

# Остатки
residuals = y - y_pred

fg = plt.figure();

ax1 = fg.add_subplot(211)
ax2 = fg.add_subplot(212)

# Построение гистограммы остатков
ax1.hist(residuals, bins='auto', edgecolor='black')
ax1.set_title('Гистограмма остатков')
ax1.set_ylabel('Частота')


# График зависимости наблюдаемого и предсказываемого значения Y
ax2.scatter(y, y_pred, color='blue', edgecolors=(0, 0, 0))
ax2.plot([y.min(), y.max()], [y.min(), y.max()], linestyle='--', color='red', linewidth=2)
ax2.set_xlabel('Наблюдаемое значение Y')
ax2.set_ylabel('Предсказанное значение Y')

plt.show()
