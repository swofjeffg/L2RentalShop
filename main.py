# v0.6
"""
Application Program for AS91896 Internal
"""

# import libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import datetime
import csv
import pathlib

root = Tk()
root.title("Julie's Rental Shop")
path = pathlib.Path(__file__).parent.resolve()
current_save = "No file selected"

# creating functions
def error_popup(msg):  # function that popups up an error message
    print(msg)
    messagebox.showerror(title='Error', message=msg)

def load_savefile():    # function that allows user to open pre-existing '.csv' files created by this program for use
    if treeview.get_children():
        error_popup("File already loaded, clear all before loading a new file.")
    else:
        filename = fd.askopenfilename(title="Load a save", initialdir=path, defaultextension='.csv', filetypes=[('CSV Files','*.csv')])
        try:
            with open(filename, 'r') as f:
                variables = csv.DictReader(f)
                try:
                    iid = 0
                    for row in variables:   # minimal error checking as we trust the end-user hasn't tampered with the file
                        treeview.insert(parent='', index='end', iid=iid, text='', values=(row['date'], row['name'], int(row['receipt']), row['item_rented'], int(row['rented_amount'])))
                        iid += 1
                    tabs.select(1)
                    global current_save
                    current_save = filename
                except:
                    error_popup("Selected CSV file incorrectly formatted, to see accepted CSV file formatting, please create a new file using this program.\n\nSelected file: (%s)"%filename)
        except:
            error_popup("No file selected.")

def create_savefile():  # function that allows user to create a new '.csv' file
    if treeview.get_children():
        error_popup("File already loaded, clear all before loading a new file.")
    else:
        try:
            filename = str(fd.asksaveasfile(title='Create a file', initialdir=path, defaultextension='.csv', filetypes=[("CSV Files",'*.csv')])).split("='")[1].split("' ")[0]
            with open(filename, 'w', newline='') as f:
                fieldnames = ['date', 'name', 'receipt', 'item_rented', 'rented_amount']
                csv_dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
                csv_dict_writer.writeheader()
            tabs.select(1)
            global current_save
            current_save = filename
        except:
            error_popup("Failed to start new save.")

def add_data(): # function that adds data to the treeview
    global current_save
    errors = False
    if current_save == "No file selected":
        errors = True
        error_popup("No file selected!!")
    iid = 0
    for i in treeview.get_children():
        iid += 1
    if len(name_entry.get().strip()) or len(receipt_entry.get().strip()) or len(item_entry.get().strip()) or len(amount_entry.get().strip()) == 0:
        if len(name_entry.get().strip()) == 0:
            errors = True
            error_popup("Name was left blank.")
        if len(receipt_entry.get().strip()) == 0:
            errors = True
            error_popup("Receipt was left blank.")
        if len(item_entry.get().strip()) == 0:
            errors = True
            error_popup("Item was left blank.")
        if len(amount_entry.get().strip()) == 0:
            errors = True
            error_popup("Amount was left blank.")
    try:
        int(receipt_entry.get().strip())
        if int(receipt_entry.get().strip()) <= 0:
            errors = True
            error_popup("Receipt entry is a negative number.")
    except:
        errors = True
        error_popup("Receipt entry not an interger.")
    try:
        int(amount_entry.get().strip())
        if int(amount_entry.get().strip()) <= 0:
            errors = True
            error_popup("Amount entry is a negative number.")
        if int(receipt_entry.get().strip()) > 500:
            errors = True
            error_popup("Amount entry is greater than 500.")
    except:
        errors = True
        error_popup("Amount entry not an interger.")
    if errors == False:
        treeview.insert(parent='', index='end', iid=iid, text='', values=(datetime.datetime.now().strftime("%d/%m/%Y | %H:%M"), name_entry.get().strip(), receipt_entry.get().strip(), item_entry.get().strip(), amount_entry.get().strip()))
        name_entry.delete(0, 'end')
        receipt_entry.delete(0, 'end')
        item_entry.delete(0, 'end')
        amount_entry.delete(0, 'end')
        save()

def confirm(msg):  # function that sends a popup asking for confirmation for deleting entries
    global current_save
    answer = messagebox.askyesno(title='Confirmation', message='Are you sure you want to {}?\n\nCurrent file is: ({})'.format(msg, current_save))
    if answer:
        return answer

def remove_selected():  # function that removes only selected items in the treeview
    answer = confirm('remove selected')
    if answer:
        selected = treeview.selection()
        if selected != 0:
            for i in selected:
                treeview.delete(i)
        save()

def remove_all():   # function that removes all entries from the treeview
    answer = confirm('remove everything')
    if answer:
        for i in treeview.get_children():
            treeview.delete(i)
    save()

def save():    # function that saves data
    data = []
    for i in treeview.get_children():   # using dicts to and headernames to ensure program recognises this file - not fast but robust
        data.append({'date': treeview.item(i)['values'][0], 'name': treeview.item(i)['values'][1], 'receipt': treeview.item(i)['values'][2], 'item_rented': treeview.item(i)['values'][3], 'rented_amount': treeview.item(i)['values'][4]})
    try:
        with open(current_save, 'w', newline='') as f:
            fieldnames = ['date', 'name', 'receipt', 'item_rented', 'rented_amount']
            csv_dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_dict_writer.writeheader()
            for i in data:
                csv_dict_writer.writerow(i)
    except:
        error_popup("Current save file is missing.\n\nPlease load or start a file in the menu!")

# creating gui
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)

# menu state
menu_frame = Frame(tabs)
menu_center = Frame(menu_frame)
menu_title = Label(menu_center, text="Menu", font="Arial 24 bold").grid(row=0, pady=20, padx=20, sticky='ew')
start_button = Button(menu_center, text="Start new save", command=lambda: create_savefile()).grid(row=1, pady=10, sticky='ew')
load_button = Button(menu_center, text="Load save", command=lambda: load_savefile()).grid(row=2, pady=10, sticky='ew')
save_button = Button(menu_center, text="Quit", command=lambda: root.destroy()).grid(row=3, pady=10, sticky='ew')
menu_center.place(relx=0.5, rely=0.3, anchor=CENTER)
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
treeview.column('date', anchor=W, width=105, minwidth=105)
treeview.column('name', anchor=W, width=150, minwidth=50)
treeview.column('receipt', anchor=W, width=100, minwidth=50)
treeview.column('item rented', anchor=W, width=150, minwidth=50)
treeview.column('rented amount', anchor=W, width=100, minwidth=50)
treeview.heading('#0')
treeview.heading('date', text="Date and time", anchor=CENTER)
treeview.heading('name', text="Customer name", anchor=CENTER)
treeview.heading('receipt', text="Receipt number", anchor=CENTER)
treeview.heading('item rented', text="Item rented", anchor=CENTER)
treeview.heading('rented amount', text="Rented amount", anchor=CENTER)
tree_scroll.configure(command=treeview.yview)
tree_scroll.pack(side=RIGHT, fill=Y)
treeview.pack(side=LEFT, fill=BOTH, expand=TRUE)
tree_frame.grid(row=0, pady=10, sticky='ew')
# treeview entries
entry_frame = Frame(treeview_frame)
time_label = Label(entry_frame, text="Date and time").grid(row=0, column=0, padx=10)
time_entry = Label(entry_frame, text="")
time_entry.grid(row=1, column=0, padx=10)
name_label = Label(entry_frame, text="Customer name").grid(row=0, column=1, padx=10)
name_entry = Entry(entry_frame)
name_entry.grid(row=1, column=1, padx=10)
receipt_label = Label(entry_frame, text="Receipt number").grid(row=0, column=2, padx=10)
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
save_button = Button(command_frame, text="Save", command=lambda: save()).grid(row=0, column=2, padx=10)
command_frame.grid(row=2, pady=10)
treeview_frame.columnconfigure(0, weight=1)
treeview_frame.pack(fill=BOTH)

# adding widgets to individual tabs/states
tabs.add(menu_frame, text="Menu")
tabs.add(treeview_frame, text="Treeview")

# clock function to update time
def tick():
    if '.5' in str(int(datetime.datetime.now().strftime("%S"))/2):  # update the clock on the treeview to display its actually doing something
        time_entry.configure(text="{}".format(datetime.datetime.now().strftime("%d/%m/%Y | %H %M")))
    else:
        time_entry.configure(text="{}".format(datetime.datetime.now().strftime("%d/%m/%Y | %H:%M")))
    root.after(1000, tick)   # called every 1s for accuracy
tick()

# "disabling" resizing smaller than widget size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
# starting app
root.mainloop()