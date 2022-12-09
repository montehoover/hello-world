# Parse something like "3 cm" or "1.5 m" and return the value in millimeters.
import re

str = "3 cm"

# Regexes you're interested in:
numbers = "[0-9]+"    # Use "+" to require at least some numbers
whitespace = "\s?"    # Use "?" to make the whitespace optional
letters = "[a-zA-Z]*" # Use "*" to make letters optional

# Use your regexes. Use parentheses to capture groups that you're interested in:
m = re.search(f"({numbers}){whitespace}({letters})", str)
value = int(m.groups()[0])
units = m.groups()[1].lower()

# Now do whatever you want with this:
print(f"Number: {value}, Units: {units}")
if units == "mm" or units == "":
    print(f"{value} mm")
elif units == "cm":
    print(f"{value * 10} mm")
elif units == "m":
    print(f"{value * 1000} mm")