import os
import sys
import time
import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pyautogui

APP_TITLE = "Snap — Classic"
DEFAULT_DELAY = 0

class SnapClassicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("760x520")
        self.minsize(720, 480)
        self.configure(bg="#f7f7f7")
        self.iconify_supported = True

        # --- mac-like light theme for ttk ---
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        bg = "#f7f7f7"          # window background
        card_bg = "#ffffff"     # card surfaces
        text = "#111111"
        subtext = "#5f6368"
        line = "#e6e6e6"
        acc = "#007aff"         # macOS blue

        self.configure(bg=bg)
        style.configure(".", background=card_bg, foreground=text, font=("Helvetica Neue", 11))
        style.configure("TFrame", background=card_bg, relief="flat")
        style.configure("Card.TFrame", background=card_bg)
        style.configure("TLabel", background=card_bg, foreground=text, font=("Helvetica Neue", 12))
        style.configure("Muted.TLabel", foreground=subtext)
        style.configure("Title.TLabel", font=("Helvetica Neue", 18, "bold"))
        style.configure("TButton", padding=10, relief="flat", font=("Helvetica Neue", 11, "bold"))
        style.map("TButton",
                  background=[("active", "#e9f2ff")],
                  foreground=[("disabled", "#a9a9a9")])
        style.configure("Primary.TButton", foreground="white")
        style.map("Primary.TButton",
                  background=[("!disabled", acc), ("active", "#2f8fff")])
        style.configure("Outline.TButton", background=card_bg)
        style.configure("TSeparator", background=line)

        # --- Root grid layout ---
        outer = tk.Frame(self, bg=bg)
        outer.pack(fill="both", expand=True)

        container = tk.Frame(outer, bg=bg)
        container.pack(padx=26, pady=26, fill="both", expand=True)

        # Card
        self.card = ttk.Frame(container, style="Card.TFrame")
        self.card.pack(fill="both", expand=True)
        self.card.update_idletasks()
        # soft shadow effect via a thin border frame
        self.card.configure(borderwidth=1)
        self.card["padding"] = (20, 20, 20, 20)

        # --- Header ---
        header = ttk.Frame(self.card, style="Card.TFrame")
        header.pack(fill="x")
        ttk.Label(header, text="Snap", style="Title.TLabel").pack(side="left")
        ttk.Label(header, text="• Classic white, minimal, precise", style="Muted.TLabel").pack(side="left", padx=10)

        ttk.Separator(self.card).pack(fill="x", pady=(16, 20))

        # --- Controls Row ---
        controls = ttk.Frame(self.card)
        controls.pack(fill="x")

        # delay
        delay_box = ttk.Frame(controls)
        delay_box.pack(side="left", padx=(0, 14))
        ttk.Label(delay_box, text="Delay").pack(anchor="w")
        self.delay_var = tk.IntVar(value=DEFAULT_DELAY)
        self.delay_spin = ttk.Spinbox(delay_box, from_=0, to=10, width=5, textvariable=self.delay_var)
        self.delay_spin.pack(pady=(4,0))
        ttk.Label(delay_box, text="seconds", style="Muted.TLabel").pack()

        # file format
        fmt_box = ttk.Frame(controls)
        fmt_box.pack(side="left", padx=14)
        ttk.Label(fmt_box, text="Format").pack(anchor="w")
        self.format_var = tk.StringVar(value="PNG")
        fmt = ttk.Combobox(fmt_box, textvariable=self.format_var, values=["PNG","JPG"], width=6, state="readonly")
        fmt.pack(pady=(4,0))
        ttk.Label(fmt_box, text="PNG recommended", style="Muted.TLabel").pack()

        # spacer
        ttk.Frame(controls).pack(side="left", expand=True, fill="x")

        # Buttons
        btns = ttk.Frame(controls)
        btns.pack(side="right")

        self.full_btn = ttk.Button(btns, text="Capture Full Screen (Ctrl+Shift+5)",
                                   style="Primary.TButton", command=self.capture_fullscreen)
        self.full_btn.pack(side="top", fill="x")

        self.region_btn = ttk.Button(btns, text="Capture Region (Ctrl+Shift+4)",
                                     style="Outline.TButton", command=self.capture_region)
        self.region_btn.pack(side="top", fill="x", pady=(10,0))

        # --- Preview Area ---
        ttk.Separator(self.card).pack(fill="x", pady=(20, 16))
        preview_wrap = ttk.Frame(self.card)
        preview_wrap.pack(fill="both", expand=True)

        left = ttk.Frame(preview_wrap)
        left.pack(side="left", fill="both", expand=True)
        ttk.Label(left, text="Last Capture Preview").pack(anchor="w")
        self.preview_canvas = tk.Canvas(left, bg="#fbfbfb", highlightthickness=1, highlightbackground=line)
        self.preview_canvas.pack(fill="both", expand=True, pady=(8,0))

        right = ttk.Frame(preview_wrap, width=240)
        right.pack(side="right", fill="y")
        ttk.Label(right, text="Tips", style="Muted.TLabel").pack(anchor="w")
        tips = (
            "• Use Ctrl+Shift+5 for full screen.\n"
            "• Use Ctrl+Shift+4 for a region.\n"
            "• Set a delay to arrange windows.\n"
            "• Window hides before capture."
        )
        ttk.Label(right, text=tips, style="Muted.TLabel", justify="left").pack(anchor="w", pady=8)

        # status bar
        ttk.Separator(self.card).pack(fill="x", pady=(16, 8))
        self.status = ttk.Label(self.card, text="Ready", style="Muted.TLabel")
        self.status.pack(anchor="w")

        # internal
        self._preview_imgtk = None
        self.last_image = None

        # Hotkeys (mac-like but cross-platform: use Control instead of Command)
        self.bind_all("<Control-Shift-Key-5>", lambda e: self.capture_fullscreen())
        self.bind_all("<Control-Shift-Key-4>", lambda e: self.capture_region())

        # Better window placement
        self.after(50, self._center)

    def _center(self):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (sw - w) // 2
        y = int(sh * 0.12)
        self.geometry(f"+{x}+{y}")

    # ---------- Capture helpers ----------
    def _safe_hide(self):
        try:
            # Withdraw to avoid appearing in screenshot
            self.withdraw()
            self.update()
        except Exception:
            self.iconify_supported = False
            try:
                self.iconify()
                self.update()
            except Exception:
                pass

    def _safe_show(self):
        try:
            self.deiconify()
            self.update()
        except Exception:
            try:
                self.state("normal")
                self.update()
            except Exception:
                pass

    def _delay_then(self):
        d = max(0, int(self.delay_var.get() or 0))
        if d:
            for i in range(d, 0, -1):
                self.status.configure(text=f"Capturing in {i}…")
                self.update_idletasks()
                time.sleep(1)
        self.status.configure(text="Capturing…")
        self.update_idletasks()

    def _default_filename(self, ext):
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"screenshot_{ts}.{ext.lower()}"

    def _ask_savepath(self, default_ext):
        initfile = self._default_filename(default_ext)
        filetypes = [("PNG image","*.png"), ("JPEG image","*.jpg;*.jpeg")]
        path = filedialog.asksaveasfilename(
            defaultextension=f".{default_ext.lower()}",
            initialfile=initfile,
            title="Save Screenshot As…",
            filetypes=filetypes)
        return path

    def _save_and_preview(self, image, chosen_path):
        # Ensure correct format and extension based on chosen_path
        ext = os.path.splitext(chosen_path)[1].lower()
        fmt = "PNG" if ext == ".png" else "JPEG"
        params = {}
        if fmt == "JPEG":
            params["quality"] = 95
        image.save(chosen_path, fmt, **params)

        # Preview (fit into canvas)
        self.last_image = image
        self._render_preview(image)
        self.status.configure(text=f"Saved: {chosen_path}")

    def _render_preview(self, image):
        self.preview_canvas.delete("all")
        cw = self.preview_canvas.winfo_width()
        ch = self.preview_canvas.winfo_height()
        if cw < 10 or ch < 10:
            self.after(100, lambda: self._render_preview(image))
            return
        iw, ih = image.size
        scale = min(cw / iw, ch / ih)
        nw, nh = max(1,int(iw*scale)), max(1,int(ih*scale))
        thumb = image.resize((nw, nh), Image.LANCZOS)
        self._preview_imgtk = ImageTk.PhotoImage(thumb)
        x = (cw - nw) // 2
        y = (ch - nh) // 2
        self.preview_canvas.create_image(x, y, image=self._preview_imgtk, anchor="nw")
        self.preview_canvas.create_rectangle(0, 0, cw, ch, outline="#e6e6e6")

    # ---------- Actions ----------
    def capture_fullscreen(self):
        try:
            path = self._ask_savepath(self.format_var.get())
            if not path:
                self.status.configure(text="Canceled.")
                return
            self._safe_hide()
            self._delay_then()
            img = pyautogui.screenshot()
            self._safe_show()
            self._save_and_preview(img, path)
        except Exception as e:
            self._safe_show()
            messagebox.showerror("Capture Failed", str(e))
            self.status.configure(text="Error during capture.")

    def capture_region(self):
        try:
            path = self._ask_savepath(self.format_var.get())
            if not path:
                self.status.configure(text="Canceled.")
                return
            # overlay for region selection
            self._safe_hide()
            self._delay_then()
            region = self._select_region_overlay()
            self._safe_show()
            if not region:
                self.status.configure(text="Region selection canceled.")
                return
            x, y, w, h = region
            img = pyautogui.screenshot(region=(x, y, w, h))
            self._save_and_preview(img, path)
        except Exception as e:
            self._safe_show()
            messagebox.showerror("Capture Failed", str(e))
            self.status.configure(text="Error during capture.")

    # ---------- Region Selection Overlay ----------
    def _select_region_overlay(self):
        """
        Returns (x, y, w, h) or None if canceled.
        Creates a semi-transparent fullscreen overlay with crosshair rectangle.
        """
        sel = {"start": None, "end": None, "rect": None, "done": False}

        overlay = tk.Toplevel()
        overlay.withdraw()
        overlay.overrideredirect(True)
        overlay.attributes("-topmost", True)
        try:
            # On Windows, enable click-through transparency is tricky; we just use alpha
            overlay.attributes("-alpha", 0.15)
        except tk.TclError:
            pass

        sw = overlay.winfo_screenwidth()
        sh = overlay.winfo_screenheight()
        overlay.geometry(f"{sw}x{sh}+0+0")

        canvas = tk.Canvas(overlay, cursor="cross", bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        hint = tk.Label(overlay, text="Drag to select region  •  Enter: confirm  •  Esc: cancel",
                        font=("Helvetica Neue", 12, "bold"), bg="#000000", fg="#ffffff")
        # Place hint near top
        def place_hint():
            hint.update_idletasks()
            hint.place(x=sw//2 - hint.winfo_width()//2, y=20)
        place_hint()

        def to_screen_coords(e):
            return (e.x, e.y)

        def on_press(e):
            sel["start"] = to_screen_coords(e)
            sel["end"] = sel["start"]
            # clear and draw initial rectangle
            canvas.delete("selection")
            sel["rect"] = canvas.create_rectangle(*sel["start"], *sel["end"],
                                                  outline="#ffffff", width=2, tags="selection")

        def on_drag(e):
            if sel["start"] is None:
                return
            sel["end"] = to_screen_coords(e)
            canvas.coords(sel["rect"], *sel["start"], *sel["end"])

        def on_release(e):
            if sel["start"] is None:
                return
            sel["end"] = to_screen_coords(e)

        def on_key(e):
            if e.keysym.lower() == "escape":
                sel["start"] = None
                sel["end"] = None
                sel["done"] = True
                overlay.destroy()
            elif e.keysym.lower() in ("return", "enter"):
                sel["done"] = True
                overlay.destroy()

        overlay.bind("<ButtonPress-1>", on_press)
        overlay.bind("<B1-Motion>", on_drag)
        overlay.bind("<ButtonRelease-1>", on_release)
        overlay.bind("<Key>", on_key)

        # show after binding so it focuses
        overlay.deiconify()
        overlay.focus_set()
        overlay.lift()

        # block dialog
        overlay.wait_window()

        if not sel["done"] or sel["start"] is None or sel["end"] is None:
            return None

        x1, y1 = sel["start"]
        x2, y2 = sel["end"]
        x, y = min(x1, x2), min(y1, y2)
        w, h = abs(x2 - x1), abs(y2 - y1)
        if w < 2 or h < 2:
            return None
        return (x, y, w, h)


if __name__ == "__main__":
    # Basic guard for missing deps (rare since we import at top)
    try:
        app = SnapClassicApp()
        app.mainloop()
    except ImportError as ie:
        messagebox.showerror("Missing Dependency",
                             f"A required package is missing:\n\n{ie}\n\nInstall with:\n  pip install pyautogui pillow")
        sys.exit(1)
