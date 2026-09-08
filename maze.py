import tkinter as tk
import os

BOX_SIZE = 40

window = tk.Tk()
window.title("Maze")

# Find shape.txt in the same folder as this program
folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "shape.txt")

# Read the maze
with open(file_path, "r") as f:
    lines = f.readlines()

rows = len(lines)
columns = max(len(line.rstrip("\n")) for line in lines)

canvas_width = columns * BOX_SIZE
canvas_height = rows * BOX_SIZE

canvas = tk.Canvas(
    window,
    width=canvas_width,
    height=canvas_height
)

canvas.pack()

# Draw the maze
for row, line in enumerate(lines):
    for column, character in enumerate(line.rstrip("\n")):

        x1 = column * BOX_SIZE
        y1 = row * BOX_SIZE
        x2 = x1 + BOX_SIZE
        y2 = y1 + BOX_SIZE

        if character == "*":
            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="blue",
                outline="black"
            )

        elif character == "P":
            # Pacman
            canvas.create_arc(
                x1, y1, x2, y2,
                start=25,
                extent=315,
                fill="#ffff00",
                outline="#000",
                width=2
            )

            canvas.create_oval(
                x1 + 22, y1 + 8,
                x1 + 28, y1 + 14,
                fill="#000",
                width=0.1
            )

window.mainloop()