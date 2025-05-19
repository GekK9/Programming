import tkinter as tk
from tkinter import ttk

def perform_button():
    global mas
    mnoj = radio_button_function()

    if mnoj != 0:
        Listbox.insert(tk.END, "Результирующий массив:")
        for i in range(len(mas)):
            mas[i] = mas[i] * mnoj
            Listbox.insert(tk.END, f"Элемент №{i+1}: {mas[i]}")
        Listbox.insert(tk.END, "")
    
    if CBvar_1.get():
        Listbox.insert(tk.END, f"Сумма элементов массива: {sum(mas)}")
    if CBvar_2.get():
        product = 1
        for num in mas:
            product *= num
        Listbox.insert(tk.END, f"Произведение элементов массива: {product}")
    if CBvar_3.get():
        Listbox.insert(tk.END, f"Минимальный элемент массива: {min(mas)}")
    if CBvar_4.get():
        Listbox.insert(tk.END, f"Максимальный элемент массива: {max(mas)}")
    Listbox.insert(tk.END, "\n")

def clear_button():
    global mas
    mas = [1, 2, 3, 4, 5]
    Listbox.delete(0, tk.END)
    Listbox.insert(tk.END, "Начальный массив:")
    for i, num in enumerate(mas, 1):
        Listbox.insert(tk.END, f"Элемент №{i}: {num}")
    Listbox.insert(tk.END, "\n")

def exit_button():
    Window.destroy()
    
def radio_button_function():
    return {0:0, 1:2, 2:3, 3:4}.get(var.get(), 0)

# Основное окно
Window = tk.Tk()
Window.title("Работа с массивами")
Window.geometry("700x350")
Window.resizable(width=False, height=False)
Window["bg"] = "lightgrey"

mas = [1, 2, 3, 4, 5]
var = tk.IntVar(value=0)

left_frame = tk.Frame(Window, bg="lightgrey", padx=10, pady=10)
middle_frame = tk.Frame(Window, bg="lightgrey", padx=10, pady=10)
right_frame = tk.Frame(Window, bg="lightgrey", padx=10, pady=10)

left_frame.grid(row=0, column=0, sticky="nsew")
middle_frame.grid(row=0, column=1, sticky="nsew")
right_frame.grid(row=0, column=2, sticky="nsew", rowspan=2)

tk.Label(left_frame, bg="lightgrey", text="Способ преобразования:").grid(row=0, column=0, columnspan=2, pady=5)
tk.Radiobutton(left_frame, bg="lightgrey", text="x 2", variable=var, value=1).grid(row=1, column=0, columnspan=3)
tk.Radiobutton(left_frame, bg="lightgrey", text="x 3", variable=var, value=2).grid(row=2, column=0, columnspan=3)
tk.Radiobutton(left_frame, bg="lightgrey", text="x 4", variable=var, value=3).grid(row=3, column=0, columnspan=3)

tk.Label(middle_frame, bg="lightgrey", text="Вывод на экран:").grid(row=0, column=0, pady=5)
CBvar_1 = tk.BooleanVar(value=False)
CBvar_2 = tk.BooleanVar(value=False)
CBvar_3 = tk.BooleanVar(value=False)
CBvar_4 = tk.BooleanVar(value=False)
tk.Checkbutton(middle_frame, bg="lightgrey", text="Сумма", variable=CBvar_1).grid(row=1, column=0, sticky="w")
tk.Checkbutton(middle_frame, bg="lightgrey", text="Произведение", variable=CBvar_2).grid(row=2, column=0, sticky="w")
tk.Checkbutton(middle_frame, bg="lightgrey", text="Минимум", variable=CBvar_3).grid(row=3, column=0, sticky="w")
tk.Checkbutton(middle_frame, bg="lightgrey", text="Максимум", variable=CBvar_4).grid(row=4, column=0, sticky="w")

Listbox = tk.Listbox(right_frame, height=18, width=40, font=('Courier New', 10))
Scrollbar = tk.Scrollbar(right_frame)
Listbox['yscrollcommand'] = Scrollbar.set
Scrollbar.config(command=Listbox.yview)

Listbox.grid(row=0, column=0, sticky="nsew")
Scrollbar.grid(row=0, column=1, sticky="ns")

button_frame = tk.Frame(Window, bg="lightgrey", pady=10)
button_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

tk.Button(button_frame, width=12, text="Выполнить", command=perform_button).pack(side="left", padx=5)
tk.Button(button_frame, width=12, text="Очистить", command=clear_button).pack(side="left", padx=5)
tk.Button(button_frame, width=12, text="Выход", command=exit_button).pack(side="left", padx=5)

clear_button()

Window.grid_rowconfigure(0, weight=1)

Window.mainloop()