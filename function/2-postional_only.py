def num(a,b,/,c,d):
    print(a,b,c,d)

# num(a=4,b=3,c=3,d=4)  // this is wrong 

num(5,6,c=4,d=4)


def float(a,b,c,d,/):
    print(a,b,c,d)

# float(a=1,b=2,c=3,d=5)    // TypeError:   float() got some positional-only arguments 
#                                           passed as keyword arguments: 'a, b, c, d'

float(1,2,3,4)


# def nm(/,a,b,c,d):    // SyntaxError: at least one argument must precede /
#     print(a,b,c,d)      