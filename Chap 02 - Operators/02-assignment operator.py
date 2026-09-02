x=10 #if we write this it means we assigned value of 10 to x

#x+=2 #its a shortcut way to write x = x + 2

x+=12 # Will values to 22
x-=5 # Will values to 17
x*=2 # Will values to 34


# If you notice everytime it becaming new Numbers
x*=2 # Will values to 68
x/=5 # Will values to 13.6
x//=2 # Will values to 6; No! 6.0


    # ---------------------------------------------------------------------------
    # But the interesting fact is x became already float and upcoming ans will be in float
    # ---------------------------------------------------------------------------


x%=4 #Will come remainder as 2.0, now the value of updated x will be 2.0
print(type(x))
x=int(x)
x**=2
print(x)
print(type(x))