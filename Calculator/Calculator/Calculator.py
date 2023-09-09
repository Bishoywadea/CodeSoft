from ast import Lambda
from tkinter import *
from turtle import width

#############################################################
###################    Calculator    ########################
#############################################################
root = Tk()
e=Entry(root,width=30)
e.grid(row=0,column=0,columnspan=4)

def clickNumber(inpt):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(inpt))

def clickOperation(inpt):
  global first
  first=e.get()
  global operation
  operation=inpt
  e.delete(0,END)

def clickEqual():
    second=e.get()
    e.delete(0,END)
    result=0
    if operation=='+':
        result=int(first)+int(second)
    elif operation=='-':
        result=int(first)-int(second)
    elif operation=='*':
        result=int(first)*int(second)
    elif operation=='/':
        result=int(first)/int(second)
    e.insert(0,result)

def clickClear():
  first=0
  second=0
  operation='$'
  e.delete(0,END)

button1 = Button(root, text='1', padx=10,pady=5,command=lambda: clickNumber(1))
button1.grid(row=1,column=0) 

button2 = Button(root, text='2', padx=10,pady=5,command=lambda: clickNumber(2))
button2.grid(row=1,column=1)

button3 = Button(root, text='3', padx=10,pady=5,command=lambda: clickNumber(3))
button3.grid(row=1,column=2)

buttonp = Button(root, text='+', padx=10,pady=5,command=lambda: clickOperation('+'))
buttonp.grid(row=1,column=3)

button4 = Button(root, text='4', padx=10,pady=5,command=lambda: clickNumber(4))
button4.grid(row=2,column=0) 

button5 = Button(root, text='5', padx=10,pady=5,command=lambda: clickNumber(5))
button5.grid(row=2,column=1)

button6 = Button(root, text='6', padx=10,pady=5,command=lambda: clickNumber(6))
button6.grid(row=2,column=2)

buttonm = Button(root, text='-', padx=10,pady=5,command=lambda: clickOperation('-'))
buttonm.grid(row=2,column=3)

button7 = Button(root, text='7', padx=10,pady=5,command=lambda: clickNumber(7))
button7.grid(row=3,column=0) 

button8 = Button(root, text='8', padx=10,pady=5,command=lambda: clickNumber(8))
button8.grid(row=3,column=1)

button9 = Button(root, text='9', padx=10,pady=5,command=lambda: clickNumber(9))
button9.grid(row=3,column=2)

buttonmm = Button(root, text='*', padx=10,pady=5,command=lambda: clickOperation('*'))
buttonmm.grid(row=3,column=3)

button7 = Button(root, text='CLR', padx=8,pady=5,command=lambda: clickClear())
button7.grid(row=4,column=0) 

buttond = Button(root, text='=', padx=10,pady=5,command=clickEqual)
buttond.grid(row=4,column=1)

button8 = Button(root, text='0', padx=10,pady=5,command=lambda: clickNumber(1))
button8.grid(row=4,column=2)

buttond = Button(root, text='/', padx=10,pady=5,command=lambda: clickOperation('/'))
buttond.grid(row=4,column=3)



root.mainloop()

