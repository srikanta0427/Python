# Inserting Data without replacing old data 
li = [2,3,4,5,6,7,8]
li[2:2] = [66,88,78,80,89]
print(li)

l2 = [2,4,5]
l2[2:2] = [6]
print(l2)
# ------------------------------------------------
li.insert(0,22)
print(li)

