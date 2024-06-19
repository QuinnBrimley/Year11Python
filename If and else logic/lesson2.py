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
elif age <= 17 or age >=10:
    print("You are between 17 and 10")
else:
    print("You are younger than 10")


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