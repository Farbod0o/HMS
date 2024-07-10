import tkinter.ttk as ttk
import customtkinter as tk


class TextWithLabel:
    def __init__(self, master, text, x, y, font_conf, distance=10, v_distance=0, disabled=False, data_type="str",
                 combo=None, label_width=30, entry_width=30, ebgc="aquamarine2", show=None, bind_func=None,
                 placeholder=None):
        tk.CTkLabel(master, text=text, width=label_width, anchor='e', font=font_conf).place(x=x, y=y)

        match data_type:
            case "str":
                self._variable = tk.StringVar()
            case "int":
                self._variable = tk.IntVar()
            case "float":
                self._variable = tk.DoubleVar()
            case "bool":
                self._variable = tk.BooleanVar()

        txt = tk.CTkEntry(master, width=entry_width,font=font_conf, textvariable=self._variable, show=show)

        if combo:
            self._variable = tk.StringVar()
            txt = tk.CTkComboBox(master, values=combo, variable=self._variable, width=entry_width)
            txt["state"] = "readonly"

        if disabled:
            txt["state"] = "readonly"
        else:
            txt["background"] = ebgc
        txt.place(x=x - distance, y=y + v_distance)

    def get_variable(self):
        return self._variable.get()

    def set_variable(self, variable):
        self._variable.set(variable)

    text = property(get_variable, set_variable)
