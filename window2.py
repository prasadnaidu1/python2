from tkinter import*
root=Tk()
root.title('sample window')
root.geometry('550x600')
c=Canvas(root,width=200,height=100,bg='blue',cursor='hand2')
c.pack()#pack is a method
c.create_text(100,150,text='welcome to GUI', bg='blue',fil='white')
c.pack()
root.mainloop()