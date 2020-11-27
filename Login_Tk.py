from tkinter import*
#Login
Login = Tk()
Login.title("Welcome to our Lotto App")

#Heading
heading_lbl = Label(Login, text="Login and play some LOTTO!!!")
heading_lbl.configure(font=("FreeMono", 16, "bold"), bg="white")
heading_lbl.place(x=100, y=0)

# Name label and entry
name_lbl = Label(Login, text="Name: ")
name_lbl.configure(font=("FreeMono", 13, "bold"), bg="white")
name_lbl.place(x=30, y=50)
name_ent = Entry(Login)
name_ent.configure(width=40)
name_ent.place(x=150, y=50)

# surname label and entry
surname_lbl = Label(Login, text="Surname: ")
surname_lbl.configure(font=("FreeMono", 13, "bold"), bg="white")
surname_lbl.place(x=30, y=90)
surname_ent = Entry(Login)
surname_ent.configure(width=40)
surname_ent.place(x=150, y=90)

#DOB guide/ Layout
dob_guide_lbl = Label(Login, text="yyyy/mm/dd: ")
dob_guide_lbl.configure(font=("Ariel",13, "bold"), bg="white")
dob_guide_lbl.place(x=30, y=150)

#DOB label
dob_lbl = Label(Login, text="Date Of Birth")
dob_lbl.configure(font=("FreeMono", 13, "bold"), bg="white")
dob_lbl.place(x=30, y=120)

# Entry for the year the user
birth_year_ent = Entry(Login, width=5)
birth_year_ent.place(x=180, y=150)

# Entry for the month the user
birth_month_ent = Entry(Login, width=3)
birth_month_ent.place(x=225, y=150)

# Entry for the day the user
birth_day_ent = Entry(Login, width=3)
birth_day_ent.place(x=255, y=150)

# Login Button
login_btn = Button(Login, text="LOGIN")
login_btn.configure(bd=2)
login_btn.place(x=190, y=200)

#Quit Button
quit_btn = Button(Login, text="EXIT")
quit_btn.configure(bd=2, command=quit)
quit_btn.place(x=260, y=200)


Login.config(bg="white")
Login.geometry('500x250')
Login.mainloop()
