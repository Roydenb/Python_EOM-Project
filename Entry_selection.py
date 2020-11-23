from tkinter import *
window=Tk()
window.title("Insert your numbers")

main_lbl= Label(text="Enter your numbers\n Ranging from 1 -49")
main_lbl.pack()

first_num= Entry()
first_num.pack()

second_num= Entry()
second_num.pack()

third_num= Entry()
third_num.pack()

fourth_num= Entry()
fourth_num.pack()

fifth_num= Entry()
fifth_num.pack()

last_num= Entry()
last_num.pack()

submit_btn= Button(text="Submit")
submit_btn.pack()

mainloop()
