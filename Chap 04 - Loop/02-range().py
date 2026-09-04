# range() function is a built-in integer number generator
#  It strictly accepts integers (using floats like range(1.0, 5.0))
# it creates a lazy iterable object --> convert to list/set to print

# range(start, stop, step)      
    # start defaults to 0 (Start)
    # step defaults to 1
# start included, stop excluded

# ------------------------------------------------------------------------------------------
#       range(start, stop, step)
#-------------------------------------------------------------------------------------------
# Range2to5 = range(2,5,1)
Range2to8 = set(range(2,8,1))
print(Range2to8)
Range2to8 = list(range(2,8,1))
print(Range2to8)
range2 = list(range(2,13,2))
print(range2)

#counting backwards
range4 = list(range(6,0,-1))
print(range4)
range5 = list(range(6,-1,-1))
print(range5)
range6 = list(range(30,16,-1))
print(range6)

print("-----------------------------")

# ------------------------------------------------------------------------------------------
#       range(start, stop)
#-------------------------------------------------------------------------------------------
# step by default to 1
range7 = list(range(5,19))
print(range7)

# ------------------------------------------------------------------------------------------
#       range(stop)
#-------------------------------------------------------------------------------------------
# range(5) --> will give you exact 5 numbers = 0,1,2,3,4
range8 = list(range(8))
print(range8)