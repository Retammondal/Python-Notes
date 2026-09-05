# ord(character)      # Character --> Integer (Unicode)
# chr(Integer)        # Integer(Unicode) --> Character

print()
print(ord("A"))     # 65
print(ord("B"))     # 66
print(ord("C"))     # 67
print()

print(ord("a"))     # 97
print(ord("b"))     # 98
print(ord("c"))     # 99
print()

# In Unicode, Capital Letters come before Small letters
print(chr(97))     # 97
print(chr(98))     # 98
print(chr(99))     # 99
print()

# String Compare...
print("A" < "a")                # A will be smaller as based on Unicode --> True
print("Retam" < "Mondal")       # Compare will be on first character