# Python program to print Fibonacci series 
a = 0
b = 1
n = int(input("Enter a number: "))

if n == 1 and n < 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
         c = a + b
         a = b
         b = c
         print(c)