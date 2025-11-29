# -------------------------------------
# PYTHON BASICS NEEDED FOR PANDAS
# -------------------------------------

# 1) Variables and Data Types
x = 10                   # int
pi = 3.14                # float
name = "Roshan"          # string
status = True            # boolean

# 2) Lists, Tuples, Dictionaries
marks = [10, 20, 30]     # list
coords = (12.5, 40.2)    # tuple
student = {              # dictionary
    "name": "Raju",
    "age": 25,
    "city": "Delhi"
}

# 3) Conditions (if/elif/else)
age = 21
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 4) Comparison & Logical Operators
a = 10
b = 20
print(a > b)             # False
print((a < b) and (b > 15))   # True

# 5) Loops
for m in marks:
    print("Mark:", m)

# 6) Functions (def)
def clean_text(text):
    return text.strip().lower()

print(clean_text("  HELLO "))

# 7) String Methods (important for Pandas)
s = "  PandaS Rock  "
print(s.lower())         # "  pandas rock  "
print(s.strip())         # "PandaS Rock"
print(s.replace(" ", "_"))  # "__PandaS_Rock__"

# 8) Import Modules
import pandas as pd
import numpy as np

# 9) Reading/Writing Files (Pandas)
# df = pd.read_csv("file.csv")
# df.to_csv("output.csv", index=False)

# 10) Error Handling
try:
    value = int("abc")
except:
    print("Conversion failed")

# 11) Basic Regex Example
import re
text = "Price: 250.00 INR"
match = re.search(r"(\d+\.?\d*)", text)
print(match.group())     # prints extracted number
