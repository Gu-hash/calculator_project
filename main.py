import tkinter as tk
from tkinter import *

#Creating the frame for the calculator
frame = tk.Tk()
frame.title("Calculator")
frame.geometry("370x420")


#Creating an entry label
result = Label(frame, width=25, height= 2, text="", font=("arial", 30))
result.pack()


expression = ""

def click(value):
    global expression
    expression += str(value)
    result.config(text= expression)

def clear():
    global expression
    expression = ""
    result.config(text= expression)

def calculate():
    global expression
    answer = ""
    if expression != "":
        try:
            answer = eval(expression)
        except:
            answer= "error"
            expression = ""
    
    result.config(text= answer)


#textbox = tk.Text(frame, height=20, width=40)
#textbox.pack()

#Creating grid to place widgets
#entry.grid(columnspan=4, rowspan=4, ipadx=70)

#Creating buttons
button1 = Button(frame, text=' 7 ', fg='blue',bg='gold', command=lambda: click(7), height=1, width=4, font=("arial",20, "bold")).place(x=10,y=100)

button2 = Button(frame, text=' 8 ', fg='blue',bg='gold', command=lambda: click(8), height=1, width=4, font=("arial",20, "bold")).place(x=95,y=100)

button3 = Button(frame, text=' 9 ', fg='blue',bg='gold', command=lambda: click(9), height=1, width=4, font=("arial",20, "bold")).place(x=180,y=100)

button4 = Button(frame, text=' / ', fg='blue',bg='gold', command=lambda: click('/'), height=1, width=4, font=("arial",20, "bold")).place(x=265,y=100)
#button4.grid(row= 0, column= 3)
button5 = Button(frame, text=' 4 ', fg='blue',bg='gold', command=lambda: click(4), height=1, width=4, font=("arial",20, "bold")).place(x=10,y=165)
#button5.grid(row= 1, column= 0)
button6 = Button(frame, text=' 5 ', fg='blue',bg='gold', command=lambda: click(5), height=1, width=4, font=("arial",20, "bold")).place(x=95,y=165)
#button6.grid(row= 1, column= 1)
button7 = Button(frame, text=' 6 ', fg='blue',bg='gold', command=lambda: click(6), height=1, width=4, font=("arial",20, "bold")).place(x=180,y=165)
#button7.grid(row= 1, column= 2)
button8 = Button(frame, text=' x ', fg='blue',bg='gold', command=lambda: click('*'), height=1, width=4, font=("arial",20, "bold")).place(x=265,y=165)
#button8.grid(row= 1, column= 3)
button9 = Button(frame, text=' 1 ', fg='blue',bg='gold', command=lambda: click(1), height=1, width=4, font=("arial",20, "bold")).place(x=10,y=230)
#button9.grid(row= 2, column= 0)
button10 = Button(frame, text=' 2 ', fg='blue',bg='gold', command=lambda: click(2), height=1, width=4, font=("arial",20, "bold")).place(x=95,y=230)
#button10.grid(row= 2, column= 1)
button11 = Button(frame, text=' 3 ', fg='blue',bg='gold', command=lambda: click(3), height=1, width=4, font=("arial",20, "bold")).place(x=180,y=230)
#button11.grid(row= 2, column= 2)
button12 = Button(frame, text=' - ', fg='blue',bg='gold', command=lambda: click('-'), height=1, width=4, font=("arial",20, "bold")).place(x=265,y=230)
#button12.grid(row= 2, column= 3)
button13 = Button(frame, text=' 0 ', fg='blue',bg='gold', command=lambda: click(0), height=1, width=4, font=("arial",20, "bold")).place(x=10,y=295)
#button13.grid(row= 3, column= 0)
button14 = Button(frame, text=' . ', fg='blue',bg='gold', command=lambda: click('.'), height=1, width=4, font=("arial",20, "bold")).place(x=95,y=295)
#button14.grid(row= 3, column= 1)
button15 = Button(frame, text=' C ', fg='blue',bg='gold', command=lambda: clear(), height=3, width=4, font=("arial",20, "bold")).place(x=180,y=295)
#button15.grid(row= 3, column= 2)
button16 = Button(frame, text=' + ', fg='blue',bg='gold', command=lambda: click('+'), height=3, width=4, font=("arial",20, "bold")).place(x=265,y=295)
#button16.grid(row= 3, column= 3)
button17 = Button(frame, text=' = ', fg='blue',bg='gold', command=lambda: calculate(), height=1, width=9, font=("arial",20, "bold")).place(x=10,y=360)

frame.mainloop() #starts the event loop