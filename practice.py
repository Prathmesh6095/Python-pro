n1 = 0
n2 = 1
n = int(input("Enter a number: "))

if n == 1 and n < 1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(2, n):
         c = n1 + n2
         n1 = n2
         n2 = c
         print(c)