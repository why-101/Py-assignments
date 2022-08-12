import math as m
# 1. Write a code to interchange first and last elements in a list
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(dir(list_1))
print(list_1)
print(list_1[::-1])

# OR

list_1[0], list_1[-1] = list_1[-1], list_1[0]
print(list_1)

# we can also use pop() and insert() method to do this

""" 2. Write a code to generate a list with key values ranging from 1 to N and
# corresponding values as n**2 where N is a user input no. amd n is the
# respective key:
# Ex if N = 10 then dictionary should look like:
# { 1: 1, 2:4, 3: 9, 4:16, 5:25, 6:36, 7 : 49, 8: 64, 9:81, 10:100} """

N = int(input("Enter the range number for square: "))
key = list(range(1, N + 1))
print(key)

# making values
value = []
for i in range(0, len(key)):
    value.append(key[i] * key[i])

# printing resultant list
print(value)

# using dictionary comprehension
# to convert lists to dictionary
res = {key[i]: value[i] for i in range(len(key))}

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

""" 3. A number is a perfect number if is equal to sum of its proper divisors,
that is, sum of its positive divisors excluding the number itself. Write a
function to check if a given number is perfect or not. """

def positive_int():
    j = []
    for i in key:
        if N % i == 0:
            j.append(i)
            i = i + 1
    print(j)
    f = j[0:-1]
    d = sum(f)
    print(d)
    if d == N:
        print("integer is perfect")
    else:
        print("integer is not perfect")
positive_int()


""" 4. find factorial of a number :: 6! = 6 *5*4*3*2*1
n! = n * (n-1) * ( n- 2)....... ( n- (n-1)) """

print(m.factorial(N))

""" Prime numbers : numbers which are divisible by only 1 & itself only if the number is
divisible by any other number other than 1 & itself then it is non prime
a. check whether a number is prime or not
b. from a vector of numbers identify all the prime numbers
c. create a vector of all the prime numbers in between 2000 and 3000
d. create a vector of first 50 prime numbers """

i = 2000
while i < 3000:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > (i / j):
        print(i, "is prime number")
    i = i + 1
print("Good bye!")

i = N
while i < 50:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > (i / j):
        print(i, "is prime number")
    i = i + 1
print("Good bye!")
