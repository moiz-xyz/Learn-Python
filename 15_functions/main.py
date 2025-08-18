# what are functions?
# Functions are reusable pieces of code that perform a specific task.
# They help to organize code, make it more readable, and reduce redundancy.
# Block of code that only runs when called.
# Functions can take inputs (arguments) and can return outputs (results).

# creating a function
def greet():
    print("Hello function")

#calling a function
greet()

# Function with parameters
def greetUser(name , age):
    print(f"Hello and welcomee :{name}" )
    print(f"Your age is {age}")

# Calling the function with arguments
greetUser("John", "26")
greetUser("Moiz", "18")

# Function with default parameters
def greetUser(name , age = 18):
     print(f"Hello, and welcome:  {name}!")
     print(f'Age is {age}')

# Calling the function with default parameter
greetUser("Ali")

# function to crete the sum oif two numbers

def sum(num1 , num2):
   sum_result = num1 + num2
   print(f"The sum is: {sum_result}")

sum(109,12)
sum(1882,1393)
sum(18329382,1382932893)