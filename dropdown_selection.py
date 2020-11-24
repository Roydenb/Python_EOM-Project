from tkinter import *

from tkinter import ttk

window=Tk()
window.title("Lets play some LOTTO")

main_lbl= Label(text= "You can select any numbers from 1 - 49: ")
main_lbl.pack()

number_1_ent= ttk.Combobox(values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_1_ent.pack()

number_2_ent= ttk.Combobox (values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_2_ent.pack()

number_3_ent= ttk.Combobox(values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_3_ent.pack()

number_4_ent= ttk.Combobox(values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_4_ent.pack()

number_5_ent= ttk.Combobox(values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_5_ent.pack()

number_6_ent= ttk.Combobox(values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
        ,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], justify=CENTER)
number_6_ent.pack()

def lotto_numbers():
    # lotto_window=Tk()
    # lotto_window.title("And here is the numbers")

    your_numbers= Label(number_1_ent.get()+number_2_ent.get())
    your_numbers.pack()

selected_numbers_btn= Button(text="Submit", command= lotto_numbers)
selected_numbers_btn.pack()




mainloop()
