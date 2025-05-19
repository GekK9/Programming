import tkinter as Tk

def Add():
    string = Entry.get()
    if string.strip():
        Entry.delete(0, Tk.END)
        Listbox.insert(0, string)

def Delete():
    selected_indices = list(Listbox.curselection())
    selected_indices.reverse()
    for index in selected_indices:
        Listbox.delete(index)
    
def Save():
    with open("list.txt", "w") as f:
        f.write("\n".join(Listbox.get(0, Tk.END)))

window = Tk.Tk()
window.title("Работа со списком")
window.geometry("500x300")


button_frame = Tk.Frame(window)
button_frame.grid(row=1, column=3, padx=10, sticky=Tk.SE)

Listbox = Tk.Listbox(window, width=40, selectmode=Tk.MULTIPLE)
Entry = Tk.Entry(window)
Entry.grid(row=1, column=3, pady=5, padx=(10, 0), sticky=Tk.E)
Button1 = Tk.Button(button_frame, text="Добавить", width=15, command=Add)
Button2 = Tk.Button(button_frame, text="Удалить", width=15, command=Delete)
Button3 = Tk.Button(button_frame, text="Сохранить", width=15, command=Save)

Scrollbar = Tk.Scrollbar(window)
Scrollbar.config(command=Listbox.yview)

Listbox.grid(row=1, column=1, pady=5, padx=(10, 0), sticky=Tk.NSEW)
Listbox["yscrollcommand"] = Scrollbar.set

Button1.pack(pady=5)
Button2.pack(pady=5)
Button3.pack(pady=5)

Scrollbar.grid(row=1, column=2, sticky=Tk.NS, pady=5)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()