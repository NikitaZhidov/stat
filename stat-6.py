import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./Samples_3.csv")

X = data[['X1', 'X2', 'X3', 'X4']]
y = data['Y']

# Решение методом наименьших квадратов
result = np.linalg.lstsq(X, y, rcond=None)

x_coeffs = result[0]

y_pred = np.dot(X, x_coeffs)

RSS = np.sum((y - y_pred) ** 2)
TSS = np.sum((y - np.mean(y)) ** 2)

det_coef = 1 - RSS / TSS

print(f"Коэффициент детерминации: {det_coef}, множественный коэффициент корреляции: {np.sqrt(det_coef)}")

# График
plt.scatter(y, y_pred)  # Фактические значения Y vs. предсказанные значения Y
plt.xlabel('Фактические значения Y')
plt.ylabel('Предсказанные значения Y')
plt.title('Зависимость предсказанных от фактических значений')
plt.show()