number = int(input("Enter a number: "))
flag = 0
for i in range(2,number):
    if number%i==0:
        flag = 0
        break
    else:
        flag = 1

if flag == 1:
    print("Prime")
else:
    print("Composite")