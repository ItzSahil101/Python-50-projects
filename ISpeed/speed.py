import tkinter as tk
from tkinter import ttk
import speedtest
import threading

def set_value(label, value):
    canvas.itemconfig(label+"_value", text=str(value))

def speed_test_thread():
    sp = speedtest.Speedtest()
    sp.get_servers()
    sp.get_best_server()
    down = str(round(sp.download()/(10**6), 2)) + " Mbps"
    up = str(round(sp.upload()/(10**6), 2)) + " Mbps"
    ping = str(round(sp.results.ping, 2)) + " ms"
    # Update GUI
    set_value("Download", down)
    set_value("Upload", up)
    set_value("Ping", ping)

def start_speed_test():
    threading.Thread(target=speed_test_thread).start()

root = tk.Tk()
root.title("🌐 Internet Speed Checker")
root.geometry("700x550")
root.configure(bg="#1e1e2f")

canvas = tk.Canvas(root, width=660, height=420, bg="#1e1e2f", highlightthickness=0)
canvas.place(x=20, y=80)

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

round_rectangle(10, 10, 650, 400, radius=30, fill="#2a2d3e")

title_label = tk.Label(root, text="Internet Speed Checker",
                       font=("Segoe UI", 22, "bold"),
                       bg="#2a2d3e", fg="white")
title_label.place(x=220, y=30)

def draw_speedometer(x, y, label):
    canvas.create_arc(x-70, y-70, x+70, y+70, start=135, extent=270,
                      style="arc", outline="#3b82f6", width=14)
    canvas.create_text(x, y, text="--", font=("Segoe UI", 16, "bold"),
                       fill="#3b82f6", tags=label+"_value")
    canvas.create_text(x, y+35, text=label, font=("Segoe UI", 12, "bold"),
                       fill="white")


draw_speedometer(150, 200, "Download")
draw_speedometer(340, 200, "Upload")
draw_speedometer(530, 200, "Ping")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Segoe UI", 14, "bold"),
                foreground="white",
                background="#3b82f6",
                borderwidth=0,
                padding=12)
style.map("TButton", background=[("active", "#2563eb")])

start_btn = ttk.Button(root, text="Start Test", command=start_speed_test)
start_btn.place(x=300, y=480)

root.mainloop()
