print("hello")

# data types

# 1 string
name = "moiz"
print (name)

# numbers 
age = 10
print(age)

# fload
float1 = 10.2

# narithema6tcoi oipertorwsd 

a = 10 
b = 20 
add = a + b 

# 1. Student Grading System

# Take marks of 5 subjects from user, calculate total, percentage, and print grade based on percentage:
student_marks1 = int(input("Enter your marks in Maths: "))
student_marks2 = int(input("Enter your marks in English: "))
student_marks3 = int(input("Enter your marks in Urdu: "))
student_marks4 = int(input("Enter your marks in Physics: "))
student_marks5 = int(input("Enter your marks in Chemistry: "))

student_sum = student_marks1 + student_marks2 + student_marks3 + student_marks4 + student_marks5
print("Total Marks:", student_sum)

student_avg = (student_sum / 500) * 100
print("Percentage:", student_avg, "%")

if student_avg > 90:
    print("Grade is A+")
elif student_avg > 70:
    print("Grade is A")
elif student_avg > 50:
    print("Grade is B")
else:
    print("Summer ka bhosr papar hogy ha")

# 2. Word Counter

Ask user for a string and count:
Number of characters
Number of words
Number of vowels in it

string = input("Enter a string: ")

length_characters = len(string)
print("The character in strings are",length_characters)
words = string.split()
length_words = len(words)
print("The length of string is" ,length_words)

vowels = "aeiouAEIOU"
length_vowels = sum(1 for char in string if char in vowels)

print("Vowels:", length_vowels)

# # Initial balance in accounts
ssaving_balance = 10000
current_balance = 5000

pin = 1234
user = int(input("Enter your pin: "))

if user == pin:
    action = input("What do you want to do? (deposit/withdraw): ").lower()
    account_type = input("Enter your account type (saving/current): ").lower()

    if account_type == "saving":
        if action == "deposit":
            amount = int(input("Enter amount you want to deposit: "))
            saving_balance += amount
            print("You have successfully deposited", amount, "into your savings account.")
            print("Your new savings balance is:", saving_balance)

        elif action == "withdraw":
            amount = int(input("Enter amount you want to withdraw: "))
            if amount <= saving_balance:
                saving_balance -= amount
                print("You have successfully withdrawn", amount, "from your savings account.")
                print("Your new savings balance is:", saving_balance)
            else:
                print("Insufficient funds in savings account.")

        else:
            print("Invalid action.")

    elif account_type == "current":
        if action == "deposit":
            amount = int(input("Enter amount you want to deposit: "))
            current_balance += amount
            print("You have successfully deposited", amount, "into your current account.")
            print("Your new current balance is:", current_balance)

        elif action == "withdraw":
            amount = int(input("Enter amount you want to withdraw: "))
            if amount <= current_balance:
                current_balance -= amount
                print("You have successfully withdrawn", amount, "from your current account.")
                print("Your new current balance is:", current_balance)
            else:
                print("Insufficient funds in current account.")

        else:
            print("Invalid action.")

    else:
        print("Invalid account type.")

else:
    print("Incorrect pin")
