from functools import partial
from CTkTable import *
from HMS.controller.controller import Controller
from HMS.model.entity.department import Department
import math
import customtkinter as tk

from HMS.model.entity.doctor import Doctor


def view(self, p=1):
    self.clear_sc()
    status, all_departments = Controller.find_all(Department)
    value = [['دپارتمان سرپرست', 'دپارتمان نام', 'دپارتمان شناسه']]

    num = len(all_departments)
    for department in all_departments[(p - 1) * 15:15 * p]:
        doc = Controller.find_by_id(Doctor,department._head_id)
        _ = [f"{doc.person._name} {doc.person._family}",department.name,department.id]
        value.append(_)
    if num > 15:
        num = math.ceil(num / 15)
    else:
        num = 1
    font_tuple = ("Sahel", 15)
    x = 658 - num * 12
    for i in range(num):
        i += 1
        tk.CTkButton(self.win, text=f"{i}", width=15, font=font_tuple, command=partial(view, self, p=i)).place(x=x,
                                                                                                               y=740)
        x += 25
    table = CTkTable(master=self.win, row=16, column=3,width=410,wraplength=250,values=value)
    table.place(x=20, y=200)
