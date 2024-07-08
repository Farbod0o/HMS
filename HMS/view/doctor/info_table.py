from functools import partial
from CTkTable import *
from HMS.controller.controller import Controller
from HMS.model.entity.doctor import Doctor
import math
import customtkinter as tk


def view(self, p=1):
    self.clear_sc()
    status, all_doctors = Controller.find_all(Doctor)
    value = [['وضعیت', '', 'ایمیل', 'شماره همراه', 'دپارتمان', 'فوق-تخصص', 'خانوادگی نام و نام ', 'آیدی']]

    num = len(all_doctors)
    for doctor in all_doctors[(p - 1) * 15:15 * p]:
        status = doctor.person.status
        if status == 1:
            status = "Available"
        if doctor.person.deleted == 0:
            _ = [status, "", doctor.person.email, doctor.person.phone, doctor.department,
                 f"{doctor.specialty}({doctor.sub_specialty})", f"{doctor.person.name} {doctor.person.family}",
                 doctor.id]
            value.append(_)
    if num > 15:
        num = math.ceil(num / 15)
    font_tuple = ("Sahel", 15)
    x = 658 - num * 12
    for i in range(num):
        i += 1
        tk.CTkButton(self.win, text=f"{i}", width=15, font=font_tuple, command=partial(view, self, p=i)).place(x=x,
                                                                                                               y=740)
        x += 25
    table = CTkTable(master=self.win, row=16, column=8,wraplength=250,values=value)
    table.place(x=20, y=200)
