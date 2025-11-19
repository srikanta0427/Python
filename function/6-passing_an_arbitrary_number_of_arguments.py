# passing_an_arbitrary_number_of_arguments

def pizzaTopping(*topping):
    print( type(topping))
    print(topping)

pizzaTopping('pepperoni')
pizzaTopping('mushrooms', 'green peppers', 'extra cheese')

