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

         random_numbers= Button(new,text="Lotto numbers",command=check_winning_count)
         random_numbers.pack()

         final_button= Button(new,text="Generate",command=check_winnings)
         final_button.pack()

         my_entry_list= int(first_num.get()),int(second_num.get()),int(third_num.get()),int(fourth_num.get()),int(fifth_num.get()),int(last_num.get())
         return my_entry_list


def check_winning_count():
    random_list = random.sample(range(1, 49), 6) # winning lotto numbers

    lbl1= Label()
    lbl1.pack()

    lbl2= Label()
    lbl2.pack()

    lbl3= Label()
    lbl3.pack()

    lbl4= Label()
    lbl4.pack()

    lbl5= Label()
    lbl5.pack()

    lbl6= Label()
    lbl6.pack()

    count = 0
    for num in random_list :
        if num in random_list:
            count = count + 1
            return count

def check_winnings():
    count = check_winning_count()
    if count < 2:
       messagebox.showinfo("Sorry, try again next time.")
    if count == 2:
       messagebox.showinfo("Well done you have 2 right\nYou win\nR20.00")
    if count == 3:
       messagebox.showinfo("Well done you have 3 right\nYou win\n R100.50")
    if count == 4:
       messagebox.showinfo("Well done you have 4 right\nYou win\n R2,384.00")
    if count == 5:
       messagebox.showinfo("Well done you have 5 right\nYou win\n 8,584.00")
       breakpoint()
    if count == 6:
       messagebox.showinfo("You win\n R10, 000 000.00")

login_btn= Button(text="Login",command=log_in)
login_btn.pack()

mainloop()
