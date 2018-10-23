import copy as cp
l1=[[[1,2,3],[10,20,30],[40,50,60]],[4,5,6]]
l2=cp.deepcopy(l1)
l2[0][0][2]=222
l3=cp.deepcopy(l1)
l3[0][2][1]=444
print(l1  )
print(l2)
print(l3)
