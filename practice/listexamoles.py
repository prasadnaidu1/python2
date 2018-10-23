list1=[12,23,32,21,45]
list2=[40,50,60,70]
list1.extend(list2)
print(list1)
print('==================================')
list1=[1,2,3,4,56]
list1.insert(3,777)
print(list1)
print('===================================')
list=[1,20,60,70,80]
list2=list.pop(3)
print(list)
print(list2)
print('===================================')
list=[1,20,60,70,80]
list2=max(list)
list3=min(list)
print('maximum value:',list2)
print('minimum value:',list3)

print('===================================')
list=[1,20,60,70,80]
list4=sum(list)
print(list4)
print('=====================================')
list=[1,20,60,70,80]
list2=len(list)
print(list2)
print('======================================')
list=[1,20,60,70,80]
list2=list.index(70)
print(list2)
print('======================================')
list=[10,20,10,20,30,40,60,40,30,30,30,10,10]
list2=list.count(10)
list3=list.count(30)
print('repeated value of',list2)
print('repeated value of',list3)
print('========================================')
list=[1,2,3,4,10,20,30,40]
del list
print(list)
print('=======================================')
list=[1,2,3,4,10,20,30,40]
list.remove(10)
print(list)
print('==================================================')
list=[1,2,3,4,10,20,30,40]
list.clear()
print(list)
print('==============================================================')
dict1={'x':'prasad','y':200}
print(dict1['x'],dict1['y'])
print('================================================================')
list=[1,2,3,4,5,6,7,8,9]
list2=list[2:8:2]
print(list2)
print('===========================================================================')
list=[1,2,3,4,5,6,7,8,9]
list2=list[-2:2:-2]
print(list2)
print('===========================================================================')
list8=[1,2,3,4]
list9=[6,7,8,9]
list0=list8+list9
list11=list0*2
print(list0)
print(list11)





