import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Square Roots (Scalars and Arrays)
# --------------------------------------------------------------------------------------------
# Square Root of Scaler                 : np.sqrt(number)
# Want Square Root of this array        : np.sqrt(array)

print(np.sqrt(25))             

numbers = np.array([4,9,16,25])

sqrt_numbers = np.sqrt(numbers)
print(sqrt_numbers)            # [2. 3. 4. 5.] 
                               # But question is Why Float ? 
                               # -> Whenever there is possibility of Float 
                               # there will by default ans Float (Division, 
                               # SquareRoot)

print(sqrt_numbers.astype(int))# [2  3  4  5]


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Powers, Roots & Distance Formula
# --------------------------------------------------------------------------------------------
# Calculating distance from origin of these 3 points using powers and roots.
# Square Root   : np.sqrt(array)
# Cube Root     : np.cbrt(array)

x = np.array([3,5,8])          
y = np.array([4,12,15])

dist = np.sqrt((x-0)**2 + (y-0)**2)
dist = np.sqrt(x**2 + y**2)

x = np.array([3,5,8])

print(dist)
print(np.power(x,3))           # want cube
print(x**(1/3))                # want cube root (**1/3)
print(np.cbrt(x))


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Absolute Values
# --------------------------------------------------------------------------------------------
# np.abs() - want all numbers to convert to positive

y = np.array([-10,5,-6,0,9])
print(np.abs(y))               

# Normal Method (Without NumPy)
for i in range(len(y)):        
    if y[i] < 0:
        y[i] *= -1

print(y)


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Rounding, Floor, Ceil, and Truncate
# --------------------------------------------------------------------------------------------
# Round      --> Nearest Round                              : np.around(array,after decimal no.)
# Round Down --> nearest integer lesser than given number   : np.floor(array)
# Round Up   --> nearest integer greater than given number  : np.ceil(array)
# Tranculate --> Give only Integer Part                     : np.trunc(array)

values = np.array([10.2345, 20.6789, 30.4567])

print(np.around(values))       # [10. 21. 30.] -- will give nearest round
print(np.around(values,2))     # [10.23 20.68 30.46] -- nearest round upto 2 decimal

print(np.floor(values))        # [10. 20. 30.]
print(np.ceil(values))         # [11. 21. 31.]

# --------------------------------------------------------------------------------------------
values = np.array([2.9, 5.7, -3.9, -7.2])

print(np.floor(values))        # Give the integer part only? But the problem is 
                               # for Negative numbers the Floor will give 
                               # lower(Problematic)

print(np.trunc(values))        # (np.trunc solves this by just chopping off 
                               # the decimals entirely!)