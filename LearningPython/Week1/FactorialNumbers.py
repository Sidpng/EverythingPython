number = int(input("Enter a number to find its factorial: "))
def factorialFinder(num):
    if(num == 0):
        return 1
    else:
        print(num*factorialFinder(num-1))
        return num*factorialFinder(num-1)

print("Factorial of the number: ",number, "is: ",factorialFinder(number))
