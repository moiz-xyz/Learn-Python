# operators 

# 1. Arithmetic Operators: +, -, *, /, //, %, **
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
# 5. Identity Operators: is, is not
# 6. Membership Operators: in, not in
# 7. Bitwise Operators: &, |, ^, ~, <<, >>
# 8. Ternary Operator: condition_if_true if condition else condition_if_false
# 9. Conditional Operator: (condition) ? (true_value) : (false_value)

# equal == 20
# not equal != 20
# greater than > 20
# less than < 20
# greater than or equal to >= 20
# less than or equal to <= 20

#logical operators 
country = "Pakistan"
city = "Karachi"

if country == "Pakistan" and city == "Karachi" :
    print("Youy are is Karachi , Pakistan")
else : 
    print ("You are not in karachi, Pakistan")
# OR operator 
country = "Pakistan"
city = "Lahore"
if country == "Pakistan" or city == "Karachi":
    print("You are in Pakistan or Karachi")
else:
    print("You are not in Pakistan or Karachi")

# not operator
country = "Pakistan"
city = "Karachi"
if not (country == "Pakistan" and city == "Karachi"):
    print("You are not in Karachi, Pakistan")
else:
    print("You are in Karachi, Pakistan")

# Identity Operators
# These check whether two variables refer to the same object in memory.

# Operator	Meaning	Example	Result
# is       True if both variables are the same object a is b	True/False
# is not   True if they are different objects a is not b	True/False

a = [1, 2, 3]
b = a          # b points to the same list as a
c = [1, 2, 3]  # c is a different list with same values

print(a is b)      # True  (same object in memory)
print(a is c)      # False (different objects)
print(a is not c)  # True

# Membership Operators

# These check if a value is present inside a sequence (string, list, tuple, etc.).

# | Operator | Meaning                      | Example              | Result |
# | -------- | ---------------------------- | -------------------- | ------ |
# | `in`     | True if value exists         | `'a' in 'apple'`     | True   |
# | `not in` | True if value does not exist | `'z' not in 'apple'` | True   |
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # True
print("mango" not in fruits)   # True
print("watermelon" in fruits)  # False

# Bitwise Operators
# These work at the binary level.

# | Operator | Name        | Example (binary of 5 → `0101`, binary of 3 → `0011`) | Result |          |                       |
# | -------- | ----------- | ---------------------------------------------------- | ------ | -------- | --------------------- |
# | `&`      | AND         | `5 & 3` → `0101 & 0011` → `0001` → **1**             |        |          |                       |
# | \`       | \`          | OR                                                   | \`5    | 3`→`0101 | 0011`→`0111\` → **7** |
# | `^`      | XOR         | `5 ^ 3` → `0101 ^ 0011` → `0110` → **6**             |        |          |                       |
# | `~`      | NOT         | `~5` → flips bits → **-6** (two’s complement)        |        |          |                       |
# | `<<`     | Left Shift  | `5 << 1` → `1010` → **10**                           |        |          |                       |
# | `>>`     | Right Shift | `5 >> 1` → `0010` → **2**                            |        |          |                       |
