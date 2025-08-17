import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE = "notes.json"

# ------------------ Helper Functions ------------------ #
def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_notes():
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note():
    subject = subject_entry.get().strip()
    content = content_text.get("1.0", tk.END).strip()

    if subject and content:
        notes.append({"subject": subject, "content": content})
        save_notes()
        refresh_notes()
        subject_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter subject and note content!")

def refresh_notes():
    notes_list.delete(0, tk.END)
    for i, note in enumerate(notes):
        notes_list.insert(i, f"{note['subject']}: {note['content'][:30]}...")

def view_note():
    try:
        index = notes_list.curselection()[0]
        note = notes[index]
        messagebox.showinfo(note["subject"], note["content"])
    except:
        messagebox.showwarning("Warning", "Please select a note to view!")

def delete_note():
    try:
        index = notes_list.curselection()[0]
        del notes[index]
        save_notes()
        refresh_notes()
    except:
        messagebox.showwarning("Warning", "Please select a note to delete!")

# ------------------ UI Setup ------------------ #
root = tk.Tk()
root.title("📚 Class Notes App")
root.geometry("600x400")

# Subject
tk.Label(root, text="Subject:").pack(anchor="w", padx=10, pady=2)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack(padx=10, pady=2)

# Content
tk.Label(root, text="Note:").pack(anchor="w", padx=10, pady=2)
content_text = tk.Text(root, height=5, width=50)
content_text.pack(padx=10, pady=2)

# Buttons
tk.Button(root, text="➕ Add Note", command=add_note, bg="lightgreen").pack(pady=5)

# Notes List
notes_list = tk.Listbox(root, width=70, height=10)
notes_list.pack(padx=10, pady=5)

# View & Delete Buttons
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Button(frame, text="👁 View Note", command=view_note, bg="lightblue").grid(row=0, column=0, padx=5)
tk.Button(frame, text="❌ Delete Note", command=delete_note, bg="salmon").grid(row=0, column=1, padx=5)

# Load notes on start
notes = load_notes()
refresh_notes()

root.mainloop()
