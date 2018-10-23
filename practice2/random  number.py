import random
print('start of your pgm')
while True:
    n =int(input('enter a number b/w 1 to 10:'))
    i =random.randint(1,10)
    if n!=i:
        print('enter your number',n)
        print('enter random number',i)
        print('your guess is wrong')
        continue
        print('enter your number',n)
        print('enter random number',i)
        print('your guess is correct')
        break
        print('The end of the pgm')