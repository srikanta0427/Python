#  function to wheather check number is odd or even

def check_odd_even(num):
    if num%2==0:
        print('even')
    else:
        print('odd')

check_odd_even(int(input('Number :')))



bool = []
def arr_check_odd_even(arr):
    for i in arr:
        if i%2==0:
            bool.append(True)
        else:
            bool.append(False)

# arr = [1,2,3,4,5,6,7,8,9]

arr = []
size = int(input("Enter size of list"))
for i in range(size):
    arr.append(int(input("Enter Number : ")))
    

arr_check_odd_even(arr)
count = 0
for i in bool:
    if i!=False:
        print(arr[count],'is Even')
    else:
        print(arr[count],'is Odd')
    count+=1
