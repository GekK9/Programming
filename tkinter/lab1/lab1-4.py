import tkinter as tk

def recycle_insert():
    unit = list(Listbox.curselection())
    unit.reverse()
    for i in range(len(unit)):
        Listbox_of_units.insert(tk.END, Listbox.get(unit[i]))

def recycle_delete():
    ssd = list(Listbox_of_units.curselection())
    ssd.reverse()
    for i in range(len(ssd)):
        Listbox_of_units.delete(ssd[i])
     
def save_list():
    with open("shop.txt", "w", encoding='utf-8') as f:
        f.write("Ваш заказ:\n")
        temp_list = list(Listbox_of_units.get(0, tk.END))
        temp_set = set(temp_list)
        for i in temp_set:
            count = temp_list.count(i)
            f.write(f"{i}: {count} шт.\n")

Window = tk.Tk()
Window.title("Добавление товаров в корзину")
Window["bg"] = "white"

main_frame = tk.Frame(Window, bg="white")
main_frame.pack(pady=20)

button_frame = tk.Frame(main_frame, bg="white")
button_frame.grid(row=0, column=2, padx=10, sticky=tk.NS)

Listbox = tk.Listbox(main_frame, width=40, selectmode=tk.MULTIPLE)
Scrollbar = tk.Scrollbar(main_frame)
Button_1 = tk.Button(button_frame, width=25, text="Добавить в корзину", command=recycle_insert)
Button_2 = tk.Button(button_frame, width=25, text="Удалить из корзины", command=recycle_delete)
Button_3 = tk.Button(button_frame, width=25, text="Оформить заказ", command=save_list)
Listbox_of_units = tk.Listbox(main_frame, width=40)

Listbox["yscrollcommand"] = Scrollbar.set
Scrollbar.config(command=Listbox.yview)

books = [
    'Самоучитель Java', 'Самоучитель C++', 'Самоучитель Python',
    'Самоучитель C#', 'Самоучитель JavaScript', 'Самоучитель PHP',
    'Самоучитель FORTRAN', 'Самоучитель Rubi', 'Самоучитель Go', 
    'Самоучитель Objective-C', 'Самоучитель Linux', 'Самоучитель Rust',
    'Самоучитель Windows', 'Самоучитель Unity', 'Самоучитель UE5',
]

for book in books:
    Listbox.insert(tk.END, book)

Listbox.grid(row=0, column=0, padx=(0, 1), pady=5, sticky=tk.NS)
Scrollbar.grid(row=0, column=1, pady=5, sticky=tk.NS)

Button_1.pack(pady=5)
Button_2.pack(pady=5)
Button_3.pack(pady=5)

Listbox_of_units.grid(row=0, column=3, padx=(5, 0), pady=5, sticky=tk.NS)

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(3, weight=1)

Window.mainloop()