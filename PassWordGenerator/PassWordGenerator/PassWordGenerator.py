from ast import Lambda
import secrets
import string
from tkinter import *

#############################################################
###################    PassWord Generator   #################
#############################################################
root=Tk()

e=Entry(root,width=50)
e.pack()
e.insert(0,'enter desired size')

def click():
    res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(int(e.get())))  
    e.delete(0,END)
    e.insert(0,str(res))

button = Button(root, text="submit", padx=10,pady=5,command=click)
button.pack()

root.mainloop()

