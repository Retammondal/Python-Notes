# if, else --> Checks Condition True or, False to run inside codes
# Indentation --> Inside; 
# ------------------------------------------------------------------------------------------
#       Else Trap
#-------------------------------------------------------------------------------------------

marks = 40

if marks < 30:
    print("Low Marks")  # Triggers!
if marks >= 30:
    print("Medium Marks")
if marks >= 70:
    print("High Marks")
else:
    print("Default Fail")  # Triggers!

# 1st, 2nd, 3rd if works independently
# last else only works on basis of 3rd if statement

# ------------------------------------------------------------------------------------------
#       Nested If
#-------------------------------------------------------------------------------------------
if marks < 30:
    print("Low Marks")
else:
    if marks < 70:
        print("Medium Marks")
    else:
        print("High Marks")

# ------------------------------------------------------------------------------------------
#       Else If
#-------------------------------------------------------------------------------------------
# Syntax
# Elif
if 2>3:
  print("A") # Runs if condition_1 is True
elif 5<4:
  print("B") # Runs if condition_1 is False AND condition_2 is True
elif 10>9:
  print("C") # Runs if prior conditions are False AND condition_3 is True
else :
  print("D") # Runs if ALL conditions above are False

# Practice
if marks < 30:
    print("Low Marks")
elif marks < 70:
    print("Medium Marks")
else:
    print("High Marks")

# ------------------------------------------------------------------------------------------
#       Ironclade Rules of if
#-------------------------------------------------------------------------------------------
#   1.  Every Different "if" works Differently..
#   2.  "elif" > works only when "if" fails
#   3.  "else" > works only when all "if" & "elif" fails