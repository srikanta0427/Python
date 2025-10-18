import re

text = 'ab '*66
result = re.findall('(a)+',text)
print(result)

