dict={'id':102,
      'name':'prasad',
      'sal':20000
      }
for x in dict:
    print(x)    #it displays keys in a dictionary
print('\n========================================')
dict={'id':102,
      'name':'prasad',
      'sal':20000
      }
for x in dict:
    print(dict[x])  #it shows values of dictionary
print('\n========================================')
dict={'id':102,
      'name':'prasad',
      'sal':20000
      }
for x in dict:
    print(x,'--',dict[x])      #it dispalys key and values in dictionary
print('\n========================================')
dict={101:[10,30,40,50,60,70,80],
      102:[45,56,78,87,34,76,67],
      103:[99,98,97,96,67,87,78],
      104:[56,45,78,90,35,90,67]}
for x in dict:
    print('idno of student:',x)
    print('total of the student marks:',sum(dict[x]))
    print('highest marks in the subject:',max(dict[x]))
    print('lowest marks in the subject:',min(dict[x]))
    print('==================================================')

print('===========================================================')
d1={'idno':102,'name':'prasad','sal':35000}
for x in d1.items():
    print(x)
print('================================================================')
d1={'idno':102,'name':'prasad','sal':35000}
for x,y in d1.items():
    print(x,y)
print('================================================================')
d1={'idno':102,'name':'prasad','sal':35000}
for key,value in d1.items():
    print(key,value)
print('================================================================')
d1={'idno':102,'name':'prasad','sal':35000}
for x in d1.keys():
    print(x)
print('================================================================')
d1={'idno':102,'name':'prasad','sal':35000}
for x in d1.values():
    print(x)
print('================================================================')