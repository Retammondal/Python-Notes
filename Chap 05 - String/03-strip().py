
# -------------------------------------------------------------------
# Strip -- What it does?
# -------------------------------------------------------------------
# Strip only works in Absolute start and end; not in middle.

# 1. Removing standard whitespace and newlines; not from middle
msg = "   \n  Hello \nWorld!   \t \n"
print(msg)
print(msg.strip())  
# Output: "Hello World!"

# 2. Removing specific characters
symbols = "...!!!Hello World!!!"
print(symbols.strip(".!"))  
# Output: "Hello World"

# 3. Stripping out-of-order characters
website = "://example.com"
print(website.strip("cmw."))  
# Output: "://example.o" (because 'o' was not in the removal set, it stopped there)

# -------------------------------------------------------------------
# Strip -- What it does not?
# -------------------------------------------------------------------
# 1. Middle spaces are ignored
text = "   Python   is   fun   "
print(text.strip())  
# Output: "Python   is   fun" (Middle spaces remain untouched!)

# 2. It doesn't match sequences perfectly
word = "banana"
print(word.strip("an"))  
# Output: "b" (It stripped 'a' and 'n' from the edges until only 'b' was left)
word1 = "ananaB Shake contain banana"
print(word1.strip("an"))  

