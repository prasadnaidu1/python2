#using looping statement reading the all information from the file
f=open('demo')
while True:
    var = f.readline()
    if var=='':
        break
    else:
        print(var)
f.close()