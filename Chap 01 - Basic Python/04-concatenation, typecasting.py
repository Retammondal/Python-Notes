# ------------------------------------------------------------------------------------------
#       Concatenation vs Addition
#-------------------------------------------------------------------------------------------
# Mathematical Addition (Int/Float + Int/Float): Sums values mathematically.
# String Concatenation (String + String): Acts like glue, stitching the text ends together.

print(3+5)
print(5.4+5)
# print("Reta" + 45)        # Not Possible
print("Retam" + " " + "Mondal")

# ------------------------------------------------------------------------------------------
#       Type Casting
#-------------------------------------------------------------------------------------------

age = "20"
newAge = int(age)  #By this was you are making the String to Integer
print(type(age))
print(type(newAge))

#-------------------------------------------------------------------------------------------
# Ques : Take length and breadth of the Rectangle as input and print its area
#-------------------------------------------------------------------------------------------

length=float(input("Enter the length:"))
breadth=float(input("Enter the Breadth:"))
    # WHY Not Int()?
    # If you input any decimal number it will give error, length and breadth
    # doesn't need to be integer always
area=print("Area =",length*breadth)