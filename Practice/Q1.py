n = int(input("Enter a more than two digit: "))

sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10

if sum == n:
    print("It's an armstrong.")

else:
    print("It's not armstrong.")
