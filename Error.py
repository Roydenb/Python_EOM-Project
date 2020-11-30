from tkinter import*
Loggedin=Tk()
Loggedin.geometry('500x500')
# Label to inform user what to do
lbl1 = Label(Loggedin, text="Insert your numbers.")
lbl1.configure(font=("FreeMono", 15, "bold"),bg="yellow")
lbl1.place(x=145, y=120)

def error_handel():
    try:
        int(e1.get())
        int(e2.get())
        int(e3.get())
        int(e4.get())
        int(e5.get())
        int(e6.get())

    except ValueError:
        # error.configure(text="Numbers can't be higher than 49")
        error.configure(text= "Please enter a number")

# Entry's for user to insert there numbers
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

error= Label(Loggedin)
error.place(x=200, y=200)

generate=Button(text="Lotto",command=error_handel)
generate.pack()

mainloop()
