import numpy as np 

# --------------------------------------------------------------------------------------------
# np.arange([start], stop, [step], dtype=None)
# --------------------------------------------------------------------------------------------
# start default 0, step default 1

a = np.arange(5)  
b = np.arange(3,9)
c = np.arange(4,15,2)
d = np.arange(5,17,1,float)

print(a)
print(b)
print(c)
print(d)

# Print odd numbers from 5-17
odd = np.arange(5,18,2)
print(odd)

# --------------------------------------------------------------------------------------------
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# --------------------------------------------------------------------------------------------
# start and end included
# linspace generates evenly spaced numbers b/w start and end

a = np.linspace(0,10,5)
print(a)


arr, step = np.linspace(0, 14, num=5, retstep=True, dtype=int)  # will not able to give properly
arr, step = np.linspace(0, 14, num=5, retstep=True, dtype=float)  
print("Array:", arr)
print("Step size:", step)