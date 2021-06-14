from tkinter import *

def xoa():
    met.set('')
    cenmet.set('')
    inch.set('')

def centimet():
    a=float(nhap.get())
    m=a/100.00
    ich=a*0.39370
    met.set(m)
    inch.set(ich)

def metre():
    a=float(nhap.get())
    ich=a*0.0254
    cm=a/0.010000
    inch.set(ich)
    cenmet.set(cm)

def inches():
    a=float(nhap.get())
    cm=a/2.54
    m=a/0.0254
    cenmet.set(cm)
    met.set(m)

root=Tk()
root.minsize(height=300,width=350)
nhap=StringVar()
met=StringVar()
cenmet=StringVar()
inch=StringVar()

root.title('code by hieutruong')

Label(root,text='LENGTH CONVERTER',fg='blue',font=(18)).grid(row=0,column=2)
Entry(root,textvariable=nhap).grid(row=1,column=2)

Label(root,text='centimet').grid(row=3,column=1)
Entry(root,textvariable=cenmet).grid(row=3,column=2)

Label(root,text='metre').grid(row=4,column=1)
Entry(root,textvariable=met).grid(row=4,column=2)

Label(root,text='inch').grid(row=5,column=1)
Entry(root,textvariable=inch).grid(row=5,column=2)

framebutton=Frame()
Button(framebutton,text='centimet',command=centimet).pack(side=LEFT)
Button(framebutton,text='metre',command=metre).pack(side=LEFT)
Button(framebutton,text='inch',command=inches).pack(side=LEFT)
Button(framebutton,text='del',command=xoa).pack(side=LEFT)
framebutton.grid(row=2,column=2)

root.mainloop()