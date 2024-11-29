import matplotlib.pyplot as plt
import math

def euler_method():
   X, Y = [], []

   print("Euler's method")
   print("Enter a gap [a;b]")
  
   a = float(input("a = "))
   b = float(input("b = "))
   h = float(input("Step = "))
   Y.append(float(input(f"Start y({a})=")))
   n = int((b - a) / h)

   print("\nTable of values:")
   for i in range(n + 1):
       X.append(a + i * h)
       Y.append(Y[i] + h * (X[i] + math.sin(Y[i]/ math.sqrt(10))))
       print(f" {X[i]:.4f}\t{Y[i]:.4f}")


   plt.plot(X, Y[:-1], marker='o', linestyle='-', label='Eulers method')
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title('Graphing using the Euler method')
   plt.legend(fontsize=10)
   plt.show()
  
def euler_cauchy_method():
   X = []
   Y = []
  
   print("Euler-Cauchy method ")
   print("Enter a gap [a;b]")
  
   a = float(input("a = "))
   b = float(input("b = "))
   h = float(input("Step = "))
   Y.append(float(input(f"Start y({a})=")))
   X.append(a)
   n = int((b - a) / h) + 1
   print("\nTable of values:")
   for i in range(n+1):
       X.append(X[i] + h)

       y_temp = Y[i] + 0.1 / 2 * (X[i] + math.cos(Y[i] / 2.25) + X[i + 1] + math.cos((Y[i] + 0.1 * (X[i] + math.cos(Y[i] / 2.25))) / 2.25))
       Y.append(y_temp)
       print(f" {X[i]:.4f}\t{Y[i]:.4f}")
   plt.plot(X[:-1], Y[:-1], marker='o', linestyle='-', label='Euler-Cauchy method')
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title('Graph using the Euler-Cauchy method')
   plt.legend(fontsize=10)
   plt.show()

if __name__ == "__main__":
   euler_method()
   euler_cauchy_method()
