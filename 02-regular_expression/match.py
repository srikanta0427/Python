import re

text = 'yes, you are'
result = re.match('yes',text).group()
print(result)
print(re.match('you are',text))
