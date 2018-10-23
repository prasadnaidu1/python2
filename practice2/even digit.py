n =int(input('enter a number:'))
temp =n
sum =0
while n!=0:
    d =n%10
    if n%2==0:
        sum+=d
        n =n//10
    print('sum of digits of {} is {}'.format(temp,sum))