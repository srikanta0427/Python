t = (*(x for x in range(1,11)),)
print(t)

even  = (*(x for x in range(1,100) if x%2==0),)
print(even)

char = (*(w for w in "python"),)
print(char)

isAlpha = (*(a for a in "1sri67kanta" if a.isalpha()),)
print(isAlpha)