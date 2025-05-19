import os
import shutil
import glob
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog 

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Файловый менеджер")
        self.root.geometry("800x600")
        
        self.current_dir = os.getcwd()
        
        self.create_widgets()
        self.update_dir_list()
        
    def create_widgets(self):
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        middle_frame = ttk.Frame(self.root)
        middle_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=5, pady=5)

        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(top_frame, textvariable=self.path_var, width=70)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        
        browse_btn = ttk.Button(top_frame, text="Обзор...", command=self.browse_directory)
        browse_btn.pack(side=tk.LEFT, padx=2)
        

        dir_frame = ttk.Frame(middle_frame)
        dir_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=2)
        
        ttk.Label(dir_frame, text="Директории").pack()
        self.dir_listbox = tk.Listbox(dir_frame, width=30, height=25)
        self.dir_listbox.pack(fill=tk.Y, expand=True)
        self.dir_listbox.bind('<<ListboxSelect>>', self.on_dir_select)
        
        file_frame = ttk.Frame(middle_frame)
        file_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        
        ttk.Label(file_frame, text="Файлы").pack()
        self.file_listbox = tk.Listbox(file_frame, width=50, height=25)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = ttk.Frame(middle_frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        ttk.Button(btn_frame, text="Дублировать все", command=self.duplicate_all).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Дублировать выбранный", command=self.duplicate_selected).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Удалить дубликаты", command=self.remove_duplicates).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Удалить пустые директории", command=self.remove_empty_dirs).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Удалить по расширению", command=self.remove_by_extension).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Переименовать выбранный", command=self.rename_selected).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Переместить выбранный", command=self.move_selected).pack(fill=tk.X, pady=2)
    
    def browse_directory(self):
        dir_path = filedialog.askdirectory(initialdir=self.current_dir)
        if dir_path:
            self.current_dir = dir_path
            self.path_var.set(dir_path)
            self.update_dir_list()
    
    def update_dir_list(self):
        self.dir_listbox.delete(0, tk.END)
        self.file_listbox.delete(0, tk.END)
        
        try:
            parent_dir = os.path.dirname(self.current_dir)
            if parent_dir != self.current_dir:
                self.dir_listbox.insert(tk.END, "..")
            
            for item in sorted(os.listdir(self.current_dir)):
                full_path = os.path.join(self.current_dir, item)
                if os.path.isdir(full_path):
                    self.dir_listbox.insert(tk.END, item)
                elif os.path.isfile(full_path):
                    self.file_listbox.insert(tk.END, item)
        except Exception as e:
            self.log_message(f"Ошибка: {str(e)}")
    
    def on_dir_select(self, event):
        selection = self.dir_listbox.curselection()
        if selection:
            selected_dir = self.dir_listbox.get(selection[0])
            if selected_dir == "..":
                new_path = os.path.dirname(self.current_dir)
            else:
                new_path = os.path.join(self.current_dir, selected_dir)
            
            if os.path.isdir(new_path):
                self.current_dir = new_path
                self.path_var.set(new_path)
                self.update_dir_list()
    
    def get_selected_file(self):
        selection = self.file_listbox.curselection()
        if selection:
            return self.file_listbox.get(selection[0])
        return None
    
    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
    
    def duplicate_all(self):
        try:
            files = [f for f in os.listdir(self.current_dir) if os.path.isfile(os.path.join(self.current_dir, f))]
            
            for file in files:
                base, ext = os.path.splitext(file)
                new_name = f"{base}_copy{ext}"
                src = os.path.join(self.current_dir, file)
                dst = os.path.join(self.current_dir, new_name)
                shutil.copy2(src, dst)
                self.log_message(f"Создана копия: {file} -> {new_name}")
            
            self.update_dir_list()
            messagebox.showinfo("Готово", "Все файлы дублированы")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def duplicate_selected(self):
        file = self.get_selected_file()
        if not file:
            messagebox.showwarning("Предупреждение", "Файл не выбран")
            return
        
        try:
            base, ext = os.path.splitext(file)
            new_name = f"{base}_copy{ext}"
            src = os.path.join(self.current_dir, file)
            dst = os.path.join(self.current_dir, new_name)
            shutil.copy2(src, dst)
            self.log_message(f"Создана копия: {file} -> {new_name}")
            self.update_dir_list()
            messagebox.showinfo("Готово", "Файл дублирован")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def remove_duplicates(self):
        try:
            files = [f for f in os.listdir(self.current_dir) if os.path.isfile(os.path.join(self.current_dir, f))]
            duplicates = []
            
            # Находим файлы с '_copy' в имени
            for file in files:
                if '_copy' in file:
                    original = file.replace('_copy', '')
                    if original in files:
                        duplicates.append(file)
            
            if not duplicates:
                messagebox.showinfo("Информация", "Дубликаты не найдены")
                return
            
            # Удаляем дубликаты
            for dup in duplicates:
                os.remove(os.path.join(self.current_dir, dup))
                self.log_message(f"Удален дубликат: {dup}")
            
            self.update_dir_list()
            messagebox.showinfo("Готово", f"Удалено {len(duplicates)} дубликатов")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def remove_empty_dirs(self):
        try:
            removed = 0
            for root, dirs, files in os.walk(self.current_dir, topdown=False):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        if not os.listdir(dir_path):
                            os.rmdir(dir_path)
                            self.log_message(f"Удалена пустая директория: {dir_path}")
                            removed += 1
                    except OSError:
                        continue
            
            self.update_dir_list()
            messagebox.showinfo("Готово", f"Удалено {removed} пустых директорий")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def remove_by_extension(self):
        ext = simpledialog.askstring("Удаление по расширению", "Введите расширение файлов (например, txt):")
        if not ext:
            return
        
        if not ext.startswith('.'):
            ext = '.' + ext
        
        try:
            files = glob.glob(os.path.join(self.current_dir, '*' + ext))
            if not files:
                messagebox.showinfo("Информация", f"Файлы с расширением {ext} не найдены")
                return
            
            if messagebox.askyesno("Подтверждение", f"Удалить {len(files)} файлов с расширением {ext}?"):
                for file in files:
                    os.remove(file)
                    self.log_message(f"Удален файл: {os.path.basename(file)}")
                
                self.update_dir_list()
                messagebox.showinfo("Готово", f"Удалено {len(files)} файлов")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def rename_selected(self):
        file = self.get_selected_file()
        if not file:
            messagebox.showwarning("Предупреждение", "Файл не выбран")
            return
        
        new_name = simpledialog.askstring("Переименование", "Введите новое имя файла:", initialvalue=file)
        if not new_name or new_name == file:
            return
        
        try:
            src = os.path.join(self.current_dir, file)
            dst = os.path.join(self.current_dir, new_name)
            os.rename(src, dst)
            self.log_message(f"Переименован: {file} -> {new_name}")
            self.update_dir_list()
            messagebox.showinfo("Готово", "Файл переименован")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def move_selected(self):
        file = self.get_selected_file()
        if not file:
            messagebox.showwarning("Предупреждение", "Файл не выбран")
            return
        
        dest_dir = filedialog.askdirectory(initialdir=self.current_dir, title="Выберите целевую директорию")
        if not dest_dir:
            return
        
        try:
            src = os.path.join(self.current_dir, file)
            dst = os.path.join(dest_dir, file)
            shutil.move(src, dst)
            self.log_message(f"Перемещен: {file} -> {dest_dir}")
            self.update_dir_list()
            messagebox.showinfo("Готово", "Файл перемещен")
        except Exception as e:  
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()