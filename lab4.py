import math

def f1(x):
   return 1 / math.sqrt(0.5 * x + 2)

def f2(x):
   return (x**2 * math.log10(x))

def f3(x):
   return 1 / math.sqrt(x**2 + 1.2)

def left_s(a, b, n, func):
   s = 0
   x = a
   h = (b - a) / float(n)
   for i in range(n):
       s += func(x)
       x += h
   s *= h
   return s

def right_s(a, b, n, func):
   s = 0
   h = (b - a) / float(n)
   x = a + h
   for i in range(1, n + 1):
       s += func(x)
       x += h
   s *= h
   return s

def mid_s(a, b, n, func):
   s = 0
   x = a
   h = (b - a) / float(n)
   for i in range(n):
       s += func(x + h / 2)
       x += h
   s *= h
   return s

def simpson_integration(a, b, n, func):
   s = 0
   s1 = 0
   s2 = 0
   h = (b - a) / float(n)
   x = a + h

   for i in range(1, n, 2):
       s1 += func(x)
       x += 2 * h

   x = a + 2 * h

   for i in range(2, n, 2):
       s2 += func(x)
       x += 2 * h

   s += func(a) + func(b) + s1 * 4 + s2 * 2
   s *= h / 3
   return s

def trapezoidal_integration(a, b, n, func):
   h = (b - a) / float(n)
   result = (func(a) + func(b)) / 2.0

   for i in range(1, n):
       result += func(a + i * h)

   result *= h
   return result

if __name__ == "__main__":
   print("\nThe method of rectangles")
   a1 = float(input("a = "))
   b1 = float(input("b = "))
   n1 = int(input("Enter the number of division segments n = "))

   print(f"Integration of a function f1(x) on the interval [{a1};{b1}]")

   print("With the left-hand rectangles method:")
   print(f"S = {left_s(a1, b1, n1, f1):.4f}")

   print("With the right-hand rectangles method:")
   print(f"S = {right_s(a1, b1, n1, f1):.4f}")

   print("With the mid-square method:")
   print(f"S = {mid_s(a1, b1, n1, f1):.4f}")

   print("\nThe Simpson's method")
   a2 = float(input("a = "))
   b2 = float(input("b = "))
   n2 = int(input("Enter the number of division segments n = "))

   print(f"Integration of a function f2(x) on the interval [{a2};{b2}]")

   result = simpson_integration(a2, b2, n2, f2)
   print(f"With Simpson's method:")
   print(f"S = {result:.4f}")

   print("\nThe method of trapezoids")
   a3 = float(input("a = "))
   b3 = float(input("b = "))
   n3 = int(input("Enter the number of division segments n = "))

   print(f"Integration of a function f3(x) on the interval [{a3};{b3}]")

   result = trapezoidal_integration(a3, b3, n3, f3)
   print(f"With the method of trapezoids:")
   print(f"S = {result:.4f}")
