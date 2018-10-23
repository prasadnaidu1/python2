from tkinter import*
def buttonclick(num):
    if num==1:
      f['bg']='red'
    elif num==2:
        f['bg']='green'
    elif num==3:
        f['bg']='blue'
    else:
        f['bg']='black'
    
root=Tk()
root.title('sample window')
root.geometry('500x400')
f=Frame(root,width=400,height=350,bg='blue',cursor='hand2')
f.propagate(0)
f.pack()
b1=Button(f,text='red',fg='red',width=8,height=2,command=lambda :buttonclick(1))
b1.place(x=50,y=50)
b2=Button(f,text='green',fg='green',width=8,height=2,command=lambda :buttonclick(2))
b2.place(x=170,y=50)
b3=Button(f,text='blue',fg='blue',width=8,height=2,command=lambda :buttonclick(3))
b3.place(x=280,y=50)
b4=Button(f,text='black',fg='black',width=8,height=2,command=lambda :buttonclick(4))
b4.place(x=0,y=50)
root.mainloop()
