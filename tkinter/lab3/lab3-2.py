import tkinter as tk

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int(screen_width/2 - width/2)
    y = int(screen_height/2 - height/2)
    win.geometry(f'{width}x{height}+{x}+{y}')

window = tk.Tk()
window.title("Структура инвестиционного портфеля")
center_window(window, 1050, 600)

canvas = tk.Canvas(window, width=1000, height=550, bg='white')
canvas.pack(pady=20)

canvas.create_text(500, 20, 
                 text="Структура инвестиционного портфеля, в %", 
                 font=("Arial", 16, "bold"),
                 anchor="n")

data = [
    ("Ростелеком", 20),
    ("Мегафон", 15),
    ("МТС", 35),
    ("АФК Система", 10),
    ("Башкирэнерго", 20),
]

graph_x_start, graph_y_start = 50, 80
graph_width, graph_height = 900, 400
max_value = max(value for _, value in data)

canvas.create_rectangle(graph_x_start, graph_y_start, 
                       graph_x_start + graph_width, graph_y_start + graph_height, 
                       fill="moccasin", outline="black")

levels = [10, 15, 20, 35]

for value in sorted(levels):
    y_pos = graph_y_start + graph_height - (value * graph_height / max_value)
    canvas.create_line(graph_x_start, y_pos, 
                      graph_x_start + graph_width, y_pos, 
                      dash=(4, 4))
    canvas.create_text(graph_x_start - 10, y_pos, 
                      text=f"{value}%", 
                      anchor='e', 
                      font=('Arial', 12))


bar_width = 95
padding = 55
colors = ["seagreen", "olive", "darkviolet", "hotpink", "coral"]
y_base = graph_y_start + graph_height

for i, (company, value) in enumerate(data):
    x1 = graph_x_start + padding + i * (bar_width + padding)
    y1 = y_base - (value * graph_height / max_value)
    x2 = x1 + bar_width
    y2 = y_base
    canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], outline="black")
    
    canvas.create_text(x1 + bar_width/2, y2 + 20, 
                      text=f"{company}", 
                      anchor=tk.CENTER,
                      font=('Arial', 10))

window.mainloop()