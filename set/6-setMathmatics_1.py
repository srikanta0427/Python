a = {1,2,3,5,7}
b = {5,7,8,9}

a.intersection_update(b)
print(a)
b.intersection_update(a)
print(b)

a = {1,2,3,5,7}
b = {5,7,8,9}

a.difference_update(b)
print(a)
b.difference_update(a)
print(b)

a = {1,2,3,5,7}
b = {5,7,8,9}

a.symmetric_difference_update(b)
print(a)
b.symmetric_difference_update(a)
print(a)
