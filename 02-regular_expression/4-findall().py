import re

text = 'can you can a can as a canner'
result = re.findall('can',text)
print(result)