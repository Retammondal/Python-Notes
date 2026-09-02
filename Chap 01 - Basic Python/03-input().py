# ------------------------------------------------------------------------------------------
#       Input()
#-------------------------------------------------------------------------------------------

name = input("Enter your name:")
print(name)

# Ques : Take two int as input from the user and print their sum
# ------------------------------------------

int1 = int(input("Enter 1st Integer:"))
int2 = int(input("Enter 1st Integer:"))

# print(int1+int2) WRONG!!!! Why? => input always gives value as a String; and + concatenates two strings
print(int1+int2)

