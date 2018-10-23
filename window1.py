
from tkinter import*
root=Tk()
root.title('sample window')
root.geometry('550x600')
c=Canvas(root,width=300,height=250,bg='blue',cursor='hand2')
c.pack()#pack is a method
img1=PhotoImage(file='C:\\Users\\PRASAD\\Desktop\\1.gif')
img2=PhotoImage(file='C:\\Users\\PRASAD\\Desktop\\2.gif')
c.create_image(200,150,image=img1,activeimage=img2)
root.mainloop()