import re

text = 'the price is $40'
price = re.search('40',text).span()

print(re.search('40',text))
# print(text[price[0]])

print(price[0])
for i in range(len(price)):
    print(price[i])