from tkinter import *
from tkinter import ttk
import datetime
import csv

root = Tk()
root.title("TTK widgets test")

tabs = ttk.Notebook(root)
tabs.pack()

# Menu state
menu_frame = Frame(tabs)
menu_label = Label(menu_frame, text="Hello!").pack(expand=True)
menu_frame.pack(fill=BOTH)

# Treeview state
treeview_frame = Frame(tabs)
treeFrame = Frame(treeview_frame)
rentalScrollbar = Scrollbar(treeFrame)

rentalTree = ttk.Treeview(treeFrame, yscrollcommand=rentalScrollbar.set)
rentalTree['columns'] = ('date', 'name', 'receipt', 'item rented', 'rented amount')
rentalTree.column('#0', width=0, stretch=NO)    # Invisbile column for parent/child rows
rentalTree.column('date', anchor=W, width=150, minwidth=50)
rentalTree.column('name', anchor=W, width=150, minwidth=50)
rentalTree.column('receipt', anchor=W, width=150, minwidth=50)
rentalTree.column('item rented', anchor=W, width=150, minwidth=50)
rentalTree.column('rented amount', anchor=W, width=150, minwidth=50)
rentalTree.heading('#0')
rentalTree.heading('date', text="Date & Time", anchor=CENTER)
rentalTree.heading('name', text="Customer name", anchor=CENTER)
rentalTree.heading('receipt', text="Receipt number", anchor=CENTER)
rentalTree.heading('item rented', text="Item rented", anchor=CENTER)
rentalTree.heading('rented amount', text="Quantity rented", anchor=CENTER)

rentalScrollbar.configure(command=rentalTree.yview)
treeFrame.grid(pady=10, padx=10, sticky='ew')
rentalScrollbar.grid(row=0, column=1, sticky='nesw')
rentalTree.grid(row=0, column=0, sticky='ew')
treeview_label = Label(treeview_frame, text="Hello! 2").grid(pady=20)
treeview_frame.pack(fill=BOTH)

# Adding tabs aka states
tabs.add(menu_frame, text="Menu")
tabs.add(treeview_frame, text="Treeview")

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()