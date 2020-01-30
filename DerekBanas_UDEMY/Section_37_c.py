from tkinter import *
from tkinter import ttk


def set_entry(*args):
    entry_1_txt.set("Hello")


def chk_btn_change(*args):
    entry_1_txt.set(chk_button_1_txt.get())


def radio_change(*args):
    entry_1_txt.set(radio_but_1_value.get())


def combo_change(*args):
    entry_1_txt.set(combo_1_val.get())


if __name__ == "__main__":
    root = Tk()
    root.title("Widget Example")
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    lable_1_txt = StringVar()
    lable_1 = ttk.Label(frame, text='Data')
    lable_1.grid(column=1, row=1, sticky=(W, E))

    lable_1['textvariable'] = lable_1_txt
    lable_1_txt.set('DATA')

    entry_1_txt = StringVar()
    entry_1 = ttk.Entry(frame, width=7, textvariable=entry_1_txt)
    entry_1.grid(column=2, row=1, sticky=(W, E))
    entry_1_txt.set(lable_1_txt.get())

    button_1 = ttk.Button(frame, text="Click", command=set_entry)
    button_1.grid(column=3, row=1, sticky=(W, E))

    button_1['state'] = 'disabled'
    button_1['state'] = 'enabled'

    chk_button_1_txt = StringVar()
    chk_button_1 = ttk.Checkbutton(frame, text="Feeling",
                                   command=chk_btn_change,
                                   variable=chk_button_1_txt,
                                   onvalue='Happy',
                                   offvalue='Sad')
    chk_button_1.grid(column=4, row=1, sticky=(W, E))

    radio_but_1_value = StringVar()
    radio_1 = ttk.Radiobutton(frame, text='Red',
                              variable=radio_but_1_value,
                              value='Red', command=radio_change)
    radio_2 = ttk.Radiobutton(frame, text='Blue',
                              variable=radio_but_1_value,
                              value='Blue', command=radio_change)
    radio_3 = ttk.Radiobutton(frame, text='Green',
                              variable=radio_but_1_value,
                              value='Green', command=radio_change)
    radio_1.grid(column=2, row=2, sticky=(W, E))
    radio_2.grid(column=3, row=2, sticky=(W, E))
    radio_3.grid(column=4, row=2, sticky=(W, E))

    lable_2 = ttk.Label(frame, text='Fav Color')
    lable_2.grid(column=1, row=2, sticky=(W, E))

    combo_1_val = StringVar()
    combo_1_val.set('Default')
    combo_1 = ttk.Combobox(frame, textvariable=combo_1_val)
    lable_3 = ttk.Label(frame, text='Size')
    lable_3.grid(column=1, row=3, sticky=(W, E))
    combo_1['values'] = ('Small', 'Medium', 'Large')
    combo_1.grid(column=2, row=3, sticky=(W, E))
    combo_1.bind("<<ComboboxSelected>>", combo_change)

    root.mainloop()
