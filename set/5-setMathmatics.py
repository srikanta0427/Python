a = {1,2,3,5,7}
b = {5,7,8,9}
print('A =',a)
print('B=',b)

union = a.union(b)
print('UNION :',union)

difference = a.difference(b)
print('DIFFERENCE :',difference)

intersection = a.intersection(b)
print('INTERSECTION :',intersection)

symmetricDiffrence = a.symmetric_difference(b)
print('symmetricDiffrence :',symmetricDiffrence)