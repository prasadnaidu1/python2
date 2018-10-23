def laptop(fun):
    def charger():
        return 'work'
    return 'laptop {} is to be charged then only laptop will  {} '.format(fun,charger())
#calling block
s =laptop('lenovo')
print(s)