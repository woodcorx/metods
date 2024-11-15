def F(x):
    return 3 * x**4 - 4 * x**3 + x**2 - 2 * x - 5

def dF(x):
    return 12 * x**3 - 12 * x**2 + 2 * x - 2

def main_newton():
    print("Розв'язання нелінійного рівняння методом Ньютона:")
    print("Рівняння: 3x^4 - 4x^3 + x^2 - 2x - 5 = 0")

    # Ввод значений
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    e = float(input("Введіть ε: "))

    if a > b:
        a, b = b, a

    print("Корені:")

    x = a  
    i = 0  
    while x <= b:
        y1 = F(x)
        y2 = F(x + e * 100)
        
        if (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0):
            i += 1
            x1 = x  
            q = abs(x1 - F(x1) / dF(x1))
            
            while q > e:
                x2 = x1 - F(x1) / dF(x1)
                q = abs(x1 - x2)
                x1 = x2
            print(f"x{i} = {round(x1, 4)}")
            
        x += e * 100  

def f(x):
    return 3 * x ** 4 - 4 * x ** 3 + x ** 2 - 2 * x - 5

def main_bisection():
    print("Розв'язання нелінійного рівняння методом бісекції:")
    print("Рівняння: 3*x^4 - 4*x^3 + x^2 - 2*x - 5 = 0")

    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))


    if a >= b:
        print("Коренів у вказаному інтервалі немає.")
        return

    t = float(input("Введіть ε: "))

    p1 = a
    p2 = b
    p = (p1 + p2) / 2

    if f(p1) * f(p2) > 0:
        print("Коренів у вказаному інтервалі немає.")
        return

    while abs(f(p)) > t:
        if f(p1) * f(p) < 0:
            p2 = p  
        else:
            p1 = p  

        p = (p1 + p2) / 2 

    print(f"Корінь x2 = {round(p, 4)}")

while True:
    choice = input("Виберіть метод (Ньютон/Бісекція): ").strip().lower()
    if choice == "ньютон":
        main_newton()
    elif choice == "бісекція":
        main_bisection()
    else:
        print("Неправильний вибір. Виберіть 'Ньютон' або'Бісекція'")
