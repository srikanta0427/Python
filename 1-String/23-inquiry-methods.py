# return as True / False

# 1-isalpha()
st = '#$%^'
print(st.isalpha())     # Output    False

# 2-islower()
s1 = 'sradha'
print(s1.islower())     # Output    True

nm = 'sradhA'
print(nm.islower())     # Output    False

# 3-isupper()
s2 = 'SRADHA'
print(s2.isupper())     # Output    True

nm = 'SRADHa'
print(nm.isupper())     # Output    False

# 4-istitle()
text = 'Sradha is a good girl'
print(text.istitle())           # Output    False

text = 'Sradha Is A Good Girl'
print(text.istitle())           # Output    True
