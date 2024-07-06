from tkinter import *
import tkinter.ttk as ttk


class Table:
    def reset_table(self):
        for i in self.table.get_children():
            self.table.delete(i)

    def refresh_table(self, data_list):
        for i in self.table.get_children():
            self.table.delete(i)
        data = list(data_list)
        if data_list:
            for dataa in data_list:
                self.table.insert("", END, values=dataa)

    def select(self, event):
        selected = self.table.item(self.table.focus())["values"]
        self.select_function(selected)

    def __init__(self, master, headings, widths, x, y, select_function, data_list=None):
        self.select_function = select_function
        cols = list(range(len(headings)))
        self.table = ttk.Treeview(master, columns=cols, show="headings")

        for i in cols:
            self.table.heading(cols[i], text=headings[i])
            self.table.column(cols[i], width=widths[i])

        self.table.bind("<ButtonRelease>", self.select)
        self.table.bind("<KeyRelease>", self.select)
        if data_list:
            self.refresh_table(data_list)
        self.table.place(x=x, y=y)
