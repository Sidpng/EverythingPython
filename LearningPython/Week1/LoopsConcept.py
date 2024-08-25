number = 234343434
flag = 0
for i in range(2,number):
    if number%i==0:
        flag = 1
        break
    else:
        flag =0
if(flag == 1):
    print("Not prime")
else:
    print("Prime")
