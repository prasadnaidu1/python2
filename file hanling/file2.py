
#using exception hanling then we create the file and read the data from files
try:
    f = open('demo', 'r')
    var = f.read()
    print(var)
    f.close()
except FileNotFoundError:
    print('file not found')
