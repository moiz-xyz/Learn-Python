#  basics
                     
class Student():
    name = "Moiz"

s1 = Student()
print(s1.name)

#constructor

# class Car:
#     def __init__():
#         print("Craeating a nnew nodel car")
#         name = "mehran"
# car1 = Car()
# print(car1)        

class Car:
    def __init__(self):  
        print("Creating a new model car")
        self.name = "Mehran"  

# create object
car1 = Car()

print(car1.name)