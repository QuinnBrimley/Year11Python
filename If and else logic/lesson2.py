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
"""

if age >= 18:
    print("You are 18 years old or older")
elif age <= 17 and age >=10:
    print("You are between 17 and 10")
else:
    print("You are younger than 10")