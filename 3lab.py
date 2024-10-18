from tabulate import tabulate

main_table = {
    'i': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'x_i': [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6],
    'y_i': [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507, 4.775, 5.159, 5.683],
    '∆1y_i': [], '∆2y_i': [], '∆3y_i': [], '∆4y_i': []
}

# Вхідні дані
x1, x2 = 3.05, 3.52

# Дістаємо значення з таблиці
x_i, y_i = main_table['x_i'], main_table['y_i']
d1y_i, d2y_i, d3y_i, d4y_i = main_table["∆1y_i"], main_table["∆2y_i"], main_table["∆3y_i"], main_table["∆4y_i"]

# Крок
h = round(x_i[1] - x_i[0], 3)

# Функція для пошуку найближчого значення x_q
def count_x_q(x):
    global x_q
    if x <= x_i[int(len(x_i) / 2)]:
        for i in range(5, 0, -1):
            if x_i[i] >= x:
                x_q = x_i[i - 1]
                break
    else:
        for i in range(6, 12):
            if x_i[i] <= x:
                x_q = x_i[i + 1]
                break
    return x_q

# Функція для обчислення різниць Δx_i з додаванням нулів
def count_dx_i(dx_i, dx_i_prev):
    for i in range(1, len(dx_i_prev)):
        dx_i.append(round(dx_i_prev[i] - dx_i_prev[i - 1], 3))
    while len(dx_i) < len(x_i):
        dx_i.append(0)
    return dx_i

# Обчислення q:
x1_q = count_x_q(x1)
q_1 = round((x1 - x1_q) / h, 2)
x2_q = count_x_q(x2)
q_2 = round((x2 - x2_q) / h, 2)

# Обчислення ∆x_i:
d1y_i = count_dx_i(d1y_i, y_i)
d2y_i = count_dx_i(d2y_i, d1y_i)
d3y_i = count_dx_i(d3y_i, d2y_i)
d4y_i = count_dx_i(d4y_i, d3y_i)

print(f"∆1y_i: {d1y_i}\n∆2y_i: {d2y_i}\n∆3y_i: {d3y_i}\n∆4y_i: {d4y_i}\n")

# Формули інтерполяції Ньютона
def frst_Newton_interp_formula(h, q, d1y, d2y, d3y, d4y):
    # Обчислення y'(x)
    y1_x = 1 / h * (d1y[3] + ((2 * q - 1) / 2) * d2y[3] + ((3 * (q**2) - 6 * q + 2) / 6) * d3y[3] +
                    ((2 * (q**3) - 9 * (q**2) + 11 * q - 3) / 12) * d4y[3])
    
    # Обчислення y"(x)
    y2_x = 1 / (h**2) * (d2y[3] + (q - 1) * d3y[3] + ((6 * (q**2) - 18 * q + 11) / 12) * d4y[3])
    return y1_x, y2_x

def frst_Newton_interp_formula2(h, q, d1y, d2y, d3y, d4y):
    # Обчислення y'(x)
    y1_x = 1 / h * (d1y[5] + ((2 * q - 1) / 2) * d2y[5] + ((3 * (q**2) - 6 * q + 2) / 6) * d3y[5] +
                    ((2 * (q**3) - 9 * (q**2) + 11 * q - 3) / 12) * d4y[5])
    
    # Обчислення y"(x)
    y2_x = 1 / (h**2) * (d2y[5] + (q - 1) * d3y[5] + ((6 * (q**2) - 18 * q + 11) / 12) * d4y[5])
    return y1_x, y2_x

# Виведення таблиці
data_for_table = [list(main_table.keys())] + list(zip(main_table['i'], main_table['x_i'], main_table['y_i'], d1y_i, d2y_i, d3y_i, d4y_i))
print(tabulate(data_for_table, headers="firstrow", tablefmt="grid"))

# Виведення результатів
print(f"q_1: {q_1}, q_2: {q_2}")

# Інтерполяція для x1
if x1 <= x_i[int(len(x_i) / 2)]:
    y1_x1, y2_x1 = frst_Newton_interp_formula(h, q_1, d1y_i, d2y_i, d3y_i, d4y_i)
    print(f"y'({x1}): {round(y1_x1, 3)}\ny\"({x1}): {round(y2_x1, 3)}")

# Інтерполяція для x2
y1_x2, y2_x2 = frst_Newton_interp_formula2(h, q_2, d1y_i, d2y_i, d3y_i, d4y_i)
print(f"y'({x2}): {round(y1_x2, 3)}\ny\"({x2}): {round(y2_x2, 3)}")
