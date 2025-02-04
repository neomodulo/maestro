from tkinter import ttk
import tkinter as tk
from PIL import Image
from PIL import ImageTk

window = tk.Tk()

window.minsize(320, 480)
window.maxsize(320, 480)
window.geometry("320x480+600+200") #The +300s are for testing purposes, not for the pi itself.
window.title("maestro")

rows, cols = (5, 7)
grid = [[0]*cols]*rows

lgray = "#BCBCBC"
dgray = "#999999"

grid[0][0] = tk.Label(window,text="⚙",      bg=lgray).grid(row=0,column=0,padx=2)
grid[0][0] = tk.Label(window,text="|",      bg=lgray).grid(row=0,column=1,padx=44)
grid[0][2] = tk.Label(window,text="maestro",bg=lgray).grid(row=0,column=2,padx=2)
grid[0][3] = tk.Label(window,text="|",      bg=lgray).grid(row=0,column=3,padx=44)
grid[0][4] = tk.Label(window,text="㍶",     bg=lgray).grid(row=0,column=4,padx=2)

album_size = 82

album_art1 = ImageTk.PhotoImage(
    Image.open("../../album_art1.png").resize((album_size,album_size),Image.LANCZOS))
album_art2 = ImageTk.PhotoImage(
    Image.open("../../album_art2.png").resize((album_size,album_size),Image.LANCZOS))

for i in range (1,5):
    for j in range (1,4):
        tk.Label(window,image=album_art2).grid(row=i,column=j)

grid[1][1] = tk.Label(window,image=album_art1).grid(row=1,column=1)

window.mainloop()
