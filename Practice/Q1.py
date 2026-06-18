n = int(input("Enter a number: "))

if n==1:
    print("Invalid choice")

elif n>1:
    for i in range(2, n):
        if n%i==0:
            print("Not prime")
            break

    else:
        print("It's Prime")
        