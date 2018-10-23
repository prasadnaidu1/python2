#in a set removed duplicates and get seqence order.
l1=[1,30,2,3,100,200,1,2,200]
l2=list(set(l1))
l2.sort(key=l1.index)
print(l2)
l3=sorted(l2)
print(l3)
l4=sorted(l2,reverse=True)
print(l4)
