# ------------------------------------------------------------------------------------------
#       Variables --> Storage Bins
#-------------------------------------------------------------------------------------------

# Variable is kind of storage container
# Writing name = Retam instead of name = "Retam". Without quotes, Python looks for a variable named Retam.
name="RETAM"
city="Mallickpur"
print(name)
print(city)
print("-------------")
# -----------------------------------------
laptop = "Desktop with i3 9th Generation"
print("First Laptop:",laptop)
#------------------------------------------
# Variable takes the latest data
laptop = "Asus Vivobook S14"
print("Latest Laptop:", laptop)


# Variable name must start with _ 
# Variable name can't start with Number(3), contain spaces, special char.

# Prefer snake_case for Name convention

print("---------------------------------------------------------")
# ------------------------------------------------------------------------------------------
#       Data Types
#-------------------------------------------------------------------------------------------
age = 23                    # Integer
mark = 96.5                 # Float
name = "Retam"              # String
is_market_open = False      # Boolean (True/ False)
data = None                 # None , null values (None)

# data = false              # not applicable , case Sensitive
new_mark = "99"             # Number ❌, String ✅

## type
print(type(new_mark))
print(type(is_market_open))