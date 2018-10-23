import copy as cp
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=cp.copy(l1)
l2[0][2]=444
print(l2)
print(l1)