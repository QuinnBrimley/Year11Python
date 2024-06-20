"""
What if we wanted to check if someone was over the age of 18 to see a R rated movie?
That would be pretty useful wouldnt it be?
Well there is a way! With if and else logic!


Basic if and else strucutres goes like this

if (conditon):
    do something
else:
    do something

"""

age = int(input("Enter your age: "))
if(age >= 18):
    print("You are old enough to watch the R rated movie!")
else:
    print("You are not old enough!")


name = str(input("Enter your name for a check: "))
if (name == "Kate"):
    print(f"Welcome {name}")
else:
    print("Your not welcome here >:(")


"""
We can add a else if to check more conditons like this
Brackets are not needed around the condtion however it can help
with visibility and readability.

if condition:
    do something
elif condition:
    do something else:
continue as many elif you need....
else:
    do this

"""

if age >= 18:
    print("You are 18 years old or older")
elif age <= 17 and age >=10:
    print("You are between 17 and 10")
else:
    print("You are younger than 10")

#Note that we can include as many elif we like, we just 
#Need to add it on to our if and else structure.

#Does changing and to or do anything?
if age >= 18:
    print("You are 18 years old or older")
    print("Hello")
elif age <= 17 or age >=10:
    print("You are between 17 and 10")
else:
    print("You are younger than 10")


#More examples of if and else logic

x = 10

if x > 15:
    print("x is greater than 15")
elif x > 10:
    print("x is greater than 10 but less than or equal to 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")


#Nesting if statements

x = 10
y = 20

if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")
    else:
        print("x is greater than 5 but y is 15 or less")
else:
    print("x is 5 or less")


#Using logic operators
x = 10
y = 5

if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10")
else:
    print("Either x is not greater than 5 or y is not less than 10")


"""
Short circuiting is when a if condition doesnt full complete
its check
"""

a = False
b = True
# This won't print anything because `a` is False, so `b` is not evaluated
if a and print("This won't be printed"):
    print("Inside if block")


a = True
b = False

# This won't print anything because `a` is True, so `b` is not evaluated
if a or print("This won't be printed"):
    print("Inside if block")


# Import math Library
import math

# Return the square root of different numbers
print (math.sqrt(9))