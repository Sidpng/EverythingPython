num=121
digit = 0
rem = 0
while(num>0):
    digit = num%10
    num= num/10
    rem = rem*10
if(rem == num):
    print("Palindrome")
else:
    print("Not Palindrome")