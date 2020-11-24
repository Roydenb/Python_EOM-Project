# Ithuba National Lottery of South
from tkinter import *
from tkinter import messagebox
import random
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
       messagebox.showerror(message, "Sorry, not allowed to play")
       window.withdraw()


    elif int(age_ent.get()) >= 18:
         window.withdraw()

         new=Tk()
         new.title("***Lets play some Lotto***")
         new.geometry("1000x1000")

         logged_in= Label(new,text="Welcome\n" +  full_name_ent.get(),fg="red")
         logged_in.pack()

         lotto_start= Label(new,text="Choose your numbers between \n 1 and 49:")
         lotto_start.pack()

         first_num= Entry(new)
         first_num.pack()

         second_num= Entry(new)
         second_num.pack()

         third_num= Entry(new)
         third_num.pack()

         fourth_num= Entry(new)
         fourth_num.pack()

         fifth_num= Entry(new)
         fifth_num.pack()

         last_num= Entry(new)
         last_num.pack()

def lotto_numbers():
    last_window=Tk()
    last_window.title("This is the lotto numbers")

    random_list = random.sample(range(1, 49), 6) # winning lotto numbers
    lotto_nums=Label(random_list)
    lotto_nums.pack()


random_numbers= Button(text="Lotto numbers")
random_numbers.pack()

login_btn= Button(text="Login",command=log_in)
login_btn.pack()





mainloop()
