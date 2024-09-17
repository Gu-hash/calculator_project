import tkinter as tk
from tkinter import *

expression = ""

def click(num):
    global expression

    expression += str(num)
    

#Creating the frame for the calculator
frame = tk.Tk()
frame.title("Calculator")
frame.geometry("300x400")


#Creating an entry label
result = Label(frame, width=25, height= 2, text="", font=("arial", 30))
result.pack()

#textbox = tk.Text(frame, height=20, width=40)
#textbox.pack()

#Creating grid to place widgets
#entry.grid(columnspan=4, rowspan=4, ipadx=70)

#Creating buttons
button1 = Button(frame, text=' 7 ', fg='blue',bg='gold', command=lambda: click(7), height=1, width=5, font=("arial",20, "bold")).place(x=10,y=100)
#button1.grid(row= 0, column= 0)
button2 = Button(frame, text=' 8 ', fg='blue',bg='gold', command=lambda: click(8), height=1, width=5)
#button2.grid(row= 0, column= 1)
button3 = Button(frame, text=' 9 ', fg='blue',bg='gold', command=lambda: click(9), height=1, width=5)
#button3.grid(row= 0, column= 2)
button4 = Button(frame, text=' / ', fg='blue',bg='gold', command=lambda: click('/'), height=1, width=5)
#button4.grid(row= 0, column= 3)
button5 = Button(frame, text=' 4 ', fg='blue',bg='gold', command=lambda: click(4), height=1, width=5)
#button5.grid(row= 1, column= 0)
button6 = Button(frame, text=' 5 ', fg='blue',bg='gold', command=lambda: click(5), height=1, width=5)
#button6.grid(row= 1, column= 1)
button7 = Button(frame, text=' 6 ', fg='blue',bg='gold', command=lambda: click(6), height=1, width=5)
#button7.grid(row= 1, column= 2)
button8 = Button(frame, text=' x ', fg='blue',bg='gold', command=lambda: click('*'), height=1, width=5)
#button8.grid(row= 1, column= 3)
button9 = Button(frame, text=' 1 ', fg='blue',bg='gold', command=lambda: click(1), height=1, width=5)
#button9.grid(row= 2, column= 0)
button10 = Button(frame, text=' 2 ', fg='blue',bg='gold', command=lambda: click(2), height=1, width=5)
#button10.grid(row= 2, column= 1)
button11 = Button(frame, text=' 3 ', fg='blue',bg='gold', command=lambda: click(3), height=1, width=5)
#button11.grid(row= 2, column= 2)
button12 = Button(frame, text=' - ', fg='blue',bg='gold', command=lambda: click('-'), height=1, width=5)
#button12.grid(row= 2, column= 3)
button13 = Button(frame, text=' 0 ', fg='blue',bg='gold', command=lambda: click(0), height=1, width=5)
#button13.grid(row= 3, column= 0)
button14 = Button(frame, text=' . ', fg='blue',bg='gold', command=lambda: click('.'), height=1, width=5)
#button14.grid(row= 3, column= 1)
button15 = Button(frame, text=' C ', fg='blue',bg='gold', command=lambda: click('C'), height=1, width=5)
#button15.grid(row= 3, column= 2)
button16 = Button(frame, text=' + ', fg='blue',bg='gold', command=lambda: click('+'), height=1, width=5)
#button16.grid(row= 3, column= 3)
frame.mainloop() #starts the event loop