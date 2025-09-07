import tkinter as tk
from tkinter import ttk

def run():
    print("RUNNING")
    box.config(text="running")

def stop():
    box.config(text="stop")

root = tk.Tk()
root.title("🌐 Internet Speed Checker")
root.geometry("700x550")
root.configure(bg="#1e1e2f")

box = ttk.Label(root, text="ermpty", )
box.place(x=200, y=300, height=80, width=200)

start_btn = ttk.Button(root, text="Start Test", command=run)
start_btn.place(x=300, y=450, height=100, width=100)

stop = ttk.Button(root, text="stop Test", command=stop)
stop.place(x=200, y=150, height=100, width=100)

root.mainloop()
