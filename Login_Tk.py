# Ithuba National Lottery of South
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.title("Login")

full_name_lbl= Label(text="Insert your full name:")
full_name_lbl.pack()
full_name_ent= Entry(justify=CENTER)
full_name_ent.pack()

age_lbl= Label(text="Insert your age: ")
age_lbl.pack()


age_ent= Entry(justify=CENTER)
age_ent.pack()

def log_in():
    if int(age_ent.get()) < 18:
       message = "ALERT"
       messagebox.showerror(message, "You are under age")
       window.withdraw()


    elif int(age_ent.get()) >= 18:
         log= Label(text="Welcome\n" +  full_name_ent.get())
         log.pack()

log_in_btn= Button(text="Login",command=log_in)
log_in_btn.pack()


mainloop()
