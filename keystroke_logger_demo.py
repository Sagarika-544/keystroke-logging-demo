import tkinter as tk
from datetime import datetime

def start_logging():
    global logging
    logging = True
    status_label.config(text="Status: Keylogger Started", fg="#1b8f3a")

def stop_logging():
    global logging
    logging = False
    status_label.config(text="Status: Keylogger Stopped", fg="#c0392b")

def log_key(event):
    if logging and event.char:
        with open("keystroke_log.txt", "a") as f:
            f.write(f"{datetime.now()} : {event.char}\n")

# Main window
root = tk.Tk()
root.title("Keystroke Logging Demo")
root.geometry("450x380")
root.config(bg="#f4f6f7")  # light professional background

logging = False

# Heading
tk.Label(
    root,
    text="Ethical Keystroke Logging Demo",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f6f7",
    fg="#2c3e50"
).pack(pady=15)

# Instruction
tk.Label(
    root,
    text="Type inside the box below",
    font=("Segoe UI", 11),
    bg="#f4f6f7",
    fg="#34495e"
).pack()

# Text box
text_box = tk.Text(
    root,
    height=6,
    width=45,
    font=("Consolas", 10),
    bd=2,
    relief="solid",
    bg="#ffffff",
    fg="#2c3e50"
)
text_box.pack(pady=10)
text_box.bind("<Key>", log_key)

# Buttons frame
button_frame = tk.Frame(root, bg="#f4f6f7")
button_frame.pack(pady=10)

# Start button
tk.Button(
    button_frame,
    text="Start Keylogger",
    command=start_logging,
    bg="#27ae60",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
).grid(row=0, column=0, padx=10)

# Stop button
tk.Button(
    button_frame,
    text="Stop Keylogger",
    command=stop_logging,
    bg="#e74c3c",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
).grid(row=0, column=1, padx=10)

# Status label
status_label = tk.Label(
    root,
    text="Status: Keylogger Stopped",
    font=("Segoe UI", 11, "bold"),
    bg="#f4f6f7",
    fg="#c0392b"
)
status_label.pack(pady=15)

root.mainloop()
