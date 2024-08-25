class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Divided by 0 is not possible, please enter some other number")

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

choice = input("Which operation do u want to execute: + - / *")

my_run = Calculator(num1,num2)
if choice == "+":
    print(my_run.addition())
elif choice == "-":
    print(my_run.subtraction())
elif choice == "*":
    print(my_run.multiplication())
elif choice == "/":
    print(my_run.division())