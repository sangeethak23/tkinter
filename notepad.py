import tkinter as tk
from tkinter import filedialog

def new_file():
    root.title("Untitled")
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        root.title(file_path)
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(file_path)

def cut_text():
    # Your custom cut implementation here
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def copy_text():
    # Your custom copy implementation here
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def paste_text():
    # Your custom paste implementation here
    text_to_paste = root.clipboard_get()
    text_area.insert(tk.INSERT, text_to_paste)

def select_all():
        # Your custom select all implementation here
        text_area.tag_add(tk.SEL, "1.0", tk.END)


root = tk.Tk()
root.title("Simple Notepad")
root.geometry("1080x720")

text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

root.mainloop()
