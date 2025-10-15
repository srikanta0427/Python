# 1-isdigit()
digit = '123'
print(digit.isdigit())      #Output     True

d1 = '123.56'
print(d1.isdigit())         #Output     False

d2 = '-34'
print(d2.isdigit())         #Output     False

# 2-isdecimal()

dec = '4555'
print(dec.isdecimal())      #Output     True
d1 = '345.78'
print(d1.isdecimal())       #Output     False

# 3-isnumeric()
num = '456'
print(num.isnumeric())      #Output     True
num1 = '567.78'
print(num1.isnumeric())     #Output     False
num2 = '-78'
print(num2.isnumeric())     #Output     False

# 4-isalnum()

n1 = '123abc'
print(n1.isalnum())         #Output     True