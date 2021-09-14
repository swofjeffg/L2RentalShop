"""
Application Program for AS91896 Internal
"""

# import libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import datetime
import csv
import pathlib

root = Tk()
root.title("Julie's Rental Shop")
path = pathlib.Path(__file__).parent.resolve()

# creating functions
def load_savefile():    # function that allows user to open pre-existing '.csv' files for use   
    pass

def create_savefile():  # function that allows user to create a new '.csv' file
    pass

def add_data(): # function that adds data to the treeview
    pass

def remove_selected():  # function that removes only selected items in the treeview
    pass

def remove_all():   # function that removes all entries from the treeview
    pass

# creating gui
tabs = ttk.Notebook(root)
tabs.pack()

# menu state
menu_frame = Frame(tabs)
menu_label = Label(menu_frame, text="Menu").pack(expand=True)
menu_frame.pack(fill=BOTH)

# treeview state
treeview_frame = Frame(tabs)
tree_frame = Frame(treeview_frame)
tree_scroll = Scrollbar(tree_frame)

treeview = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
treeview['columns'] = ('date', 'name', 'receipt', 'item rented', 'rented amount')
treeview.column('#0', width=0, stretch=NO)    # invisbile column for parent/child rows
treeview.column('date', anchor=W, width=150, minwidth=50)
treeview.column('name', anchor=W, width=150, minwidth=50)
treeview.column('receipt', anchor=W, width=150, minwidth=50)
treeview.column('item rented', anchor=W, width=150, minwidth=50)
treeview.column('rented amount', anchor=W, width=150, minwidth=50)
treeview.heading('#0')
treeview.heading('date', text="Date & Time", anchor=CENTER)
treeview.heading('name', text="Customer name", anchor=CENTER)
treeview.heading('receipt', text="Receipt number", anchor=CENTER)
treeview.heading('item rented', text="Item rented", anchor=CENTER)
treeview.heading('rented amount', text="Quantity rented", anchor=CENTER)

tree_scroll.configure(command=treeview.yview)
tree_frame.grid(pady=10, padx=10, sticky='ew')
tree_scroll.grid(row=0, column=1, sticky='nesw')
treeview.grid(row=0, column=0, sticky='ew')
treeview_label = Label(treeview_frame, text="Entry field").grid(pady=20)
treeview_frame.pack(fill=BOTH)

# adding widgets to individual tabs/states
tabs.add(menu_frame, text="Menu")
tabs.add(treeview_frame, text="Treeview")


# "disabling" resizing smaller than widget size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())