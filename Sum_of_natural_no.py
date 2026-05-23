n = int(input("Enter a number: "))

if n <0:
    print("Invalid choice. Enter +ve number.")

else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1

        print(sum)