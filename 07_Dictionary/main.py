# Dictionary in Python:
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after creation.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Keys must be immutable types (e.g., strings, numbers, tuples), while values can be of any type.
# Dictionaries are unordered collections, meaning the order of items is not guaranteed.

cars = {
   "toyota" : "Corolla" ,
   "Honda" : "Civic" ,
   "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "Nissan": "Altima"

}

print(" All cars" , cars) #it will print all cars
print("Toyota from objects" , cars["toyota"]) # # Access the value associated with the key "toyota"

marks=  {
    "Urdu" : 97 , 
    "Maths" : 100 , 
    "English" : 80 
}

#print all subject marks 
print("Marks of all subjects are" , marks) #print all subject marks 
print("Marks in maths are " , marks ["Maths"] )  #Access the value associated with the key "Math"
print("Urdu marks:", marks.get("Urdu"))  # Access the value associated with the key "Urdu" using get() method


marks["Science"] = 70 # it will add a new key in marks

del marks["English"] # removes english from Dictionary 

length = len(marks)  # Get the number of key-value pairs in the dictionary
print("Number of subjects:", length)  # Print the number of subjects in the dictionary
