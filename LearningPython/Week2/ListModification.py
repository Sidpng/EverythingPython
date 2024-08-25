numbers = [10, 20, 30, 40, 50]
print("Original list", numbers)
numbers[2] = 100
print("Modified list", numbers)
colors = ["red", "green", "blue"]
print(colors)
#Adding new items in the list
colors.append("yellow")
colors.insert(0, "purple")
print(colors)
colors.remove("green")
print(colors)
#Slicing
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Numbers[0:4])
print(Numbers[-3:])
numbersNew = [5, 10, 15, 20, 25, 30, 35, 40]
print(numbersNew[2:5])
print(numbersNew[-6:-3])
print(numbersNew[6:3:-1])