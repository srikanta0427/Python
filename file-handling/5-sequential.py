path = r"C:\Users\Srikanta\Desktop\Python\file_handling\read.txt"
with open(path,'r') as file:
    ch1 = file.read(1)
    ch2 = file.read(3)
    ch3 = file.read(7)
print(ch1,ch2,ch3)
