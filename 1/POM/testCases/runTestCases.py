import os

my_dir = os.getcwd()
# Using os.listdir to create a list of all of the files in dir
dir_list = os.listdir(my_dir)
print(dir_list)
# Use the for loop to iterate through the list you just created, and open the files
for f in dir_list:
    if f != "runTestCases.py" and f != "Test.py":
        print("Testing file: " + f)
        os.system("python3 -m unittest " + f)