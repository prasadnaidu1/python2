set1={1,2,3,4,6,2,3,4,5}
print(set1)
print('========================================================')
set2={10,30,21,23,40,67,89,98,87,67}
set2.remove(40)
print(set2)
print('========================================================')
set3={10,30,21,23,40,67,89,98,87,67}
set3.clear()
print(set3)
print('=========================================================')
set4={10,30,21,23,40,67,89,98,87,67}
set5={23,4,4,43,23,6}
set6=set4.union(set5)
print(set6)
print('============================================================')
set4={10,30,21,23,40,67,89,98,87,67}
set5={23,4,4,43,23,6,21,89,87,67}
set7=set4&set5
print(set7)
print('===============================================')
set4={1,2,3,4,5,6,7,8,9,10,11,22,33,44,111,222,333,444}
set5={1,2,3,4,5,6,7,8,9,10}
set8=set4>set5#finding the length of the sets and then it will compare to each other
set9=set4<set5
print(set8)
print(set9)
print('================================================')

set={10,2,3,4,5,6,7,8,9,11}
set13={1,2,3,4,55,60,7,8,9,14}
set11=set13-set
set12=set^set13
print(set11)
print(set12)




