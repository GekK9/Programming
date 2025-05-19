import tkinter as tk

def button_function(event):
    width = entry1.get()
    height = entry2.get()
    text.config(width, height)

def button_function():
    width = entry1.get()
    height = entry2.get()
    text.config(width, height)

def in_focus_height(event):
    entry1.config(bg = "white")
    
def out_focus_height(event):
    entry1.config(bg = "lightgrey")
    
def in_focus_width(event):
    entry2.config(bg = "white")
    
def out_focus_width(event):
    entry2.config(bg = "lightgrey")

window = tk.Tk()
window.title("tk")

text = tk.Text(window, width = 25, height = 10)
button = tk.Button(window, width = 13, text = "Изменить", command = button_function)
entry1 = tk.Entry(window, width = 5)
entry2 = tk.Entry(window, width = 5)

entry1.grid(row = 1, column = 1, sticky = tk.E)
entry2.grid(row = 2, column = 1, sticky = tk.E)
button.grid(row = 1, column = 2, rowspan = 2, sticky = tk.W)
text.grid(row = 3, columnspan = 3)

entry1.bind('<Return>', button_function)
entry2.bind('<Return>', button_function)

entry1.config(bg = "lightgrey")
entry2.config(bg = "lightgrey")

entry1.bind('<FocusIn>', in_focus_height)
entry1.bind('<FocusOut>', out_focus_height)
entry2.bind('<FocusIn>', in_focus_width)
entry2.bind('<FocusOut>', out_focus_width)

window.mainloop()