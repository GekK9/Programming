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
    
    answer = messagebox.askyesno("Подтверждение", "Очистить текст?")
    if answer:
        text_area.delete(1.0, tk.END)

Window = tk.Tk()
Window.title("Работа с файлами")

text_area = tk.Text(Window, height = 20, width = 50)
text_area.pack(fill = tk.BOTH, expand = True)

Button_open = tk.Button(Window, text = "Открыть", command = open_file)
Button_save = tk.Button(Window, text = "Сохранить", command = save_file)
Button_clear = tk.Button(Window, text = "Очистить", command = clear_text)

Button_open.pack(side = tk.LEFT)
Button_save.pack(side = tk.LEFT)
Button_clear.pack(side = tk.RIGHT)

Window.mainloop()