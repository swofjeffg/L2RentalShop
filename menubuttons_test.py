from tkinter import *
from tkinter import filedialog as file
import csv

root = Tk()
root.title('Test for menu buttons')

def load_savefile():
    filename = file.askopenfilename(title='Open a file', initialdir='/', defaultextension='.csv', filetypes=[("CSV Files",'*.csv')])
    print("I can load files")

def save_savefile():
    filename = file.asksaveasfile(title='Save a file', initialdir='/', defaultextension='.csv', filetypes=[("CSV Files",'*.csv')])
    print("I can save files")

menu_frame = Frame(root)
menu_title = Label(menu_frame, text="Menu", font="Arial 24 bold")
load_button = Button(menu_frame, text="Load", command=lambda: load_savefile())
save_button = Button(menu_frame, text="Save", command=lambda: save_savefile())
quit_button = Button(menu_frame, text="Quit", command=root.destroy)

menu_frame.grid(pady=20, padx=200, sticky='ew')
menu_title.grid(pady=20, sticky='ew')
load_button.grid(row=1, pady=20, sticky='ew')
save_button.grid(row=2, pady=20, sticky='ew')
quit_button.grid(row=3, pady=20, sticky='ew')

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()