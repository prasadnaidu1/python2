f=open('demo2','w')
print('enter the data')
while True:
    line=input()
    if line!='stop':
        f.write(line)
        f.write('\n')
    else:
        f.close()
        break
