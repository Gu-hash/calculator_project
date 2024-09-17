import tkinter as tk

#Creating the frame for the calculator
frame = tk.Tk()
frame.title("Calculator")
frame.geometry("300x400")

#Creating an entry textbox
entry = tk.Entry(frame, width=50)
entry.pack(pady=10)
#textbox = tk.Text(frame, height=20, width=40)
#textbox.pack()

#Creating grid to place widgets
entry.grid(rowspan=4, columnspan=4)
frame.mainloop() #starts the event loop