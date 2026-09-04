"""
=========================================================
PYTHON WHILE LOOPS - NOTES & PRACTICE
=========================================================
⭐ PRO TRICK: First, think about the Condition! 
The condition will tell you what Initialization (state variable) 
you need. And NEVER forget the Updation step!

Anatomy of a While Loop:
1. Initialization
2. Condition ==> Needs to be 'True' to enter in Loop
3. Updation
"""

# ==========================================
# 1. THE BASIC WHILE LOOP (Counting)
# ==========================================
# Goal: Print "Hi" 7 times on the screen.

print("--- 1. Basic While Loop ---")

i = 1                   # 1. Initialization

while i <= 7:           # 2. Condition
    print(i, "- Hi")
    i = i + 1           # 3. Updation

    # If you don't update, the loop runs infinitely and crashes!

print("\n")


# ==========================================
# 2. WHILE LOOP FOR CONTINUOUS INPUT
# ==========================================
# Goal: A login screen that keeps asking until the user gets it right.

print("--- 2. Input While Loop ---")

realPassword = "Secret123@"
password = ""  # 1. Initialization

while password != realPassword:
# 2. Condition
# WHY NOT EQUAL (!=)? The loop only runs while the condition is TRUE.
# If they enter the wrong password, != evaluates to True (keep looping).
# Once they type "Secret123@", != evaluates to False (close loop, move forward).
    
    # 3. Updation (The user's input updates the variable directly!)
    password = input("Enter password: ") 
    
    if password != realPassword:
        print("Wrong Password ❌❌")

print("Access Granted! 😇😇\n")


# ==========================================
# 3. THE "WHILE TRUE" CHEAT SHEET
# ==========================================
# ⭐ CHEAT SHEET: When the condition feels too complex to set up, 
# just enter an infinite loop (while True) and use 'break' as an emergency exit!

print("--- 3. While True Pattern ---")

# Best Practice: Define constants outside the loop so they aren't recreated every cycle.
correct_password = "Secret123" 

while True:
    ask = input("Enter your Password: ")
    
    if ask == realPassword:
        print("Password Successful! 😇😇")
        break            # EMERGENCY EXIT: Breaks out of the loop immediately!
    else:
        print("Wrong Password....Try Again! ❌❌")

print("\n")