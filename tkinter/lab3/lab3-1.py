from tkinter import font
import tkinter as tk

window = tk.Tk()
window.title("Структура инвестиционного портфеля")

label_1 = tk.Label(font = font.Font(weight = "bold"), text = 'Газпромнефть - 20%')
label_2 = tk.Label(font = font.Font(weight = "bold"), text = 'Мечел - 15%')
label_3 = tk.Label(font = font.Font(weight = "bold"), text = 'НЛМК - 35%')
label_4 = tk.Label(font = font.Font(weight = "bold"), text = 'Красноярская ГЭС - 10%')
label_5 = tk.Label(font = font.Font(weight = "bold"), text = 'Иркутскэнерго - 5%')
label_6 = tk.Label(font = font.Font(weight = "bold"), text = 'Магнит - 15%')

canvas_1 = tk.Canvas(window, width = 300, height = 200)
canvas_2 = tk.Canvas(window, width = 50, height = 200)

circ_main = canvas_1.create_oval((62,12),(238, 188), fill = "grey")
arc_1 = canvas_1.create_arc((62,12),(238, 188), start = 0, extent = 72, fill = 'blue')
arc_2 = canvas_1.create_arc((62,12),(238, 188), start = 72, extent = 54, fill = 'orchid')
arc_3 = canvas_1.create_arc((62,12),(238, 188), start = 126, extent = 126, fill = 'red')
arc_4 = canvas_1.create_arc((62,12),(238, 188), start = 252, extent = 36, fill = 'orange')
arc_5 = canvas_1.create_arc((62,12),(238, 188), start = 288, extent = 18, fill = 'yellow')
arc_6 = canvas_1.create_arc((62,12),(238, 188), start = 306, extent = 54, fill = 'green')

rect_1 = canvas_2.create_rectangle((10,12),(50, 20), fill= 'blue')
rect_2 = canvas_2.create_rectangle((10,45),(50, 53), fill= 'orchid')
rect_3 = canvas_2.create_rectangle((10,78),(50, 86), fill='red')
rect_4 = canvas_2.create_rectangle((10,112),(50, 120), fill= 'orange')
rect_5 = canvas_2.create_rectangle((10,148),(50, 156), fill= 'yellow')
rect_6 = canvas_2.create_rectangle((10,180),(50, 188), fill= 'green')


canvas_1.grid(column = 1, row = 2, rowspan = 6)
canvas_2.grid(column = 2, row = 2, rowspan = 6)

label_1.grid(row = 2, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)
label_2.grid(row = 3, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)
label_3.grid(row = 4, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)
label_4.grid(row = 5, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)
label_5.grid(row = 6, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)
label_6.grid(row = 7, column = 3, padx = (10, 50), pady = 2, sticky = tk.W)



window.mainloop()

