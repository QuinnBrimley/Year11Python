v = ["a,e,i,o,u"] #You could also do a string here since a string is a list of characters
user_input = str(input("Enter a string: "))
count = 0
for i in user_input:
    if i.lower() in v:
        count+=1
print(f"There are {count} vowels in the string {user_input}")

for i in user_input:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
print(f"There are {count} vowels in the string {user_input}")
