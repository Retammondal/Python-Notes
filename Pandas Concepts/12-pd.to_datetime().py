# -----------------------------------------------------------------------------------------
# Concept : pandas.to_datetime()
# -----------------------------------------------------------------------------------------
# 1. Purpose:
#    - Converts various date/time representations (strings, epoch timestamps, integers)
#      into standard pandas `datetime64[ns]` objects (Timestamp or DatetimeIndex).
#    - Unlocks datetime-specific properties via the `.dt` accessor (e.g., .dt.year, .dt.day_name()).
#
# 2. Syntax:
#    pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, format=None, unit=None)
#
# 3. Critical Parameters:
#    - `format`: Explicit strftime format (e.g., "%Y-%m-%d"). Providing this skips format
#      inference and makes parsing up to 10x–20x faster.
#    - `errors`: How to handle unparseable dates:
#        'raise'  (default) : Raises a ValueError and crashes.
#        'coerce'           : Sets invalid values to `NaT` (Not-a-Time), pandas' null for datetimes.
#    - `dayfirst=True`: Solves ambiguity between DD/MM/YYYY and MM/DD/YYYY (e.g., "01/02/2024").
#    - `unit`: Time unit when converting Unix epoch integers/floats ('s', 'ms', 'us', 'ns').
# -----------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# Sample dirty real-world dataset
df = pd.DataFrame({
    "date_str": ["2024-01-15", "2024/02/20", "not_a_date", "2024-03-30"],
    "uk_date": ["12/01/2024", "15/02/2024", "01/03/2024", "25/04/2024"],                # DD/MM/YYYY
    "custom_format": ["15-Jan-2024", "20-Feb-2024", "10-Mar-2024", "05-Apr-2024"],
    "unix_timestamp": [1705315200, 1708425600, 1710067200, 1715313600]                  # Seconds since epoch
})


# 1. Handling Bad Data with errors='coerce'
# -----------------------------------------------------------------------------------------
# Converts strings to datetime; invalid values ("not_a_date") turn into NaT instead of crashing
df["clean_date"] = pd.to_datetime(df["date_str"], errors="coerce")


# 2. Ambiguous Dates: dayfirst=True
# -----------------------------------------------------------------------------------------
# "12/01/2024" is parsed as 12th Jan 2024 instead of 1st Dec 2024
df["uk_parsed"] = pd.to_datetime(df["uk_date"], dayfirst=True)


# 3. High Performance with Explicit `format`
# -----------------------------------------------------------------------------------------
# Faster and avoids guesswork: %d = day, %b = abbreviated month, %Y = 4-digit year
df["custom_parsed"] = pd.to_datetime(df["custom_format"], format="%d-%b-%Y")


# 4. Converting Unix Timestamps (unit='s')
# -----------------------------------------------------------------------------------------
df["epoch_parsed"] = pd.to_datetime(df["unix_timestamp"], unit="s")


print(df)
print(df.dtypes)

# 5. Extracting Components via the .dt Accessor
# -----------------------------------------------------------------------------------------
df["year"] = df["clean_date"].dt.year
df["month_name"] = df["clean_date"].dt.month_name()
df["day_name"] = df["clean_date"].dt.day_name()


print(df[["clean_date", "year", "month_name", "day_name"]])


# -----------------------------------------------------------------------------------------
# Concept : Why pd.to_datetime() Turns Valid Dates into NaT (Format Guessing)
# -----------------------------------------------------------------------------------------
# 1. How pandas Infers Date Formats:
#    - When no `format` argument is specified, pandas inspects the FIRST non-null valid date
#      to guess the pattern for the entire Series (e.g., "%Y-%m-%d" vs "%Y/%m/%d").
#    - In Pandas 2.0+, the parser is stricter for speed: it tries to find ONE consistent
#      format across the column.
#
# 2. What Happens with Mixed Delimiters ("-" vs "/"):
#    - Case A: If rows use DIFFERENT delimiters (some "-", some "/"), the inferred format
#      (e.g., "%Y-%m-%d") fails to parse the rows using "/" (e.g., "2024/02/20").
#    - With `errors='coerce'`, any row that does not conform to the chosen format
#      silently turns into `NaT`!
#
# 3. The Fix: `format='mixed'`
#    - Introduced in pandas 2.0+ specifically to handle columns containing mixed formats
#      or inconsistent delimiters without turning them into NaT.
# ----------------------------------------------------------------------------------------
# Solution : Use format=mixed to understand by Pandas



