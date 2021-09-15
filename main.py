# v0.1
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
global fileopened
fileopened = BooleanVar()

# creating functions
def load_savefile():    # function that allows user to open pre-existing '.csv' files for use
    if treeview.get_children():
        print("File already loaded, clear all before loading a new file")
    else:
        filename = fd.askopenfilename(title="Load a save", initialdir=path, defaultextension='.csv', filetypes=[('CSV Files','*.csv')])
        try:
            with open(filename, 'r') as f:
                variables = csv.DictReader(f)
                try:
                    iid = 0
                    for row in variables:
                        treeview.insert(parent='', index='end', iid=iid, text="", values=(row['date'], row['name'], row['receipt'], row['item_rented'], row['rented_amount']))
                        iid += 1
                    tabs.select(1)
                except:
                    print("Selected CSV file incorrectly formatted, to see accepted CSV file formatting, please create a new file using this program\nSelected file: (%s)"%filename)
        except:
            print("No file selected")

def create_savefile():  # function that allows user to create a new '.csv' file
    if treeview.get_children():
        print("Save data before creating a new save")
    else:
        filename = fd.asksaveasfile(title='Create a file', initialdir=path, defaultextension='.csv', filetypes=[("CSV Files",'*.csv')])
        tabs.select(1)

def add_data(): # function that adds data to the treeview
    iid=0
    pop=0
    while pop == 0:
        try:
            treeview.insert(parent='', index='end', iid=iid, text="", values=(datetime.datetime.now().strftime("%d-%m-%Y | %H:%M"), name_entry.get(), receipt_entry.get(), item_entry.get(), amount_entry.get()))
            pop+=1
        except:
            iid+=1

def remove_selected():  # function that removes only selected items in the treeview
    selected = treeview.selection()
    if selected != 0:
        for i in selected:
            treeview.delete(i)

def remove_all():   # function that removes all entries from the treeview
    for i in treeview.get_children():
        treeview.delete(i)

def manual_save():
    pass

def auto_save():
    pass

# creating gui
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)

# menu state
menu_frame = Frame(tabs)
menu_title = Label(menu_frame, text="Menu", font="Arial 24 bold").grid(row=0, pady=20, padx=20, sticky='ew')
start_button = Button(menu_frame, text="Start new save", command=lambda: create_savefile()).grid(row=1, pady=10, padx=330, sticky='ew')
load_button = Button(menu_frame, text="Load save", command=lambda: load_savefile()).grid(row=2, pady=10, padx=330, sticky='ew')
save_button = Button(menu_frame, text="Quit", command=lambda: root.destroy()).grid(row=3, pady=10, padx=330, sticky='ew')
menu_frame.columnconfigure(0, weight=1)
menu_frame.pack(fill=BOTH)

# treeview state
treeview_frame = Frame(tabs)
# treeview itself + scrollbar
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
tree_scroll.grid(row=0, column=1, sticky='nesw')
treeview.grid(row=0, column=0, sticky='nesw')
tree_frame.grid(row=0, pady=10)
# treeview entries
entry_frame = Frame(treeview_frame)
time_label = Label(entry_frame, text="Time").grid(row=0, column=0, padx=10)
time_entry = Label(entry_frame, text="")
time_entry.grid(row=1, column=0, padx=10)
name_label = Label(entry_frame, text="Name").grid(row=0, column=1, padx=10)
name_entry = Entry(entry_frame)
name_entry.grid(row=1, column=1, padx=10)
receipt_label = Label(entry_frame, text="Receipt").grid(row=0, column=2, padx=10)
receipt_entry = Entry(entry_frame)
receipt_entry.grid(row=1, column=2, padx=10)
item_label = Label(entry_frame, text="Item rented").grid(row=0, column=3, padx=10)
item_entry = Entry(entry_frame)
item_entry.grid(row=1, column=3, padx=10)
amount_label = Label(entry_frame, text="Rented amount").grid(row=0, column=4, padx=10)
amount_entry = Entry(entry_frame)
amount_entry.grid(row=1, column=4, padx=10)
add_button = Button(entry_frame, text="Add", command=lambda: add_data()).grid(row=1, column=5, padx=10)
entry_frame.grid(row=1, pady=10)
# treeview commands
command_frame = Frame(treeview_frame)
clear_selected_button = Button(command_frame, text="Remove selected", command=lambda: remove_selected()).grid(padx=10)
clear_all_button = Button(command_frame, text="Clear all", command=lambda: remove_all()).grid(row=0, column=1, padx=10)
save_button = Button(command_frame, text="Save", command=lambda: manual_save()).grid(row=0, column=2, padx=10)
command_frame.grid(row=2, pady=10)
treeview_frame.columnconfigure(0, weight=1)
treeview_frame.pack(fill=BOTH)

# adding widgets to individual tabs/states
tabs.add(menu_frame, text="Menu")
tabs.add(treeview_frame, text="Treeview")

# clock function to update time
def tick():
    if '.5' in str(int(datetime.datetime.now().strftime("%S"))/2):  # update the clock on the treeview to display its actually doing something
        time_entry.configure(text="{}".format(datetime.datetime.now().strftime("%d-%m-%Y | %H:%M")))
    else:
        time_entry.configure(text="{}".format(datetime.datetime.now().strftime("%d-%m-%Y | %H %M")))
    root.after(1000, tick)   # called every 1s for accuracy
tick()

# "disabling" resizing smaller than widget size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()