import os

print(os.name)
print(os.getlogin())
print(os.getcwd())
# print(os.listdir("C://Users//Srikanta//Downloads"))
os.chdir("C:\\")
print(os.getcwd())
# os.mkdir("C:\\PyMake")
print(os.path.isdir("C:\\PyMake"))
os.makedirs("C:\\PyMake\\Py1\\pandas")