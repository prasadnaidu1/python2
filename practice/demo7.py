my_list=[10,20,(30,40,60),80]
my_list2=set(my_list)
print(my_list2)
my_list3=list(my_list2)
print(my_list3)
set={10,20,30,40}
set1=set.add(70)
print(set)
set2=set.remove(30)
print(set)
myset1={10,20,30}
myset2={1,2,3,4}
myset3=myset1|myset2    # (or)myset3=myset1.union(myset2)
print(myset3)
myset4=myset1.intersection(myset2)
print(myset4)
myset5=myset2.difference(myset1)
print(myset5)
myset6=myset1.issubset(myset2)
print(myset6)
myset7=myset1.issuperset(myset2)
print(myset7)
myset8=myset1.symmetric_difference(myset2)
print(myset8)
