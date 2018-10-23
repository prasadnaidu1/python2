import copy as cp
l1=[[10,20,30],[40,50,60],[70,80,90]]
l2=cp.deepcopy(l1)
l2[1][2]=555
print(l1)
print(l2)
