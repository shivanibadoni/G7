#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface."""
from tkinter import *
m = Tk()
label = Label(m, text= "\nHello World\n")
label.pack()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text. 
def write_TEXT():
    print("Acadview Python Training")
button = Button(m,text='Click to See Message',width=50,command = write_TEXT)
button.pack()

#Q3. Create a frame using tkinter with any label text and two buttons. One to exit and other to change the label to some other text. 
r = Tk()
def change_label():
    label2["text"] = "Python Programming "
frame = Frame(r)
frame.pack()
label2 = Label(r,text="\nCLICK TO CONTINUE\n")
label2.pack()
bottomframe = Frame(r)
bottomframe.pack(side=BOTTOM)
stopbutton = Button(frame, text='Abort', width = 30, fg = 'Red', command = r.destroy)
stopbutton.pack(side=LEFT)
printbutton = Button(frame, text='Change Label', width = 30, fg = 'Steel Blue', command=change_label)
printbutton.pack(side=LEFT) 

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
tk = Tk()
def display():
    print(temp1.get()+ " is " +temp2.get())
Label(tk, text = "Enter your name: ").grid(row=0)
Label(tk, text = "Enter AGE: ").grid(row=1)
temp1 = Entry(tk)
temp2 = Entry(tk)
temp.grid(row=0,column=1)
temp.grid(row=1,column=1)
button1 = Button(tk, text='PRINT',width=50,fg='Blue',command=display)
button1.grid(row=4,column=1)

m.mainloop()
