def div(a,b):
    print('the div=', add(a,b))
    return (a + b)
def mul(a,b):
    print('the div=', sub(a,b))
    return (a - b)
def sub(a,b):
    print('the mul=', mul(a,b))
    return (a * b)
def add(a,b):
    print('the sub=', div(a,b))
    return (a / b)

print(add(2,4))


