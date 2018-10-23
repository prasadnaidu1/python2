from tkinter import *
def show_entry_fields():
    print('firstname: %s\nLastname: %s' % (e1.get(),e2.get()))
master = Tk()
master.title('login')
Label(master, text='firstname').grid(row=0)
Label(master, text='lastname').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master,text='Quit',command=master.quit).grid(rows=3,column=0,sticky=W,pady=4)
Button(master,text='Show',command=show_entry_fields()).grid(rows=3,column=1,sticky=W,pady=4)
master.mainloop()
