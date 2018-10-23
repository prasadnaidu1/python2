a=input('enter a string:')
b=input('enter  b string:')
if len(a)>len(b):
    print('a is bigger than b')
if len(a)<len(b):
    print('a is smaller than b')
if len(b)<len(a):
    print('b is smaller than a')
if len(b)>len(a):
    print('b is bigger than a')
if len(a)==len(b):
    print('both strings are equal')
