string = input("Enter the string: ")
char = input("Enter the character: ")
index = -1
for i in range(len(string)):
    if string[i] == char:
        index = i
        break
if index != -1:
    print(f"{char} is found at index: {index}")
else:
    print(f"{char} is not found in the string")
