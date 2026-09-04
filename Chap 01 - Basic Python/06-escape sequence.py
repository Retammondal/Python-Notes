"""
=========================================================
PYTHON ESCAPE SEQUENCE CHARACTERS 
=========================================================
Core Concepts:
- Sequence of characters after backslash "\" are called Escape Sequence characters.
- These characters represent one special character inside strings.
"""

# ==========================================
# 1. NEWLINE (\n)
# ==========================================
# Concept: '\n' represents a newline. 
# It acts like pressing 'Enter', moving text from line 1 down to line 2.

print("--- 1. Newline (\\n) ---")
print("line 1\nline 2")
print("\n") # Adding an extra newline for clean output


# ==========================================
# 2. TAB (\t)
# ==========================================
# Concept: '\t' creates a Tab space.
# It is used to move the cursor forward, for example, creating a gap between 'A' and 'B'.

print("--- 2. Tab (\\t) ---")
print("A\tB")
print("\n")


# ==========================================
# 3. SINGLE QUOTE (\')
# ==========================================
# Concept: '\'' allows you to print a single quote character.
# Useful when your string is already enclosed in single quotes and you need an apostrophe.

print("--- 3. Single Quote (\\') ---")
print('It\'s going to be a great day!')
print("\n")


# ==========================================
# 4. BACKSLASH (\\)
# ==========================================
# Concept: '\\' allows you to print a literal backslash.
# Since a single backslash starts an escape sequence, you must use two of them to print just one.

print("--- 4. Backslash (\\\\) ---")
print("This is a backslash: \\")
print("\n")