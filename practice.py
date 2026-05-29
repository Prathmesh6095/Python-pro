x = 13;
y = 12;

temp = x;
print("Value of temp variable is", temp)

x = y;
print("Value of x is", x)

y = temp
print("The value of y is", y,"\n",)

print("The second method is: ")
# Method 2 - Without using third variable
x = 12
y = 13

x,y = y,x;

print("The value of x", x)
print("The value of y", y)
