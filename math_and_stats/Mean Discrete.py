# Simple program that can perform mean in Discrete series

try:
    x = int(input("Enter the number of X elements: "))
except ValueError:
    print("INVALID, USE ONLY INTEGER")
    exit()

l = []
for i in range(x):
    try:
        n = int(input("Enter the X element: "))
        l.append(n)
    except ValueError:
        print("INVALID, USE ONLY INTEGER")
        exit()

try:
    y = int(input("Enter the number of Y elements: "))
except ValueError:
    print("INVALID, USE ONLY INTEGER")
    exit()

J = []
for i in range(y):
    try:
        n = int(input("Enter the Y element: "))
        J.append(n)
    except ValueError:
        print("INVALID, USE ONLY INTEGER")
        exit()

# Ensure the lengths of l and J are the same
if len(l) != len(J):
    print("The number of X and Y elements must be the same.")
    exit()

M = []
sum_xy = 0
for i in range(len(l)):
    mux = l[i] * J[i]
    M.append(mux)
    sum_xy += mux

print("The Elements of X are:", l)
print("The Elements of Y are:", J)
print("The Summation of XY is:", sum_xy)

# Calculate the mean
sum_y = sum(J)
if sum_y == 0:
    print("Cannot calculate mean because the sum of Y is zero.")
else:
    mean = sum_xy / sum_y
    print("Mean is:", mean)

