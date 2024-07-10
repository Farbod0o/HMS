import math
from functools import partial
from CTkTable import *

import customtkinter as tk

from HMS.controller.controller import Controller
from HMS.model.entity.patient import Patient

class PatientInfo:
    @classmethod
    def show(cls,self, patient):
        win = tk.CTk()
        win.title("Patient Info")
        win.geometry("400x400")
        font_tuple = ("Sahel", 13,)
        cls.table.destroy()
        tk.CTkLabel(win, text=f"نام و نام خانوادگی : {patient.person.name} {patient.person.family}", anchor='e', width=370,
                    font=font_tuple).place(x=20, y=20)
        tk.CTkLabel(win, text=f"کدملی : {patient.person.username}", anchor='e', width=370,font=font_tuple).place(x=20, y=50)
        tk.CTkLabel(win, text=f"{patient.gender} : جنسیت", anchor='e', width=370,font=font_tuple).place(x=20, y=80)
        tk.CTkLabel(win, text=f"{patient.blood_type} : گروه خونی", anchor='e', width=370,font=font_tuple).place(x=20, y=110)
        tk.CTkLabel(win, text=f"وضعیت : {patient.current_conditions}", anchor='e', width=370,font=font_tuple).place(x=20, y=140)
        tk.CTkLabel(win, text=f"{patient.person.birth_date} : تاریخ تولد", anchor='e', width=370,font=font_tuple).place(x=20, y=170)
        tk.CTkLabel(win, text=f"{patient.person.username} : کدملی", anchor='e', width=370,font=font_tuple).place(x=20, y=200)
        tk.CTkLabel(win, text=f"{patient.person.phone} : شماره تماس", anchor='e', width=370,font=font_tuple).place(x=20, y=230)
        tk.CTkLabel(win, text=f"{patient.person.email} : ایمیل", anchor='e', width=370,font=font_tuple).place(x=20, y=260)
        tk.CTkLabel(win, text=f"آدرس : {patient.person.address}", anchor='e', width=370,font=font_tuple).place(x=20, y=290)
        win.mainloop()

    @classmethod
    def show_menu(cls,self, patient,p=1):
        all_patients = patient
        value = [['کدملی', 'حال شرح', 'ایمیل', 'همراه شماره', 'خونی گروه', 'جنسیت', 'خانوادگی نام و نام ', 'آیدی']]

        num = len(all_patients)
        for patient in all_patients[(p - 1) * 7:7 * p]:
            status = patient.person.status
            if status == 1:
                status = "Available"
            if patient.person.deleted == 0:
                _ = [patient.person.username, patient.current_conditions, patient.person.email, patient.person.phone, patient.blood_type,
                     patient.gender, f"{patient.person.name} {patient.person.family}",
                     patient.id]
                value.append(_)
        if num > 7:
            num = math.ceil(num / 7)
        else:
            num = 1
        font_tuple = ("Sahel", 14)
        x = 658 - num * 12
        for i in range(num):
            i += 1
            tk.CTkButton(self.win, text=f"{i}", width=15, font=font_tuple, command=partial(cls.show_menu, self, p=i)).place(x=x,
                                                                                                                   y=740)
            x += 25
        cls.table = CTkTable(master=self.win, row=8, column=8,font=font_tuple,wraplength=250,values=value)
        cls.table.place(x=20, y=430)
