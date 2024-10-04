import numpy as np
import matplotlib.pyplot as plt

def interpolation(x_values, y_values):
    def basis_poly(i):
        def basis(x):
            result = 1
            for j in range(len(x_values)):
                if i != j:
                    # Обчислення базисну функцію Лагранжа для точки i
                    result *= (x - x_values[j]) / (x_values[i] - x_values[j])
            return result
        return basis

    def lagrange_polynomial(x):
        result = 0
        for i in range(len(x_values)):
            # Обчислюємо значення інтерполяційного багаточлена Лагранжа
            # Як суму добутків значень y_values на базисні функції для кожної точки
            result += y_values[i] * basis_poly(i)(x)
        return result

    return lagrange_polynomial

# Задані значення
x_values = [-4, -3, 0, 1]
y_values = [-7, -10, -11, -22]

# Побудова інтерполяційного багаточлена Лагранжа
interpolation_func = interpolation(x_values, y_values)

# Значення точок з другої таблиці
x_values_to_evaluate = [-2, -0.5, 0.5, 2]

# Обчислення значення інтерполяційної функції для кожного x
for x in x_values_to_evaluate:
    result = interpolation_func(x)
    print(f"Значення функції в точці x={x} дорівнює {result}")

# Графік інтерполяційної функції та заданих точок
x_plot = np.linspace(min(x_values + x_values_to_evaluate), max(x_values + x_values_to_evaluate), 400)
y_plot = [interpolation_func(x) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label="Інтерполяційна функція", linewidth=2)
plt.scatter(x_values, y_values, color='red', label='Задані точки')
plt.scatter(x_values_to_evaluate, [interpolation_func(x) for x in x_values_to_evaluate], color='green', label='Точки оцінки')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Інтерполяція за допомогою багаточлена Лагранжа')
plt.legend()
plt.show()
