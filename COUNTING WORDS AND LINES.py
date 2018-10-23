fobj=open('satya','r')
count=0
c1=0
c2=0
for line in fobj:
    count+=1
    str=line.split()
    print(str)
    c1+=len(str)
    c2+=len(line)
print('no of lines', count)
print('no of words',c1)
print('no of characters',c2)
fobj.close()

