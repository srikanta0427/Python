s = 'hello'
s1 = s.ljust(len(s)+5,'*')
print(s1)

text = "hello"
print(text.ljust(10))        # Output: 'hello     '
print(text.ljust(10, '-'))   # Output: 'hello-----'
