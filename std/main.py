import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import platform

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

app = tk.Tk()
app.title("System Control Panel")
app.geometry("600x500")
app.config(bg="#1e1e2f")

btn_style = {
    "font": ("Segoe UI", 14, "bold"),
    "bg": "#2e2e3e",
    "fg": "white",
    "activebackground": "#4e4e6e",
    "activeforeground": "white",
    "relief": "flat",
    "width": 22,
    "height": 2,
    "bd": 0,
    "highlightthickness": 0,
    "cursor": "hand2"
}

title = tk.Label(app, text="⚡ System Control Panel ⚡", font=("Segoe UI", 20, "bold"),
                 bg="#1e1e2f", fg="cyan")
title.pack(pady=30)

shutdown_btn = tk.Button(app, text="Shutdown", command=shutdown, **btn_style)
shutdown_btn.pack(pady=12)

restart_btn = tk.Button(app, text="Restart", command=restart, **btn_style)
restart_btn.pack(pady=12)

logout_btn = tk.Button(app, text="Logout", command=logout, **btn_style)
logout_btn.pack(pady=12)

restart_timer_btn = tk.Button(app, text="Restart with Timer", command=restart_time, **btn_style)
restart_timer_btn.pack(pady=12)

app.mainloop()
