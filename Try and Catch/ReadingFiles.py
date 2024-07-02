import os

print("Current working directory:", os.getcwd())
file_path = "C:\\Users\\QBR\\Documents\\Year11Python\\file.txt"

if os.path.isfile(file_path):

    f = open(file_path)
    print(f.read())

    for x in f:
        print(x)
else:
    print("File does not exist!")