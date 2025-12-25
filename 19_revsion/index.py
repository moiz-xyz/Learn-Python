# print("heelo")

# print("hello")

# # string
# userName = "moiz"
# adeena = "name"

# # integer data types
# num1 = 1

# print(adeena)
# print(num1)


# num2 = 102.12
# bolean = True
# bolean = False

# num1 = 10
# num2 = "10"



# num1 = 10
# num2 = 20

# print(10 + 20) 
# print(10 - 20) 
# print(10 * 20) 
# print(10 / 20)

# a = 12
# b = 12
# print (a + b)


# a = 7
# b = 3
# print( 7 // 3)


# firsstName = "adeena"
# lastName = "amjad"

# print(firsstName + " "+ lastName)
# print(len(lastName))

# string = "Hello world again"
# sliced_Again = string [12:17]
# print("slicing again from hellon world " , sliced_Again)


# firsstName = "Hellu my name is adeena amjad snake "
# sliced = firsstName[17:35]
# print(sliced)


# # lists
# users = ["ali" , "qasim" , "ahemd", "sara"]

# users = ["hadin" , "adeena" , "mahrukh"]
# print(users) 
# print(users[0])  # first user
# print(users[1]) 
# print(users[2]) 
# # ast user
# print(users[-1])  


# # users.append("moiz")
# users.insert(0 , "moiz")
# print("update lists" , users)
# users.remove("moiz")
# print("update lists" , users)
# del users[1]
# print("delete user" , users) 
# print("length  of user array",len(users))

# numberlst = [1,2,3,4,5,6,7]
# numberlst.sort() # decending
# print("sorted array from chota sa bara",numberlst)
# numberlst.reverse()#aseending
# print("sorted array from bara sa chota",numberlst)

# users = ["hadin" , "adeena" , "mahrukh", "moiz" , "mahreen" , "zaraksha"]
# users.sort() # decending
# print("sorted array from chota sa bara",users)
# users.reverse()#aseending
# print("sorted array from bara sa chota",users)

# users.pop()
# print("pop ki howi list" , users)

# print(users[1:5])




# tuples

# name = "moiz"
# cordiaates = (12.123 , 77.321 , "adeena")
# print(cordiaates)

# bacha_ka_record = ( 1,"zehrilly" , 3.0 ,True )
# print(bacha_ka_record[0])


# t = (1, 2, 2, 3, 3, 4, 1, 1, 1)
# print(t.count(1))   
# print(t.index(1))   


# student_record = ["adeene amjad" ,"moiz" , "mahrukh" , "zaraksha" " mahreen"]
# student_record = {
#     "name": "adeena amjad",
#     "father_name": "amjad",
#     "age": 21,
#     "is_student": True
# }
# print(student_record["father_name"])

# student_record["age"] = 22
# print(student_record.get("age"))

# del student_record["is_student"]
# print(student_record)


# # userImput

# name = input("enter your name:")
# print("Hello " + name)

# marks = input("Enter your marks in islamiyat")
# print(name, "your marks in islamiyat is " , marks)

# # marksheet 
# name = input("What is your name? ")
# english_marks = int(input("Enter your marks in English: "))
# math_marks = int(input("Enter your marks in Math: "))
# pst_marks = int(input("Enter your marks in PST: "))
# islamiyat_marks = int(input("Enter your marks in Islamiyat: "))

# total_marks = 400
# obtained_marks = english_marks + math_marks + pst_marks + islamiyat_marks 
# percentage = (obtained_marks / total_marks) * 100

# print("Marksheet for", name)
# print("Total Marks:", total_marks)
# print("Obtained Marks:", obtained_marks)
# print("Percentage:", percentage, "%")
# print("Marks breakdown:")
# print("English:", english_marks)
# print("Math:", math_marks)
# print("PST:", pst_marks)
# print("Islamiyat:", islamiyat_marks)


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else :
#     print("You are not eligible to vote yet.")

# name = input("What is your name? ")
# english_marks = int(input("Enter your marks in English: "))
# math_marks = int(input("Enter your marks in Math: "))
# pst_marks = int(input("Enter your marks in PST: "))
# islamiyat_marks = int(input("Enter your marks in Islamiyat: "))

# total_marks = 400
# obtained_marks = english_marks + math_marks + pst_marks + islamiyat_marks 
# percentage = (obtained_marks / total_marks) * 100
# if (percentage >= 90):
#     grade = "A+"
# elif (percentage >= 80):
#     grade = "A"
# elif (percentage >= 70):
#     grade = "B"
# elif (percentage >= 60 or total_marks >= 50):
#     grade = "C"
# else:
#     grade = "F"

# print("Marksheet for", name)
# print("Total Marks:", total_marks)
# print("Obtained Marks:", obtained_marks)
# print("Percentage:", percentage, "%")
# print("Grade:", grade)
# print("Marks breakdown:")
# print("English:", english_marks)
# print("Math:", math_marks)
# print("PST:", pst_marks)
# print("Islamiyat:", islamiyat_marks)


# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
# 5. Identity Operators: is, is not
# 6. Membership Operators: in, not in
# 7. Bitwise Operators: &, |, ^, ~, <<, >>
# 8. Ternary Operator: condition_if_true if condition else condition_if_false
# 9. Conditional Operator: (condition) ? (true_value) : (false_value)

#logical operators 
# country = input("Enter your country: ")
# city = input("Enter your city: ")

# if country == "Pakistan" and city == "Karachi" :
#     print("Youy are is Karachi , Pakistan")
# else : 
#     print ("You are not in karachi, Pakistan")

# country = input("Enter your country: ")
# city = input("Enter your city: ")

# if country == "Pakistan" or city == "Karachi" :
#     print("Youy are is Karachi , Pakistan")
# else : 
#     print ("You are not in karachi, Pakistan")


a = 10
print(a)
a += 4
print(a)

a = 10
b = 10

print(a is b)
print(a is not b)

name = ["mahren" , 'zaraksha' , 'adeena' , "moiz"]
print('moiz' not in name)

a = 5   # 0101
b = 3   # 0011

print(a & b)  # 1 (0001)


age = 17
if age >= 18 :
    status = "Adult"
else:
    status = "Minor"
print(status)