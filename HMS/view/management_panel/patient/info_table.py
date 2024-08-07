from functools import partial
from CTkTable import *
from HMS.controller.controller import Controller
import math
import customtkinter as tk

from HMS.model.entity.patient import Patient


def view(self, p=1):
    self.clear_sc()
    status, all_patients = Controller.find_all(Patient)
    value = [['وضعیت', 'حال شرح', 'ایمیل', 'همراه شماره', 'خونی گروه', 'جنسیت', 'خانوادگی نام و نام ', 'بیمار شناسه']]

    num = len(all_patients)
    for patient in all_patients[(p - 1) * 15:15 * p]:
        status = patient.person.status
        if status == 1:
            status = "Available"
        if patient.person.deleted == 0:
            _ = [status, patient.current_conditions, patient.person.email, patient.person.phone, patient.blood_type,
                 patient.gender, f"{patient.person.name} {patient.person.family}",
                 patient.id]
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
    table = CTkTable(master=self.win, row=16, column=8,width=145,wraplength=250,values=value)
    table.place(x=20, y=200)
