number = int(input("Enter a number to check whether even or odd: "))
if(number%2==0):
    print("Number provided by you ", number, "is even.")
elif(number%2!=0):
    print("Number provided by you ", number, "is odd.")
else:
    print("Number provided by you ", number, "is neither even nor odd. Please check and retry")