# radius = int(input("Enter radius: "))

# area = 3.14 * radius * radius

# print("Area of Circle =", area)


#length * breadth
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))

# area = length * breadth
# perimeter = 3 * (length + breadth)

# print("Area =", area)
# print("Perimeter =", perimeter)

#Area of Triangle
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))

# area = 2 * base * height

# print("Area of Triangle =", area)



#Celcius to Farnehite
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit =", fahrenheit)


#Kelometer to centimeter
# km = float(input("Enter distance in kilometers: "))

# meters = km * 1000
# centimeters = km * 100000

# print("Meters =", meters)
# print("Centimeters =", centimeters)

#Simple intrest
# principal = float(input("Enter principal amount: "))
# rate = float(input("Enter rate of interest: "))
# time = float(input("Enter time in years: "))

# si = (principal * rate * time) / 100

# print("Simple Interest =", si)



#swap without third variable
# a = 7
# b = 5

# a = a + b
# b = a - b
# a = a - b


# print("After swapping:")
# print("a =", a)
# print("b =", b)


#Percentage of five subject
# m1 = float(input("Enter marks of Subject 1: "))
# m2 = float(input("Enter marks of Subject 2: "))
# m3 = float(input("Enter marks of Subject 3: "))
# m4 = float(input("Enter marks of Subject 4: "))
# m5 = float(input("Enter marks of Subject 5: "))

# total = m1 + m2 + m3 + m4 + m5
# percentage = total / 5

# print("Total Marks =", total)
# print("Percentage =", percentage, "%")



#15. Convert days into weeks and days*
# days = int(input("Enter number of days: "))

# weeks = days // 7
# remaining_days = days % 7

# print("Weeks =", weeks)
# print("Days =", remaining_days)


#16. Convert seconds into hours, minutes, and seconds*
# seconds = int(input("Enter seconds: "))

# hours = seconds // 3600
# remaining = seconds % 3600
# minutes = remaining // 60
# seconds = remaining % 60

# print("Hours =", hours)
# print("Minutes =", minutes)
# print("Seconds =", seconds)


#Sallary
# basic_salary = float(input("Enter basic salary: "))

# hra = basic_salary * 0.20
# da = basic_salary * 0.10

# gross_salary = basic_salary + hra + da

# print("HRA =", hra)
# print("DA =", da)
# print("Gross Salary =", gross_salary)



#18. Total bill after adding GST*
# amount = float(input("Enter bill amount: "))
# gst_rate = float(input("Enter GST rate (%): "))

# gst = amount * gst_rate / 100
# total_bill = amount + gst

# print("GST =", gst)
# print("Total Bill Amount =", total_bill)



#24. Sum of digits of a three-digit number*
# num = int(input("Enter a three-digit number: "))

# hundreds = num // 100
# tens = (num // 10) % 10
# ones = num % 10

# sum_digits = hundreds + tens + ones

# print("Sum of digits =", sum_digits)



#25. Reverse a three-digit number*
# num = int(input("Enter a three-digit number: "))

# hundreds = num // 100
# tens = (num // 10) % 10
# ones = num % 10

# reverse = ones * 100 + tens * 10 + hundreds

# print("Reverse number =", reverse)



### 10. Check whether a character is a vowel or consonant
# ch = input("Enter a character: ")

# if ch.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


### 16. Check whether a character is uppercase or lowercase
# ch = input("Enter a character: ")

# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# else:
#     print("Not an alphabet")


### 17. Check whether a number is a two-digit number
# num = int(input("Enter a number: "))

# if 10 <= abs(num) <= 99:
#     print("Two Digit Number")
# else:
#     print("Not a Two Digit Number")



### 24. Calculate discount
# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = amount * 20 / 100
# elif amount >= 3000:
#     discount = amount * 10 / 100
# else:
#     discount = 0

# final_amount = amount - discount

# print("Discount =", discount)
# print("Final Amount =", final_amount)




### 30. ATM withdrawal program
balance = 10000

amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
else:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)


    








  


 

   





