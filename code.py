import math

print("**** Task 1 ****")

def first(x, X):
    return abs(x - X)/x

n1, x1 = 31, 5.56

X1 = math.sqrt(n1)
dx1 = first(x1, X1)
print(f"dx1 = {dx1}")

n2, N2, x2 = 13, 17, 0.764

X2 = n2/N2
dx2 = first(x2, X2)
print(f"dx2 = {dx2}")

answer = 0
print(f"sqrt({n1})  is more accurate" if dx1 < dx2 else f"{n2}/{N2}  is more accurate")
print("")
print("**** Task 2 a) ****")

x, dx, a, i = 3.6878, 0.0013, 0.5, 0

while dx < a/10:
    a /= 10; i += 1

fdx = round(dx + abs(round(x, i) - x), 4)

while fdx > a:
    i -= 1; a *= 10
    tmp = abs(round(x, i))
    fdx = round(dx + abs(round(x, i) - x), 4)

print(f"In rounded number x = {fdx} all numbers are true in the narrow sense ")
print("")
print("**** Task 2 b) ****")

x, sx = 15.873, 0.042

dx, er, i = x*sx/100, 1, 0  
if x > 9: i -= 1  
while dx < er: er /= 10; i += 1
er *= 10  

ndx = dx + abs(round(x, i) - x) 
while ndx < er:
    i -= 1  
    ndx = dx + abs(round(x, i) - x)  

print(f"In rounded number x* = {round(x, i)} all numbers are true in the broad sense ")
print("")
print("**** Task 3 a) ****")

x = 14.862
x2, i = x, 0

while int(x2) != x:  
    i += 1
    x, x2 = x*10, x2*10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10**i  
dx = (0.1/(10**i))*5 
sx = dx/x  
print(f"∆x = {dx}, σx = {sx} ({sx*100}%)")
print("")
print("**** Task 3 b) ****")

x = 8.73
x2, i = x, -1

while int(x2) != x:  
    i += 1
    x, x2 = x*10, x2*10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10**(i+1)  
dx = 0.1/(10**i)  
sx = dx/x  
print(f"∆x = {dx}, σx = {sx} ({sx*100}%)")
