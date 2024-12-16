#Вариант 24
#Объекты – пятиугольники
#Функции:	сегментация
#визуализация
#раскраска
#перемещение на плоскости

import tkinter as tk
import random
import math

class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор пятиугольников")
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.instruction_label = tk.Label(root, text="Нажмите 'Создать пятиугольник' для генерации пятиугольника", font=("Arial", 12))
        self.instruction_label.pack()

        self.color_button = tk.Button(root, text="Изменить цвет", command=self.change_color)
        self.color_button.pack()

        self.current_color = self.random_color()
        self.current_color_button = tk.Button(root, text=f"Текущий цвет: {self.current_color}", command=self.show_current_color)
        self.current_color_button.pack()

        self.move_button = tk.Button(root, text="Переместить пятиугольник", command=self.move_shape)
        self.move_button.pack()

        self.shape_button = tk.Button(root, text="Создать пятиугольник", command=self.create_shape)
        self.shape_button.pack()

        self.shape_id = None

    def create_shape(self):
        x1 = random.randint(50, 550)
        y1 = random.randint(50, 350)
        size = random.randint(20, 100)
        self.shape_id = self.draw_pentagon(x1, y1, size)

    def draw_pentagon(self, x, y, size):
        points = []
        for i in range(5):
            angle = 2 * math.pi / 5 * i
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append(px)
            points.append(py)
        return self.canvas.create_polygon(points, fill=self.current_color, outline='black')

    def move_shape(self):
        if self.shape_id:
            dx = random.randint(-50, 50)
            dy = random.randint(-50, 50)
            self.canvas.move(self.shape_id, dx, dy)

    def change_color(self):
        self.current_color = self.random_color()
        if self.shape_id:
            self.canvas.itemconfig(self.shape_id, fill=self.current_color)
        self.update_color_button()

    def show_current_color(self):
        color_info = f"Текущий цвет: {self.current_color}"
        tk.messagebox.showinfo("Текущий цвет", color_info)

    def update_color_button(self):
        self.current_color_button.config(text=f"Текущий цвет: {self.current_color}")

    def random_color(self):
        return f'#{random.randint(0, 0xFFFFFF):06x}'

if __name__ == "__main__":
    import tkinter.messagebox
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
