from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def show_about(event=None):
    messagebox.showwarning("About", "akashofficial@gmail.com")


if __name__ == "__main__":
    print("Start")
    root = Tk()
    root.title("Menu Bar")

    the_menu = Menu(root)
    file_menu = Menu(the_menu, tearoff=0)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=lambda: root.quit())
    the_menu.add_cascade(label="File", menu=file_menu)

    view_menu = Menu(the_menu, tearoff=0)
    line_numbers = IntVar()
    line_numbers.set(1)
    view_menu.add_checkbutton(label="Line Numbers", variable=line_numbers)
    the_menu.add_cascade(label="View", menu=view_menu)

    text_font = StringVar()
    text_font.set("Times")
    font_menu = Menu(the_menu, tearoff=0)
    font_menu.add_radiobutton(label="Times", variable=text_font, command=lambda: print("Font Changed to", text_font.get()))
    font_menu.add_radiobutton(label="Courier", variable=text_font, command=lambda: print("Font Changed to", text_font.get()))
    font_menu.add_radiobutton(label="Arial", variable=text_font, command=lambda: print("Font Changed to", text_font.get()))
    the_menu.add_cascade(label="Font", menu=font_menu)

    help_menu = Menu(the_menu, tearoff=0)
    help_menu.add_command(label="About", accelerator="Ctrl+A", command=show_about)
    # Key substitutions on Windows and Mac
    # Control (Windows) = Command (Mac)
    # Alt (Windows) = Option (Mac)
    the_menu.add_cascade(label="Help", menu=help_menu)
    root.bind('<Control-A>', show_about)
    root.bind('<Control-a>', show_about)
    root.config(menu=the_menu)

    root.mainloop()
    print("Stop")
