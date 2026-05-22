# Check the number is prime or not.
n = int(input("Enter a number: "))

if n ==1:
    print("invalid choice.")
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime.")
            break
    else:
            print("It's prime.")