from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0
    div_trigger = False
    mul_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        if value == 'AC':
            self.div_trigger = False
            self.mul_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.number_entry.delete(0, "end")
            # self.number_entry.insert(0, entry_val)
        else:
            if self.is_float(self.number_entry.get()):
                entry_val = self.number_entry.get()
                entry_val += value
                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, entry_val)
            else:
                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, value)

    def is_float(self, str_val):
        try:
            float(str_val)
        except ValueError:
            return False
        else:
            return True

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.div_trigger = False
            self.mul_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                self.div_trigger = True
            elif value == "*":
                self.mul_trigger = True
            elif value == "+":
                self.add_trigger = True
            else:
                self.sub_trigger = True
            self.number_entry.delete(0, "end")
        else:
            self.number_entry.delete(0, "end")

    def eql_botton_press(self):
        if self.add_trigger or self.sub_trigger or self.mul_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mul_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                if float(self.entry_value.get()) == 0:
                    self.number_entry.delete(0, "end")
                    solution = "Not Divisible By Zero"
                else:
                    solution = self.calc_value / float(self.entry_value.get())

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entry_value = StringVar(root, value='')
        root.title("Calculator")
        # root.geometry("480x220")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 15", padding=10)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4, sticky=(W, E))

        self.button_7 = ttk.Button(root, text="7", command=lambda: self.button_press('7'))
        self.button_7.grid(row=1, column=0, sticky=(W, E))
        self.button_8 = ttk.Button(root, text="8", command=lambda: self.button_press('8'))
        self.button_8.grid(row=1, column=1, sticky=(W, E))
        self.button_9 = ttk.Button(root, text="9", command=lambda: self.button_press('9'))
        self.button_9.grid(row=1, column=2, sticky=(W, E))
        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/'))
        self.button_div.grid(row=1, column=3, sticky=(W, E))

        self.button_4 = ttk.Button(root, text="4", command=lambda: self.button_press('4'))
        self.button_4.grid(row=2, column=0, sticky=(W, E))
        self.button_5 = ttk.Button(root, text="5", command=lambda: self.button_press('5'))
        self.button_5.grid(row=2, column=1, sticky=(W, E))
        self.button_6 = ttk.Button(root, text="6", command=lambda: self.button_press('6'))
        self.button_6.grid(row=2, column=2, sticky=(W, E))
        self.button_mul = ttk.Button(root, text="*", command=lambda: self.math_button_press('*'))
        self.button_mul.grid(row=2, column=3, sticky=(W, E))

        self.button_1 = ttk.Button(root, text="1", command=lambda: self.button_press('1'))
        self.button_1.grid(row=3, column=0, sticky=(W, E))
        self.button_2 = ttk.Button(root, text="2", command=lambda: self.button_press('2'))
        self.button_2.grid(row=3, column=1, sticky=(W, E))
        self.button_3 = ttk.Button(root, text="3", command=lambda: self.button_press('3'))
        self.button_3.grid(row=3, column=2, sticky=(W, E))
        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+'))
        self.button_add.grid(row=3, column=3, sticky=(W, E))

        self.button_clr = ttk.Button(root, text="AC", command=lambda: self.button_press('AC'))
        self.button_clr.grid(row=4, column=0, sticky=(W, E))
        self.button_0 = ttk.Button(root, text="0", command=lambda: self.button_press('0'))
        self.button_0.grid(row=4, column=1, sticky=(W, E))
        self.button_eql = ttk.Button(root, text="=", command=lambda: self.eql_botton_press())
        self.button_eql.grid(row=4, column=2, sticky=(W, E))
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-'))
        self.button_sub.grid(row=4, column=3, sticky=(W, E))


if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
