

def setName(firstName,lastName):
    fullName = f'{firstName} {lastName}'
    return fullName.title()

while(True):
    print("Please tell your name:")
    print("(enter 'q' for exit any time)")

    firstName = str(input("Enter First Name :"))
    if firstName == 'q':
        break
    lastName = str(input("Enter Last Name :"))
    if lastName == 'q':
        break

    getName = setName(firstName,lastName)
    print(getName)

    