li = [i for i in range(1,5)]
print(li)

l_1 = [(i*2) for i in range(1,9)]
print(l_1)

name = [s.upper() for s in "SriKantA"]
print(name)

num = [int(n) for n in "1234"]
print(num)
print(type(num[1]))


word = [w for w in "12sri&4" if w.isalpha()]
print(word)