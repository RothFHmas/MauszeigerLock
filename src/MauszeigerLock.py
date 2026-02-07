import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import win32api
import time

LOCK_INTERVAL_MS = 150  # wie oft die Mausbeschränkung erneuert wird

current_monitor = None
lock_active = False

# ---------------- Maussteuerung ----------------
def get_monitor_for_window(root):
    root.update_idletasks()
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    for m in get_monitors():
        if (x >= m.x and x <= m.x + m.width and
            y >= m.y and y <= m.y + m.height):
            return m
    return None

def clip_mouse_to_monitor(monitor):
    rect = (monitor.x, monitor.y,
            monitor.x + monitor.width,
            monitor.y + monitor.height)
    win32api.ClipCursor(rect)

def release_mouse():
    min_x = min(m.x for m in get_monitors())
    min_y = min(m.y for m in get_monitors())
    max_x = max(m.x + m.width for m in get_monitors())
    max_y = max(m.y + m.height for m in get_monitors())
    win32api.ClipCursor((min_x, min_y, max_x, max_y))

# ---------------- Lock-Logik ----------------
def enforce_lock():
    if lock_active and current_monitor is not None:
        clip_mouse_to_monitor(current_monitor)
        root.after(LOCK_INTERVAL_MS, enforce_lock)

def lock_mouse():
    global current_monitor, lock_active
    current_monitor = get_monitor_for_window(root)
    if current_monitor:
        lock_active = True
        clip_mouse_to_monitor(current_monitor)
        enforce_lock()
        print("Maus dauerhaft auf Monitor gesperrt.")

def unlock_mouse():
    global lock_active
    lock_active = False
    release_mouse()
    print("Maus freigegeben.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Mauszeiger Lock")
root.geometry("460x300")
root.resizable(False, False)

info_text = (
    "Dieses Tool sperrt den Mauszeiger auf den Monitor,\n"
    "auf dem sich dieses Fenster befindet.\n\n"
    "🔒 Zweck:\n"
    "- Praktisch für Präsentationen, Simulationen,\n"
    "  Multi-Monitor-Setups oder Gaming-Szenarien.\n\n"
    "🛡 Sicherheit:\n"
    "- Dieses Programm enthält 100% KEINE Malware,\n"
    "  KEINE Spyware und KEINE versteckten Funktionen.\n\n"
    "📜 Lizenz:\n"
    "- Das Tool ist lizenzfrei und darf von jedem\n"
    "  kostenlos genutzt, verändert und weitergegeben werden.\n\n"
    "👨‍💻 Entwickler:\n"
    "RothFHmas (GitHub-Link unten)"
    "V1.1"
)

label_info = tk.Label(root, text=info_text, justify="left", wraplength=440)
label_info.pack(padx=10, pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

btn_lock = ttk.Button(button_frame, text="Maus sperren", command=lock_mouse)
btn_lock.grid(row=0, column=0, padx=10)

btn_unlock = ttk.Button(button_frame, text="Maus freigeben", command=unlock_mouse)
btn_unlock.grid(row=0, column=1, padx=10)

# ESC zum Freigeben
def on_key(event):
    if event.keysym == 'Escape':
        unlock_mouse()

root.bind('<Key>', on_key)

# Beim Schließen Maus freigeben
def on_close():
    unlock_mouse()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
