str = input("Enter a string: ")
letter = '$'
result = str[0] + str[1:].replace(str[0], letter)
print(result)