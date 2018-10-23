n =int(input('enter a number:'))
count =0
for i in range(1,n+1):
    if n%i==0:
        count +=1
if count ==2:
        print(n ,'it is a prime number')
else:
        print(n ,'it is not a prime number')