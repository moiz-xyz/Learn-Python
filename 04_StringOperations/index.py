#String operations

#01 String Concatenation:
firstName = "Ali"
lastName = "Ahmed"
fullName = firstName + " " + lastName

print(fullName)

#Strings are immutable means they cannot be changed  after they arec created

#2 Strings length 
# The length of a string can be determined using the len() function.
string = "Hello world"
length = len(string)

print ("Length of " + string + " is" ,length)

#3 String slicing 
# Slicing allows you to extract a portion of a string.
string = "Hello world again"
sliced_Again = string [12:17]
print("slicing again from hellon world " , sliced_Again)

# 4. String Formatting:
# String formatting allows you to create formatted strings using placeholders.
name = "John Ellia"
age = 90
formatted_string = f"My name is {name} and I'm {age} years old"

# String Methods:
# There are various built-in methods available for string manipulation.

# 1. upper(): Converts all characters to uppercase.
city = "lahore"
print(city.upper() ) #LAHORE

# 2. lower(): Converts all characters to lowercase.
city = "LAHORE"
print(city.lower())  # Output: lahore

# 3. title(): Converts the first character of each word to uppercase.
city = "lahore city"
print(city.title())  # Output: Lahore City

# 4. capitalize(): Converts the first character of the string to uppercase.
city = "lahore"
print(city.capitalize())  # Output: Lahore

# 5. strip(): Removes leading and trailing whitespace.
city = "   lahore   "
print(city.strip())  # Output: lahore

# 6. lstrip(): Removes leading whitespace.
city = "   lahore   "
print(city.lstrip())  # Output: "lahore   "

# 7. rstrip(): Removes trailing whitespace.
city = "   lahore   "
print(city.rstrip())  # Output: "   lahore"

# 8. replace(old, new): Replaces occurrences of a substring with another substring.
city = "lahore"
print(city.replace("lahore", "karachi"))  # Output: karachi

# 9. split(separator): Splits the string into a list of substrings based on the separator.
city = "lahore,karachi"
print(city.split(","))  # Output: ['lahore', 'karachi']

# 10. join(iterable): Joins elements of an iterable (like a list) into a single string.
city_list = ["lahore", "karachi"]
print(", ".join(city_list))  # Output: lahore, karachi

# 11. find(substring): Returns the index of the first occurrence of a substring.
city = "lahore"
print(city.find("h"))  # Output: 2 (index of 'h')

# 12. count(substring): Returns the number of occurrences of a substring.
city = "lahore"
print(city.count("a"))  # Output: 1 (number of 'a' in "lahore")

# 13. startswith(prefix): Checks if the string starts with a specified prefix.
city = "lahore"
print(city.startswith("la"))  # Output: True (starts with 'la')

# 14. endswith(suffix): Checks if the string ends with a specified suffix.
city = "lahore"
print(city.endswith("re"))  # Output: True (ends with 're')