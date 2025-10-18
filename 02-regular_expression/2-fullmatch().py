import re

text = 'yes, you are'
result = re.fullmatch('are',text)
print(result)

print(re.match('yes, you are',text).group())