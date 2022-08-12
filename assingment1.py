import numpy as np
import random
""" Problem Statement
1 Write a Python program to multiply an M * N matrix by N * A matrix and
create a real matrix product. """

print("\nQ1 START\n")
M = int(input("Enter value for m: "))
N = int(input("Enter value for n: "))
A = int(input("Enter value for a: \n"))

array_1 = np.random.random_sample((M, N))
print(array_1)

array_2 = np.random.random_sample((N, A))
print(array_2)

print(f"\nDot product of two arrays: ")

print(array_1.dot(array_2))

print("\nQ1 ENDS HERE\n")

""" Problem Statement
2: Write a NumPy program to check if each element of an array of your 
choice is composed of digits, lower case letters, and upper case letters only. """

print("Q2 STARTs \n")

lst = []
print("input like this : Python PHP JS Examples html5 5 -7")
lst = [item for item in input(f"\nEnter the list items with space to separate: ").split()]


array_3 = np.array(lst)
print("\nOriginal array:\n", array_3)
print(f"\nDigits only =", np.core.defchararray.isdigit(array_3))
print("Lower cases only =", np.core.defchararray.isupper(array_3))
print("Upper cases only =", np.core.defchararray.islower(array_3))

print("\nQ2 ENDS HERE\n")

""" Problem Statement
3: Write a program that reads two space-separated positive integers X and Y as input and perform the following tasks:
Tasks to be performed:
1. Create a list (lst1) starting at one (1) with 16 elements at a step of X
2. Create a list (lst2) starting at one (1) with 16 elements at a step of Y
3. Create two NumPy arrays np1 and np2 using lst1 and lst2 respectively
4. Reshape both the NumPy arrays to (4,4)
5. Create a new np array (np3) with values obtained by subtracting both the arrays (np1 - np2)
6. Print all the elements of np3 in a single dimension list like the 
format as shown below:
   a.[n0 n1 n2 n3 n4 n5 n6 n7 n8] """

print("Q3 STARTs \n")

st = []
st = [item for item in input(f"\nEnter two integer with space to separate: ").split()]
t = np.array(st, dtype=int)
print(t, "\n")
X = (t[0])
Y = (t[-1])
Z = 16

lst1 = []

for i in range(1, 1000, X):
    demo = i
    lst1.append(demo)
    if len(lst1) >= Z:
        break
print(lst1)

lst2 = []

for i in range(1, 1000, Y):
    demo = i
    lst2.append(demo)
    if len(lst2) >= Z:
        break
print(lst2, "\n")

np1 = np.array(lst1)
np2 = np.array(lst2)

e = np1.reshape(4, 4)
h = np2.reshape(4, 4)

print("\n", e)
print(h)

np3 = (e-h)
print(np3, "\n")

L = np3.flatten()
print(L, "\n")

print("\nQ3 ENDS HERE\n")

""" Problem Statement
4: Write a Python program that takes two integer-NumPy arrays, P and Q of shape [3∗3] and perform the following task:

Task to be performed:
Print the element-wise difference of the matrix P and Q (P−Q). """

print("Q4 STARTs \n")

# Either using input things I am just using random module

ll1 = []
for i in range(0, 9):
    n = random.randint(1, 30)
    ll1.append(n)
print(ll1)

ll2 = []
for i in range(0, 9):
    n = random.randint(1, 30)
    ll2.append(n)
print(ll2, "\n")

P = np.array(ll1).reshape(3, 3)
Q = np.array(ll2).reshape(3, 3)

print(P)
print(Q, "\n")

final = (P-Q)
print(final)

print("Q4 ENDS HERE\n")

print("END of ASSIGNMENTS-I")