## Clock Analogy : outer loop sets the main pace, inner loop must run its entire
# cycle for every single step of the outer loop
for i in range(5):
  for j in range(3):
    print("i=",i,"j=",j)

print("\n")

# ==========================================
# Type Writer Rule
# ==========================================
# Terminals always print left-to-right, top-to-bottom.
# - Outer Loop = Controls the Rows (moving down line-by-line).
# - Inner Loop = Controls the Columns (typing left-to-right).
# - `print()`** = The Enter Key. 
#                 Placed inside the outer loop but 
#                 outside the inner loop 
#                 to drop the cursor down a line after completing a row.

# ==========================================
# Examples
# ==========================================
# Print this output
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for outer in range(4):
    for inner in range(5):
        print("*",end=" ")
    print()

print("\n")

# ==========================================
# Examples
# ==========================================
# Print this Output
# *
# * *
# * * *
# * * * *
# * * * * *
for outer in range(5):
    for inner in range(outer+1):        # wwhy outer+1 --> b/c range give 0-4
        print("*",end=" ")
    print()
## Dynamic Inner loops: instead of giving inner loops a fixed number,
# make it depends on outer loop variable

# ==========================================
# ⭐ Examples -- Floyd's Triangle
# ==========================================

##  Creating structure only(Floyd's Triangle)
# Print it
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = 1                                # The Data (The Bricks)
for row in range(1, 5):              # The Structure (The Blueprint)
    for col in range(1, row + 1):
        print(n, end=" ")            # Lay the brick
        n = n + 1                    # Prepare the next brick
    print()                          # Move to the next floor

print("\n")
# ==========================================
# Examples 
# ==========================================
# Print this:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for outer in range(1,6):
    for inner in range(1,outer+1):
        print(inner,end=" ")
    print()