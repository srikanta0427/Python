import csv
data =  [
            ('name','roll'),
            ('srikanta','27')
        ]
# f = open("C://PyMake\\Book2.csv",'w')
f = open("C:\\PyMake\\Book2.csv",'w',newline='')
wtr = csv.writer(f)

for i in data:
    wtr.writerow(i)


f.close()