c1 = "Make a more money!"
c2 = "You won prize money!"
c3 = "Subscribe this!"

message = "You won prize money"
if(c1 in message or c2 in message or c3 in message):
    print("It's a scam.")

else:
    print("It's valid website. ")