import tkinter as tk
from tkinter import filedialog, messagebox
import os

def scan_folder():
    folder = filedialog.askdirectory()
    if folder:
        files = os.listdir(folder)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Files in {folder}:\n")
        for f in files:
            result_text.insert(tk.END, f"{f}\n")

root = tk.Tk()
root.title("Scan Folder UI")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

scan_btn = tk.Button(frame, text="Select Folder and Scan", command=scan_folder)
scan_btn.pack(pady=5)

result_text = tk.Text(frame, width=60, height=20)
result_text.pack()

root.mainloop()