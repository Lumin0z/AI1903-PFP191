#Q3 Write a program that performs the following tasks: 1.Input 4 real numbers a, b, c, and x
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
x = float(input("Enter the value of x: "))

# 2.Calculate S1 = ax^2 + bx + c
S1 = a * x**2 + b * x + c
print("S1 =", S1)

# 3.Calculate S2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    S2 = a * c * (b**2 - 4) / (b**2 - 4*a*c)
else:
    S2 = 0
print("S2 =", S2)

# 4.Re-input a, b, and c
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# 5.Check whether a, b, and c are sides of a triangle
if a + b > c and a + c > b and b + c > a:
    print("a, b, and c are sides of a triangle.")
    perimeter = a + b + c
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Perimeter:", perimeter)
    print("Area:", area)
else:
    print("a, b, and c are not sides of a triangle.")
    
#Q4 Write a program to accept 3 real numbers a, b, c, then: 1.Input 3 real numbers a, b, c.
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# 2.Display the maximum and minimum values among them.
max_value = max(a, b, c)
min_value = min(a, b, c)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Arrange them in ascending order, i.e. a ≤ b ≤ c.
sorted_values = sorted([a, b, c])
print(f"Values in ascending order: {sorted_values}")