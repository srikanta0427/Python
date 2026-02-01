arr = [1, 2, 2, 3, 4, 4, 5]

unique = []
for x in arr:
    if x not in unique:
        unique.append(x)

print(unique)
