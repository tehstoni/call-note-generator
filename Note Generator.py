from tkinter import *

root = Tk()
root.geometry("800x600")
root.title('Note Generator')
root.resizable(0, 0)
root.title("Stoni's note tool")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)


username_label = Label(root, text="Agent Name:")
username_label.grid(column=0, row=0, sticky=W, padx=30, pady=5)

username_entry = Entry(root, exportselection=0, width=70)
username_entry.grid(column=1, row=0, sticky=N, padx=5, pady=5)


customerName_label = Label(root, text="Customer Name")
customerName_label.grid(column=0, row=1, sticky=W, padx=30, pady=5)

customerName_entry = Entry(root, text="Customer Name", exportselection=0, width=70)
customerName_entry.grid(column=1, row=1, sticky=N, padx=5, pady=5)

issue_label = Label(root, text="Issue")
issue_label.grid(column=0, row=2, sticky=W, padx=30, pady=5)

issue_entry = Entry(root, exportselection=0, width=70)
issue_entry.grid(column=1, row=2, sticky=N, padx=5, pady=5)

ticket_label = Label(root, text="Ticket #")
ticket_label.grid(column=0, row=3, sticky=W, padx=30, pady=5)

ticket_entry = Entry(root, exportselection=0, width=70)
ticket_entry.grid(column=1, row=3, sticky=N, padx=5, pady=5)

notes_label = Label(root, text="Notes")
notes_label.grid(column=0, row=4, sticky=W, padx=30, pady=5)

notes_entry = Text(root, exportselection=0, width=70)
notes_entry.grid(column=1, row=4, sticky=N, padx=5, pady=5)

def copy():
    data1 = username_entry.get()
    data2 = customerName_entry.get()
    data3 = issue_entry.get()
    data4 = ticket_entry.get()
    data5 = notes_entry.get("1.0", "end")
    root.clipboard_clear()
    root.clipboard_append("<-Ticket # " + data4 + "Agent's name: " + data1 + " " + "Caller's Name: " + data2 + " " + "Reported Issue: " +data3 + " " +  " " + "Actions Taken: " + data5)

copy_button = Button(root, text="Copy", command=copy, width=70)
copy_button.grid(column=1, row=5, sticky=N, padx=5, pady=5)

def reset():
    customerName_entry.delete("0", END)
    issue_entry.delete("0", END)
    ticket_entry.delete("0", END)
    notes_entry.delete("1.0", END)

reset_button = Button(root, text="Reset", command=reset, width=70)
reset_button.grid(column=1, row=6, sticky=N, padx=5, pady=5)

root.mainloop()