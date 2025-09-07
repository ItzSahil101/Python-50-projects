from tkinter import *
from tkinter import ttk
import asyncio
from googletrans import Translator,LANGUAGES

def change(txt="type", src="english", dest="nepali"):
    trans = Translator()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(trans.translate(txt, src=src, dest=dest))
    return result.text

def data():
    s = comb_src.get()
    d = comb_dest.get()
    msg = src_Txt.get(1.0, END)
    textget = change(txt=msg, src=s, dest=d)
    dest_Txt.delete(1.0, END)
    dest_Txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='lightblue')

lab_title = Label(root, text="🌍 Translator", font=("Times New Roman", 40, "bold"), bg="lightblue", fg="darkblue")
lab_title.place(x=60, y=20, height=60, width=380)

lab_src = Label(root, text="Source Text:", font=("Times New Roman", 18, "bold"), fg="black", bg="lightblue")
lab_src.place(x=20, y=100, height=30, width=200)

src_Txt = Text(root, font=("Times New Roman", 16), wrap=WORD, bd=3, relief=SOLID)
src_Txt.place(x=20, y=140, height=200, width=460)

frame = Frame(root, bg="lightblue", height=100, width=500)
frame.pack(side=BOTTOM, fill=X, pady=20)

languages = list(LANGUAGES.values())

comb_src = ttk.Combobox(frame, value=languages, font=("Times New Roman", 12), state="readonly", justify="center")
comb_src.place(x=50, y=30, height=30, width=120)
comb_src.set("english")

button_change = Button(frame, text="➡ Translate ➡", font=("Times New Roman", 12, "bold"),
                       relief=RAISED, command=data, bg="darkblue", fg="white", cursor="hand2")
button_change.place(x=190, y=30, height=35, width=120)

comb_dest = ttk.Combobox(frame, value=languages, font=("Times New Roman", 12), state="readonly", justify="center")
comb_dest.place(x=340, y=30, height=30, width=120)
comb_dest.set("nepali")

lab_dest = Label(root, text="Translated Text:", font=("Times New Roman", 18, "bold"), fg="black", bg="lightblue")
lab_dest.place(x=20, y=360, height=30, width=220)

dest_Txt = Text(root, font=("Times New Roman", 16), wrap=WORD, bd=3, relief=SOLID, fg="darkgreen")
dest_Txt.place(x=20, y=400, height=200, width=460)

root.mainloop()
