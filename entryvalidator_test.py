from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Entry Validation tests")

def interger_validator():   # Function that checks if inputted number is an interger
    print("Validating interger input...")
    try:
        pop = 0
        while pop != 1: # Getting rid of blank spaces at the beginning
            if len(interger_entry.get()) == 0:
                print("Interger entry left blank")
                raise TypeError
            elif interger_entry.get()[0] == " ":
                interger_entry.delete(0)
            elif interger_entry.get()[0] != " ":
                pop += 1
        int(interger_entry.get())
        print("All interger tests passed! {} is an interger!".format(interger_entry.get()))
        interger_entry.delete(0, 'end')
    except TypeError:
        print("TypeError | Most likely Interger entry left blank")
    except ValueError:
        print("ValueError | Interger entry not an interger")
        interger_entry.delete(0, 'end')
    except:
        print("Interger entry error")

def word_validator():   # Word validation is a lot harder, so I'll only be testing blanks
    print("Validating word input...")
    try:
        pop = 0
        while pop != 1: # Getting rid of blank spaces at the beginning
            if len(word_entry.get()) == 0:
                print("Word entry left blank")
                raise TypeError
            elif word_entry.get()[0] == " ":
                word_entry.delete(0)
            elif word_entry.get()[0] != " ":
                pop += 1
        print("All word tests passed! {} is a word!".format(word_entry.get()))
        word_entry.delete(0, 'end')
    except TypeError:
        print("TypeError | Most likely Word entry left blank")
    except:
        print("Word entry error")


frame = Frame(root)

word_label = Label(frame, text="Enter a word:").grid(row=0, column=0)
word_entry = Entry(frame)
word_entry.grid(row=1, column=0)
word_add = Button(frame, text="Submit", command=lambda: word_validator()).grid(row=2, column=0)

interger_label = Label(frame, text="Enter a interger:").grid(row=0, column=1)
interger_entry = Entry(frame)
interger_entry.grid(row=1, column=1)
interger_add = Button(frame, text="Submit", command=lambda: interger_validator()).grid(row=2, column=1)

frame.pack(pady=20, padx=20)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()