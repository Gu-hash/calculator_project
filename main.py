import tkinter as tk

#Creating the frame for the calculator
frame = tk.Tk()
frame.title("Calculator")

#Creating an entry textbox
#entry = tk.Entry(frame, width=40)
#entry.pack(pady=10)
textbox = tk.Text(frame, height=20, width=40)
textbox.pack()

frame.mainloop() #starts the event loop