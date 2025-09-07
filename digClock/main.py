from tkinter import *
import time

clock = Tk()
clock.title("🌙 Digital Clock")
clock.geometry("800x400")
clock.config(bg="#1e1e2f")

frame = Frame(clock, bg="#282a36", bd=0, relief="solid")
frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=300)

lab_hr_text = Label(frame, text="HOUR", font=("Segoe UI", 14, "bold"), bg="#282a36", fg="#f8f8f2")
lab_hr_text.place(x=40, y=10, width=130, height=30)

lab_hr = Label(frame, text="00", font=("Segoe UI", 60, "bold"), bg="#44475a", fg="#50fa7b")
lab_hr.place(x=40, y=40, height=110, width=130)

lab_min_text = Label(frame, text="MIN", font=("Segoe UI", 14, "bold"), bg="#282a36", fg="#f8f8f2")
lab_min_text.place(x=200, y=10, width=130, height=30)

lab_min = Label(frame, text="00", font=("Segoe UI", 60, "bold"), bg="#44475a", fg="#8be9fd")
lab_min.place(x=200, y=40, height=110, width=130)

lab_sec_text = Label(frame, text="SEC", font=("Segoe UI", 14, "bold"), bg="#282a36", fg="#f8f8f2")
lab_sec_text.place(x=360, y=10, width=130, height=30)

lab_sec = Label(frame, text="00", font=("Segoe UI", 60, "bold"), bg="#44475a", fg="#ff5555")
lab_sec.place(x=360, y=40, height=110, width=130)

lab_day = Label(frame, text="DAY", font=("Segoe UI", 20, "bold"), bg="#282a36", fg="#f1fa8c")
lab_day.place(x=40, y=170, height=50, width=120)

lab_date = Label(frame, text="00-00-0000", font=("Segoe UI", 20, "bold"), bg="#282a36", fg="#ffb86c")
lab_date.place(x=200, y=170, height=50, width=220)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    hr, minute, sec = current_time.split(":")
    
    day = time.strftime("%A")
    date = time.strftime("%d-%m-%Y")
    
    lab_hr.config(text=hr)
    lab_min.config(text=minute)
    lab_sec.config(text=sec)
    lab_day.config(text=day)
    lab_date.config(text=date)
    
    clock.after(1000, update_time)

update_time()
clock.mainloop()
