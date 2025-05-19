from tkinter import *

window = Tk()
window.title("Коды цветов")

text="Выбранный цвет"
colors_labels = Label(text=text, width=30, height=2, bg='white', font = ("Arial", 16, "bold"))

def red_label_click(event):
    global text
    text = "Красный - #C62828"
    colors_labels.config(fg = "red", text=text)

def orange_label_click(event):
    global text
    text = "Оранжевый - #F57C00"
    colors_labels.config(fg = "orange", text=text)

def yellow_label_click(event):
    global text
    text = "Желтый - #FFA726"
    colors_labels.config(fg = "yellow", text=text)

def green_label_click(event):
    global text
    text = "Зеленый - #689F38"
    colors_labels.config(fg = "green", text=text)
    
def lightblue_label_click(event):
    global text
    text = "Голубой - #ADD8E6"
    colors_labels.config(fg = "lightblue", text=text)
    
def blue_label_click(event):
    global text
    text = "Синий - #1565C0"
    colors_labels.config(fg = "blue", text=text)
    
def purple_label_click(event):
    global text
    text = "Фиолетовый - #512DA8"
    colors_labels.config(fg = "purple", text=text)

red_label = Label(width=8, height=3, bg='red', text='', borderwidth='1', relief='solid')
orange_label = Label(width=8, height=3, bg='orange', text='', borderwidth='1', relief='solid')
yellow_label = Label(width=8, height=3, bg='yellow', text='', borderwidth='1', relief='solid')
green_label = Label(width=8, height=3, bg='green', text='', borderwidth='1', relief='solid')
lightblue_label = Label(width=8, height=3, bg='lightblue', text='', borderwidth='1', relief='solid')
blue_label = Label(width=8, height=3, bg='blue', text='', borderwidth='1', relief='solid')
purple_label = Label(width=8, height=3, bg='purple', text='', borderwidth='1', relief='solid')

colors_labels.pack(side=TOP)
red_label.pack(side=LEFT)
orange_label.pack(side=LEFT)
yellow_label.pack(side=LEFT)
green_label.pack(side=LEFT)
lightblue_label.pack(side=LEFT)
blue_label.pack(side=LEFT)
purple_label.pack(side=LEFT)

red_label.bind("<Button-1>", red_label_click)
orange_label.bind("<Button-1>", orange_label_click)
yellow_label.bind("<Button-1>", yellow_label_click)
green_label.bind("<Button-1>", green_label_click)
lightblue_label.bind("<Button-1>", lightblue_label_click)
blue_label.bind("<Button-1>", blue_label_click)
purple_label.bind("<Button-1>", purple_label_click)

window.mainloop()
