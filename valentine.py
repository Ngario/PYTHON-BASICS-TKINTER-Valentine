import tkinter as tk
from tkinter import *
import tkinter.messagebox

#tkinter root window
root = tk.Tk()

root.geometry("500x500")
root.title("My Valentine Date")

#name = input("Enter your valentine name")
# Create a messagebox showinfo
def onClick():
    tkinter.messagebox.showinfo("Hey Salma, Will you be my valentine?")

# Create a Button
button = Button(root, text="Click Me Baby", command=onClick, height=3, width=17)

# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()
