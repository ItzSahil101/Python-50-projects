import re

condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
userEmail = input("Enter Your Emai: ")

if re.search(condition, userEmail):
    print("Right Email")
else:
    print("Wrong Email")