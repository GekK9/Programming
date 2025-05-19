import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
    except Exception as e:
        messagebox.showerror("Ошибка", "Файл не был открыт.")

def save_file():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension="txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
    except Exception as e:
        messagebox.showerror("Ошибка", "Файл не был сохранён.")

def clear_text():
    answer = messagebox.askyesno("Подтверждение", "Вы действительно хотите очистить текст?")
    if answer:
        text_area.delete(1.0, tk.END)

window = tk.Tk()
window.title("Работа с файлами")

text_area = tk.Text(window, height=20, width=50)
text_area.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=False)

file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)

menu_bar.add_cascade(label="Файл", menu=file_menu)
window.config(menu=menu_bar)
context_menu = tk.Menu(window, tearoff=False)
file_menu.add_command(label="Очистить", command=clear_text)

window.mainloop()