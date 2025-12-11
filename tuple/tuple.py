#  Creating a tuple
numbers = (10, 20, 30, 40, 50)
print("Original Tuple:",numbers)

#  Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

#  Slicing a tuple
print("Slice (1 to 3):", numbers[1:4])
#  Checking membership
value = 30
if value in numbers:
    print(value, "is present in the tuple")
else:
    print(value, "is not present")

#  Looping through a tuple
print("All elements in tuple:")
for n in numbers:
    print(n)

#  Tuple length
print("Tuple length:", len(numbers))

#  Using functions: min(), max(), sum()
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

#  Trying to update tuple (Convert to list and back)
temp_list = list(numbers)
temp_list.append(60)  # Adding new value
numbers = tuple(temp_list)
print("Updated Tuple after adding 60:", numbers)

#  Concatenating two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print("Concatenated Tuple:", t3)

#  Tuple with mixed data types
mixed = ("Srikanta", 22, 5.7, True)
print("Mixed Tuple:", mixed)
