no=int(input('Enter a Number:  '))
rev=0
while no>4:
    r=no%10
    no=no//10
    rev=(rev*10)+r
print(rev)
print('Thanks')
