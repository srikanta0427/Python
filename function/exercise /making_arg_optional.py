def get_formatted_name(firstName,lastName,middleName='',):
    if middleName:
        fullName = f'{firstName} {middleName} {lastName}'
        return fullName.title()
    else:
        fullName = f'{firstName} {lastName}'
        return fullName.title()
    
print(get_formatted_name("srikanta","barik"))
print(get_formatted_name("soumya","nanda","ranjan"))
