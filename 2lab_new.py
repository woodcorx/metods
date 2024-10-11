import numpy as np
import matplotlib.pyplot as plt

# Вихідні дані
x_values = np.array([-4, -3, 0, 1])
y_values = np.array([-7, 10, -11, -22])

def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    L = np.zeros_like(x, dtype=float)

    for i in range(n):
        term = np.ones_like(x)
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        L += y_points[i] * term

    return L

x_new = np.array([-2, -0.5, 0.5, 2])

y_new = lagrange_interpolation(x_new, x_values, y_values)

y_new_rounded = np.round(y_new, 3)

for i, x in enumerate(x_new):
    print(f"Значення функції в точці x={x} дорівнює {y_new_rounded[i]:.3f}")

# Побудова графіка
x_range = np.linspace(min(x_values) - 1, max(x_values) + 1, 500)
y_range = lagrange_interpolation(x_range, x_values, y_values)

plt.plot(x_values, y_values, 'o', label='Відомі точки')
plt.plot(x_range, y_range, label='Інтерполяційна функція')
plt.scatter(x_new, y_new, color='red', label='Обчислені точки')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title("Інтерполяція Лагранжа")
plt.show()
