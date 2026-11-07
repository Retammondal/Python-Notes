# -----------------------------------------------------------------------------------------
# Concept : Vectorized String Operations (.str Accessor) & Method Chaining in Pandas
# -----------------------------------------------------------------------------------------
# 1. Vectorization via `.str` Accessor:
#    - Python strings are immutable; modifying strings row-by-row via standard loops or `.apply()`
#      incurs heavy Python-level overhead and memory re-allocation.
#    - The `.str` accessor exposes native Python string methods (and regex tools) directly to
#      an entire Series or Index at once.
#    - Under the hood, operations run in optimized C-level vectorized code, delivering massive
#      speedups and handling missing values (`NaN`) gracefully without crashing.
#
# 2. Method Chaining:
#    - Each `.str` method call produces a new Pandas Series.
#    - Because the return type is a Series, subsequent string operations require re-invoking `.str`
#      prior to each successive string method:
#          series.str.strip().str.lower().str.replace(...)
#    - Wrapping chained operations inside parentheses `(...)` enables clean multi-line formatting
#      without requiring backslashes (`\`).
#
# 3. Automatic NaN Handling:
#    - Unlike plain Python (where `"hello" + None` raises a TypeError), `.str` methods
#      propagate `NaN` safely: `np.nan` values remain `NaN` rather than crashing the pipeline.
# -----------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# Sample dirty real-world dataset
df = pd.DataFrame({
    "student_id": [101, 102, 103, 104],
    "raw_name": ["  aLiCe smITh  ", "BOB_JONES  ", np.nan, "  chArLie-BROWN "]
})

# -----------------------------------------------------------------------------------------
# Example: Cleaning & standardizing names with Method Chaining
# Goal: Strip whitespace -> Replace delimiters ('_', '-') with spaces -> Title Case
# -----------------------------------------------------------------------------------------

# Pythonic multi-line chaining using outer parentheses:
df["clean_name"] = (
    df["raw_name"]
    .str.strip()                                    # 1. Remove leading/trailing spaces
    .str.replace(r"[_-]", " ", regex=True)          # 2. Standardize delimiters to a space
    .str.title()                                    # 3. Capitalize first letter of each word
)
print(df)

# Extracting components: Splitting into first and last name
df[["first_name", "last_name"]] = (
    df["clean_name"]
    .str.split(" ", n=1, expand=True)               # expand=True turns output into DataFrame columns
)
print(df)

# Boolean filtering using .str accessor (e.g., starts with specific letter)
# na=False ensures missing/NaN rows don't cause filtering errors
a_students = df[df["clean_name"].str.startswith("Alice", na=False)]

print(a_students[["student_id", "clean_name"]])



# -----------------------------------------------------------------------------------------
# Essential Pandas .str Cheat Sheet (Most Used in Data Cleaning)
# -----------------------------------------------------------------------------------------

# 1. Cleaning & Formatting
s.str.strip()                                 # Remove leading/trailing spaces
s.str.lower()                                 # Standardize to lowercase
s.str.title()                                 # Title Case (e.g., "John Doe")

# 2. Replacing
s.str.replace("old", "new")                   # Simple text replacement
s.str.replace(r"\s+", " ", regex=True)        # Regex: collapse multiple spaces to one

# 3. Filtering / Conditions (Na-safe for df[mask])
s.str.contains("keyword", case=False, na=False)  # Substring check (case-insensitive)
s.str.startswith("prefix", na=False)             # Starts-with check

# 4. Splitting into Columns
s.str.split(" ", n=1, expand=True)            # Split once into multiple DataFrame columns

# 5. Extracting via Regex
s.str.extract(r"(\d+)")                       # Extract first regex match into a column

# 6. Slicing & Length
s.str.len()                                   # Get character length of strings
s.str[:3]                                     # Get first 3 characters