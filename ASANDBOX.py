import os

current_working_directory = os.getcwd()

print(current_working_directory)

parent_directory = os.path.dirname(current_working_directory)

print(parent_directory)


for file in os.listdir(parent_directory):
    if file.endswith(".py"):
        print(file)
