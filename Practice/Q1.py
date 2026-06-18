yr = int(input("Enter a year: "))

if (yr % 400 == 0) and (yr % 100 == 0):
    print("It's  leap year")

elif (yr % 4 == 0) and (yr % 100 != 0):
    print("It's leap year")

else:
    print("It's  not leap year.")