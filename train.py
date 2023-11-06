from tkinter import *
from tkinter import messagebox
vk = Tk()
vk.title("interface")
vk.geometry("300x300")
vk.resizable(False,False)
vk.configure(bg="red")
def login():
    username=entry1.get()
    password=entry2.get()
    if(username==""and password==""):
        messagebox.showerror("error","blank not allowed")
    elif(username==""):
      messagebox.showinfo("error","please enter user name")
    elif(password==""):
     messagebox.showinfo("error","please enter password ")
    elif(username=="yash mishra"and password=="1234"):
       messagebox.showinfo("succes","Login succesfull!!")
    else:
       messagebox.showerror("OOPS","Invalid username/password")

#label
Label(vk,text="login page",font="italics 20 bold",bg="blue",fg="yellow").pack(fill=X)
Label(vk,text="Username").place(x=50,y=60)
Label(vk,text="password").place(x=50,y=120)
#entry

entry1=Entry(vk,bd=4,bg="green")
entry1.place(x=130,y=60)
entry2=Entry(vk,bd=4,bg="green",show="*")
entry2.place(x=130,y=120)
#button
Button(vk,text="login",bg="purple",bd=8,command=login).place(x=120,y=190)

mainloop()