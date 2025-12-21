print("heelo")

print("hello")

# string
userName = "moiz"
adeena = "name"

# integer data types
num1 = 1

print(adeena)
print(num1)


num2 = 102.12
bolean = True
bolean = False

num1 = 10
num2 = "10"



num1 = 10
num2 = 20

print(10 + 20) 
print(10 - 20) 
print(10 * 20) 
print(10 / 20)

a = 12
b = 12
print (a + b)


a = 7
b = 3
print( 7 // 3)


firsstName = "adeena"
lastName = "amjad"

print(firsstName + " "+ lastName)
print(len(lastName))

string = "Hello world again"
sliced_Again = string [12:17]
print("slicing again from hellon world " , sliced_Again)


firsstName = "Hellu my name is adeena amjad snake "
sliced = firsstName[17:35]
print(sliced)


# lists
users = ["ali" , "qasim" , "ahemd", "sara"]

users = ["hadin" , "adeena" , "mahrukh"]
print(users) 
print(users[0])  # first user
print(users[1]) 
print(users[2]) 
# ast user
print(users[-1])  


# users.append("moiz")
users.insert(0 , "moiz")
print("update lists" , users)
users.remove("moiz")
print("update lists" , users)
del users[1]
print("delete user" , users) 
print("length  of user array",len(users))

numberlst = [1,2,3,4,5,6,7]
numberlst.sort() # decending
print("sorted array from chota sa bara",numberlst)
numberlst.reverse()#aseending
print("sorted array from bara sa chota",numberlst)

users = ["hadin" , "adeena" , "mahrukh", "moiz" , "mahreen" , "zaraksha"]
users.sort() # decending
print("sorted array from chota sa bara",users)
users.reverse()#aseending
print("sorted array from bara sa chota",users)

users.pop()
print("pop ki howi list" , users)

print(users[1:5])