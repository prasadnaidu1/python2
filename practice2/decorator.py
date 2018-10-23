def decor(fun):
    def inner():
        val =fun()
        val+=20
        return val
    return inner
@decor
def my_num():
    return 10
#calling block
s1 =my_num()
print(s1)