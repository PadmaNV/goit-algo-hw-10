import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та її інтеграл
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Кількість випадкових точок
N1 = 1000
N2 = 1000000

# Генерування випадкових точок
x_random1 = np.random.uniform(a, b, N1)
x_random2 = np.random.uniform(a, b, N2)

# Обчислення значень функції випадкових точок
f_values1 = f(x_random1)
f_values2 = f(x_random2)

# Визначення кількості точок, що потрапили під криву
points_under_curve1 = sum(np.random.uniform(0, max(f_values1), N1) < f_values1)
points_under_curve2 = sum(np.random.uniform(0, max(f_values2), N2) < f_values2)

# Обчислення відношення кількості точок під кривою до загальної кількості точок
fraction_under_curve1 = points_under_curve1 / N1
fraction_under_curve2 = points_under_curve2 / N2

# Обчислення площі прямокутника
rectangle_area = (b - a) * max(max(f_values1), max(f_values2))

# Обчислення площі під кривою
area_under_curve1 = rectangle_area * fraction_under_curve1
area_under_curve2 = rectangle_area * fraction_under_curve2

# Аналітичний розрахунок інтегралу
analytical_result, error = quad(f, a, b)

print("Значення інтеграла методом Монте-Карло з 1000 випадкових точок:", area_under_curve1)
print("Значення інтеграла методом Монте-Карло з 1000 000 випадкових точок:", area_under_curve2)
print("Аналітичний результат інтеграла:", analytical_result)
