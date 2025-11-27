import csv

f = open("C://PyMake\\Book1.csv",'r')
csv_reader = csv.reader(f)
print(csv_reader)
ff = next(csv_reader)
print(ff)
for i in csv_reader:
    if int(i[1]) > 20:
        print(int(i[1]) + 10)