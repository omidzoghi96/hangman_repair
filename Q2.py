import re

string = input("Enter your string: ")
b = re.findall(r'[A-Z][a-z]*', string)
for i in b:
    print(i, end=" ")
