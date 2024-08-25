vowels = ["A", "E", "I", "O", "U"]
flag = 0
userInput = input("Enter a character to check whether its a vowel or consonant")
print(userInput.upper())
if userInput.upper() in vowels:
    print("The character: ", userInput, "is a vowel")
else:
    print("The character: ", userInput, "is a consonant")