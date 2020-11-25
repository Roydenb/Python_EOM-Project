from tkinter import*

new=Tk()

all_the_entries=[]

def something():
    int(users_numbers.get())
    for  numbers in all_the_entries:
         your_numbers.config(text= numbers)

for x in range(6):
    users_numbers=Entry(new)
    users_numbers.pack()
    all_the_entries.append(users_numbers)

your_numbers= Label(new,text= "Your numbers is\n" )
your_numbers.pack()

button=Button(text="Click Me",command=something)
button.pack()

mainloop()


 # num=[]
 #
 #    for x in range(6):
 #        entries=Entry(new)
 #        entries.pack()
 #        continue
 #



    # for all_entries in entries:
    #     entry_list="" + entries.get()
    #     entry_list= entry_list + int(entries.get())
    #     your_numbers.config(text= entry_list)
    #
    #     all_entries.append(entries)
    #
    #     button=Button(text="Click Me")
    #     button.pack()
    #
    #     your_numbers= Label(new)
    #     your_numbers.pack()
    #     return  entry_list

