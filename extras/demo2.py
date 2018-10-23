id=int(input('enter id no:'))
na=input('enter name:')
no=int(input('enter no of subjects:'))
subj=[]
for x in range(no):
    subject=input('enter subject name')
    subj.append(subject)
from extras.sample import faculty
f3=faculty(idno=id,name=na,subjects=subj)
f3.display()


