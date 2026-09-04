"""
==========================================
PYTHON NEWLINES (\n) & PRINT() BEHAVIOR 
==========================================
Core Concept:
- The print() function automatically adds a newline at the 
  end of your text by default (acting like end="\n").
- If you manually add "\n" inside your string, you will 
  create EXTRA blank lines!
"""

# ==========================================
# 1. NORMAL PRINT (NO MANUAL \n)
# ==========================================
# Concept: print() hits "Enter" automatically at the end.

print("\n--- 1. Normal Print ---")
print("hello")
print("world")
print()             # also add a line space
print()             # also add a line space
# Output:
# hello
# world


# ==========================================
# 2. NEWLINE INSIDE TEXT (hello\n)
# ==========================================

print("--- 2. Text with \\n ---")
print("hello\nworld")
print()             # also add a line space
print()             # also add a line space
# Output:
# hello
# <blank line>
# world


# ==========================================
# 3. PRINTING ONLY A NEWLINE ("\n")
# ==========================================

print("--- 3. Only \\n ---")
print("Line A")
print("\n") 
print("Line B")
# Output:
# Line A
# <blank line>
# <blank line>
# Line B