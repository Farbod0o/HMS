
from CTkTable import *
import customtkinter as tk
from HMS.view.component.CTkXYFrame import CTkXYFrame
from datetime import datetime


class PatientInfo:
    @classmethod
    def show(cls,self, patient):
        win = tk.CTk()
        win.title("Patient Info")
        win.geometry("400x400")
        font_tuple = ("Sahel", 13,)
        try:
            self.table.destroy()
        except Exception as e:
            print(e)
        tk.CTkLabel(win, text=f"نام و نام خانوادگی : {patient.person.name} {patient.person.family}", anchor='e',
                    width=370,
                    font=font_tuple).place(x=20, y=20)
        tk.CTkLabel(win, text=f"کدملی : {patient.person.username}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                  y=50)
        tk.CTkLabel(win, text=f"{patient.gender} : جنسیت", anchor='e', width=370, font=font_tuple).place(x=20, y=80)
        tk.CTkLabel(win, text=f"{patient.blood_type} : گروه خونی", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                 y=110)
        tk.CTkLabel(win, text=f"وضعیت : {patient.current_conditions}", anchor='e', width=370, font=font_tuple).place(
            x=20, y=140)
        tk.CTkLabel(win, text=f"{patient.person.birth_date} : تاریخ تولد", anchor='e', width=370,
                    font=font_tuple).place(x=20, y=170)
        tk.CTkLabel(win, text=f"{patient.person.username} : کدملی", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                  y=200)
        tk.CTkLabel(win, text=f"{patient.person.phone} : شماره تماس", anchor='e', width=370, font=font_tuple).place(
            x=20, y=230)
        tk.CTkLabel(win, text=f"{patient.person.email} : ایمیل", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                               y=260)
        tk.CTkLabel(win, text=f"آدرس : {patient.person.address}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                y=290)
        win.mainloop()

    @classmethod
    def show_menu(cls, self, patient):
        all_patients = patient
        font_tuple = ("Sahel", 14)
        value = [['شرح حال', 'شماره همراه ', 'گروه خونی ', 'کدملی', 'سن', 'جنسیت', 'مشخصات', 'شناسه بیمار']]
        xy_frame = CTkXYFrame(self.win, width=1540, height=430)
        xy_frame.place(x=20, y=410)

        for patient in all_patients:
            if patient.person.deleted == 0:
                _ = [patient.current_conditions, patient.person.phone, patient.blood_type,
                     patient.person.username,cls.calculate_age(patient.person.birth_date),
                     patient.gender, f"{patient.person.name} {patient.person.family}",
                     patient.id]
                value.append(_)

        cls.table = CTkTable(master=xy_frame, row=len(value), column=8, font=font_tuple,width=150, wraplength=250, values=value)
        cls.table.pack(fill="both", expand=True, padx=5, pady=5)

    @classmethod
    def calculate_age(cls, born):
        today = datetime.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError:
            birthday = born.replace(year=today.year,
                                    month=born.month + 1, day=1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year
