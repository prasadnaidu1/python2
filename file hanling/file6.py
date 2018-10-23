#without using any read method we can read the data also
f=open('demo')
for x in f:
    print(x,end='')
f.close()