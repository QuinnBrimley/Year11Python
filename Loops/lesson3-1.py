lst = [1,2,3,4,5,6,7,8,9,10]
print(lst)

x = lst[4]

lst = [1,2,"sting",3.142,True]

lst.pop()
lst.append(5)
ln = len(lst)
s = "we-ball"
n = len(s)


for i in range(1,10):
    print(i)

lst_names = ["Quinn","Sarah"]

for name in lst_names:
    if name == "Sarah":
       print("we dont ball")
    else:
        print("WE ball")

answer = 5
user_guess = int(input("Enter a number: "))
is_correct = False
while is_correct == False:
    if(user_guess == answer):
        print("You go girl")
        is_correct = True
    else:
        print("We aint balling")
    user_guess = int(input("Enter a number: "))
    

    