
import pandas as pd

df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Marks": [85, 95, 75, 90, 80]
})

# Question : Sort them on basis of Marks then assign Roll accordingly?
df_sort = df.sort_values(by="Marks")
df_sort["Roll"] = [1,2,3,4,5]
print(df_sort)
# Problem is it will change the index order

# Use Rank Concept --> it will not change the index order
df["Rank"] = df["Marks"].rank()
print(df)

# -----------------------------------------------------------------------------------------
# Concept : Computing Numerical Ranks with df.rank() in Pandas
# -----------------------------------------------------------------------------------------
# 1. Purpose:
#    - Assigns numerical ranks (1 through N) to entries along an axis (default: down rows).
#    - By default, ranks are assigned in ASCENDING order (smallest value = rank 1).
#    - Use `ascending=False` for standard leaderboards (highest score = rank 1).
#
# 2. Syntax:
#    df.rank(
#        axis=0,              # 0 = rank down each column | 1 = rank across each row
#        method='average',    # How to assign ranks to tied values
#        numeric_only=False,  # True = rank only numeric columns
#        na_option='keep',    # How to handle NaN: 'keep', 'top', or 'bottom'
#        ascending=True,      # True = smallest is 1 | False = largest is 1
#        pct=False            # True = return percentile ranks (0.0 to 1.0)
#    )
#
# 3. Tie-Breaking Methods (`method` parameter) — Example scores: [100, 90, 90, 80] (descending):
#    - 'average' (default) : Assigns the average of the tied positions -> [1.0, 2.5, 2.5, 4.0]
#    - 'min'               : Standard Competition Ranking ("1224")       -> [1.0, 2.0, 2.0, 4.0]
#    - 'max'               : Modified Competition Ranking ("1334")       -> [1.0, 3.0, 3.0, 4.0]
#    - 'first'             : Ranks assigned in order of appearance       -> [1.0, 2.0, 3.0, 4.0]
#    - 'dense'             : Like 'min', but no gaps in rank numbers     -> [1.0, 2.0, 2.0, 3.0]
# -----------------------------------------------------------------------------------------
# * Note : Why Ranking comes in Float?
# As in Tie-Break it takes default Average --> so it always use float


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score":   [100,     90,    90,        80,      np.nan]
})

# -----------------------------------------------------------------------------------------
# 1. Comparing Tie-Breaking Methods (Highest Score = Rank 1 -> ascending=False)

df["rank_average"] = df["score"].rank(ascending=False, method="average")  # 1.0, 2.5, 2.5, 4.0
df["rank_min"]     = df["score"].rank(ascending=False, method="min")      # 1.0, 2.0, 2.0, 4.0
df["rank_dense"]   = df["score"].rank(ascending=False, method="dense")    # 1.0, 2.0, 2.0, 3.0
df["rank_first"]   = df["score"].rank(ascending=False, method="first")    # 1.0, 2.0, 3.0, 4.0

# -----------------------------------------------------------------------------------------
# 2. Percentile Ranking (pct=True) & Handling NaNs (na_option)

# na_option='bottom' pushes NaN to the lowest rank instead of leaving it as NaN
df["percentile"] = df["score"].rank(ascending=True, pct=True, na_option="bottom")

print(df)

# -----------------------------------------------------------------------------------------
# 3. Group-wise Ranking with groupby()

sales_df = pd.DataFrame({
    "dept":   ["Tech", "Tech", "Sales", "Sales"],
    "rep":    ["A",    "B",    "C",     "D"],
    "revenue":[500,    700,    400,     400]
})

# Rank employees within their own department
sales_df["dept_rank"] = sales_df.groupby("dept")["revenue"].rank(ascending=False, method="dense")
print("\nDepartment-wise Ranking:")
print(sales_df)