import tkinter as tk
from random import shuffle

window = tk.Tk()
window.title("Преобразование данных")

class GroupWidgets:
    
    def __init__(self, window):
        self.entry = tk.Entry(window, width=55)
        self.button = tk.Button(window, text="Преобразовать", fg="red", bg="lightgreen")
        self.label = tk.Label(window, bg="blue", width=47, fg="yellow")
        
        self.entry.pack()
        self.button.pack()
        self.label.pack()
    
    def sort_ascending(self):
        text = self.entry.get().split()
        sorted_text = sorted(text, key=int)
        self.label.config(text=sorted_text)
    
    def sort_descending(self):
        text = self.entry.get().split()
        sorted_text = sorted(text, key=int, reverse=True)
        self.label.config(text=sorted_text)
    
    def shuffle_text(self):
        text = self.entry.get().split()
        shuffle(text)
        shuffled_text = ' '.join(text)
        self.label.config(text=shuffled_text)
    
    def bind_button(self, command):
        self.button.config(command=command)

if __name__ == '__main__':
    group_1 = GroupWidgets(window)  
    group_2 = GroupWidgets(window)
    group_3 = GroupWidgets(window)

    group_1.bind_button(group_1.sort_ascending)
    group_2.bind_button(group_2.sort_descending)
    group_3.bind_button(group_3.shuffle_text)

    window.mainloop()


