s =input('enter a number:')
i =len(s)
n =int(s)
temp =n
sum =0
while n!=0:
    k =n%10
    sum+=k**i
    n =n//10
if sum==temp:
    print('is a armstrong')
else:
    print('is not a armstrong')