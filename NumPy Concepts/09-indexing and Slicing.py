print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Indexing & Accessing Elements
# --------------------------------------------------------------------------------------------
marks_1d = np.array([10, 15, 48, 69, 63])

print(marks_1d[2])             # Indexing in NumPy Array... we can get Elements using
print(marks_1d[-2])            # Index (Zero + Negative Index)

marks_2d = np.array([
    [78, 85, 90, 88],
    [76, 74, 85, 90],
    [88, 76, 70, 85],
    [90, 88, 76, 68],
    [85, 90, 88, 76],
    [78, 85, 90, 88]
])

print(marks_2d[3][2])          # How to Extract an Element from a 2D Array: Method 1 
                               # (Standard Python)
print(marks_2d[3, 2])          # Method 2 (Numpy Method - Preferred). For 1D array only 
                               # one Index was needed, but for 2D we need 2 index 
                               # (row, column). NOTE : Here row, column both can be 
                               # Zero Indexed + Negative Indexed

print(marks_2d.shape[0])       # Extracting specific shape data: No. of Students -> rows
print(marks_2d.shape[1])       # No. of Subjects -> no. of columns

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 1-D Slicing
# --------------------------------------------------------------------------------------------
matrix1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(matrix1d[2:5])           # 1-D -> [start : stop : step]
print(matrix1d[::])

print(matrix1d[::2])           # Give even indexed elements only / alternate
print(matrix1d[1::2])          # Give odd indexed elements only / alternate
print(matrix1d[::-1])          # Give all elements backwards / Reverse Order

print(matrix1d[-3:-1:-1])      # Give last 3 items in reverse order. NO []
print(matrix1d[-1:-4:-1])

print(matrix1d[-5:-1])         # Note : Negative index elements will still go rightside, 
                               # indexing is only leftside without step
print(matrix1d[-1:-5])         # No data will come (needs negative step to go left)

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 2-D Slicing
# --------------------------------------------------------------------------------------------
student_marks = np.array([
    [70, 80, 90, 85],
    [60, 75, 85, 88],
    [88, 92, 95, 90],
    [65, 70, 80, 75]
])

print(student_marks[:, 1:3])   # 2-D -> Slicing: [row_start:row_end:step, col_start:
                               # col_end:step]. Extract all rows, but only columns 
                               # from index 1 up to (but excluding) 3

print(student_marks[:2])       # Give data of first 2 Students --> 2 Rows
print(student_marks[:3, :2])   # want 1st two column data of first 3 students
print(student_marks[:3, -2:])  # want last two column data of first 3 students

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Mathematical Operations & Updating Arrays (Broadcasting)
# --------------------------------------------------------------------------------------------
print(student_marks[:3, -2:] + 5)                      # Mathematical operation of sliced
                                                       # part. Not Update
student_marks[:3, -2:] = student_marks[:3, -2:] + 5    # Update the Real One
print(student_marks)

marks_1d += 5                  # We want to give 5 bonus marks to all students 
                               # (This is called 'Broadcasting' in NumPy)
print(marks_1d)

marks_1d[2] += 5               # We want to give 5 more bonus marks to 3rd Student -> 
                               # Index 2. We can update any Particular element of Array 
                               # using Index instead of all
print(marks_1d)

# --------------------------------------------------------------------------------------------
# Question :  Real World / Logic Examples
# --------------------------------------------------------------------------------------------
sales = np.array([             # How we can use Sales data in NumPY 2d array
    [125000, 148000, 135000, 172000],       # Year 2024 quarterwise data
    [100000, 148000, 130000, 160000]        # Year 2025 quarterwise data
])

print(sales.shape)             # (2,4) -> 2 Rows, 4 Columns

def diagEle(input_array):      # Question : Print all the diagonal elements of the 2d
                               # numpy array
    row, column = input_array.shape       # Tuple Unpacking

    if row < column:
        count = row 
    else:
        count = column
        
    print("\nDiagonal Elements :", end=" ")
    for i in range(count):
        if i == (count-1):
            print(input_array[i, i])
        else:
            print(input_array[i, i], end=" ")

diagEle(marks_2d)

# print(np.diag(marks_2d))     # (Bonus Concept added: NumPy actually has a built in 
                               # function to do what you just coded!)