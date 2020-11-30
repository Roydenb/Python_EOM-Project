from tkinter import *
from tkinter import messagebox
from datetime import *
from random import sample

# Fuction that will have the game started
def game_time():
    Loggedin = Tk()
    Loggedin.title("Lotto")

    # heading frame
    main_lbl = Label(Loggedin, text="Ithuba National Lottery")
    main_lbl.configure(font=("FreeMono", 18, "bold"), bg="yellow")
    main_lbl.place(x=95, y=0)

    important_notice = Label(Loggedin, text="PLEASE NOTE:")
    important_notice.configure(font=("bold"), bg="yellow")
    important_notice.place(x=190, y=30)

    notice_continue = Label(Loggedin, text="1.You can only choose between \n1 and 49 \n2.Duplicated numbers is not allowed.", bg="yellow", font="bold")
    notice_continue.place(x=100, y=50)

    # Label to inform user to insert there numbers
    lbl1 = Label(Loggedin, text="Insert your numbers.")
    lbl1.configure(font=("FreeMono", 15, "bold"),bg="yellow")
    lbl1.place(x=145, y=120)


    # Entries for user to insert there numbers
    e1 = Entry(Loggedin)
    e1.configure(bd=2, width=4)
    e1.place(x=145, y=150)
    e2 = Entry(Loggedin)
    e2.configure(bd=2, width=4)
    e2.place(x=180, y=150)
    e3 = Entry(Loggedin)
    e3.configure(bd=2, width=4)
    e3.place(x=215, y=150)
    e4 = Entry(Loggedin)
    e4.configure(bd=2, width=4)
    e4.place(x=250, y=150)
    e5 = Entry(Loggedin)
    e5.configure(bd=2, width=4)
    e5.place(x=285, y=150)
    e6 = Entry(Loggedin)
    e6.configure(bd=2, width=4)
    e6.place(x=320, y=150)

    # Error handling,
    # when user don't insert any numbers it don't allow them to go any further
    def lotto_list():
        try:
            number_1 = int(e1.get())
            number_2 = int(e2.get())
            number_3 = int(e3.get())
            number_4 = int(e4.get())
            number_5 = int(e5.get())
            number_6 = int(e6.get())
            list_1 = number_1, number_2, number_3, number_4, number_5, number_6
            return list_1
        except ValueError:
               messagebox.showerror("Please note","You need to enter your numbers to play\nNo cheating is allowed \nStart over!!!")
               Loggedin.withdraw()

    # heading for random numbers/lotto numbers
    head = Label(Loggedin, text="& the LOTTO numbers is...")
    head.configure(font=("FreeMono", 15, "bold"),bg="yellow")
    head.place(x=145, y=180)

    # Creating and placing the labels for the random numbers/lotto numbers
    lotto_number1_lbl = Label(Loggedin, width=4, bg="yellow")
    lotto_number1_lbl.place(x=145, y=210)
    lotto_number2_lbl = Label(Loggedin, width=4, bg="yellow")
    lotto_number2_lbl.place(x=180, y=210)
    lotto_number3_lbl = Label(Loggedin, width=4, bg="yellow")
    lotto_number3_lbl.place(x=215, y=210)
    lotto_number4_lbl= Label(Loggedin, width=4, bg="yellow")
    lotto_number4_lbl.place(x=250, y=210)
    lotto_number5_lbl = Label(Loggedin, width=4, bg="yellow")
    lotto_number5_lbl.place(x=285, y=210)
    lotto_number6_lbl = Label(Loggedin, width=4, bg="yellow")
    lotto_number6_lbl.place(x=320, y=210)

        # Configuring the labels for the random numbers/lotto numbers
    def lotto_numbers_is():
        lotto = sample(range(1, 49), 7)
        lotto.sort()
        lotto_number6_lbl.configure(text=lotto[5])
        lotto_number1_lbl.configure(text=lotto[0], bg="red")
        lotto_number2_lbl.configure(text=lotto[1], bg="purple")
        lotto_number3_lbl.configure(text=lotto[2], bg="orange")
        lotto_number4_lbl.configure(text=lotto[3], bg="blue")
        lotto_number5_lbl.configure(text=lotto[4], bg="green")
        lotto_number6_lbl.configure(text=lotto[5], bg="purple")
        play_lotto.configure(state=DISABLED)

        # Comparing the numbers with one another
        # Informing if a user win something or wins nothing at all
        count = 0
        for number in lotto_list():
            if number in lotto:
                count += 1
        if count < 2:
            messagebox.showinfo("Sorry","Try again next time")
        elif count == 2:
            messagebox.showinfo("Well done you have 2 right","You win\n" "R20.00")
        elif count == 3:
            messagebox.showinfo("Well done you have 3 right","You win\n" "R100.50")
        elif count == 4:
            messagebox.showinfo("Well done you have 4 right","You win\n" "R2,384.00")
        elif count == 5:
            messagebox.showinfo("Well done you have 5 right","You win\n" "8,584.00")
        elif count == 6:
            messagebox.showinfo("!!!You a full on winner!!!","You won yourself a\n" "R10, 000 000.00")
        return lotto


    now = datetime.datetime.now()

    def append():
        # Appending text file
        f = open("Lotto.txt", "a+")
        f.write("The lotto numbers are: " + str(lotto_numbers_is()) + " " + "The Users numbers: " +
                str(lotto_list()) + " " + "Numbers user guessed right: " + " " + "Time: " + str(now) + "\n")
        f.close()



    # Button to play lotto.
    # Will append the text file as well.
    play_lotto = Button(Loggedin, text="Lotto numbers")
    play_lotto.configure()
    play_lotto.place(x=10, y=250)
    play_lotto.configure(command=append)


    Loggedin.configure(bg="yellow")
    Loggedin.geometry('500x500')
    Loggedin.mainloop()


import datetime
#Fuction for the log in part to show in the text file
now = datetime.datetime.now()


def age():
    #appending text
    f = open("Lotto.txt", "a+")
    f.write(name_ent.get() + " " + surname_ent.get() + " " + "DOB:" + birth_year_ent.get() + " " +
            birth_month_ent.get() + " " + birth_day_ent.get() +" " + "Logged on at: " + str(now) + "\n")
    f.close()

    #Getting the users DOB input
    year_of_bday = int(birth_year_ent.get())
    month_of_bday = int(birth_month_ent.get())
    day_of_bday = int(birth_day_ent.get())
    b_date = datetime.date(year_of_bday, month_of_bday, day_of_bday)
    today = datetime.date.today()

    #allows a user thats over 18 to play
    #And it avoid underage parties to play
    age = today.year - b_date.year
    if age > 18:
       messagebox.showinfo("Welcome", "You have successfully \n""Logged in \n""!!!Best of luck!!!")
       Login.destroy()
       game_time()
    else:
        messagebox.showerror("Please NOTE","No one under 18 \nis allowed to \npartake in playing \nLOTTO")

# Exits the program
def quit():
    Login.destroy()


# First window
# Where the user need to Login
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

#DOB guide/ Layout the DOB need to be entered
dob_guide_lbl = Label(Login, text="yyyy/mm/dd: ")
dob_guide_lbl.configure(font=("Ariel",13, "bold"), bg="white")
dob_guide_lbl.place(x=30, y=150)

#DOB label
# This is like a heading to indicate here the DOB
# information is needed
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
login_btn = Button(Login, text="LOGIN", command=age)
login_btn.configure(bd=2)
login_btn.place(x=190, y=200)

#Quit Button/ Exit Button.
quit_btn = Button(Login, text="EXIT")
quit_btn.configure(bd=2, command=quit)
quit_btn.place(x=260, y=200)


Login.config(bg="white")
Login.geometry('500x250')
Login.mainloop()
