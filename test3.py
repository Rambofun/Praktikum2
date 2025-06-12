from tkinter import *

def open_new_window():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("New Window")
    new_window.geometry("250x150")
    root.destroy()  # Close the old window

root = Tk()
root.title("Main Window")
root.geometry("300x200")

button = Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=10)

root.mainloop()
