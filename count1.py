fobj=open('prasad.txt','w')
print('enter the data')
while True:
    line=input()
    if line!='stop':
        fobj.write(line)
        fobj.write('\n')
    else:
        break
fobj.close()
