import math
from functools import partial
from CTkTable import *

import customtkinter as tk


class DoctorInfo:
    @classmethod
    def show(cls, self, doctor):
        win = tk.CTk()
        win.title("Doctor Info")
        win.geometry("400x450")
        font_tuple = ("Sahel", 13,)
        try:
            cls.table.destroy()
        except:
            pass
        tk.CTkLabel(win, text=f"نام و نام خانوادگی : {doctor.person.name} {doctor.person.family}", anchor='e',
                    width=370,
                    font=font_tuple).place(x=20, y=20)
        tk.CTkLabel(win, text=f"کد ملی : {doctor.person.username}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                  y=50)
        tk.CTkLabel(win, text=f"{doctor.specialty} : تخصص", anchor='e', width=370, font=font_tuple).place(x=20, y=80)
        tk.CTkLabel(win, text=f"{doctor.sub_specialty} : فوق", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                             y=110)
        tk.CTkLabel(win, text=f"دپارتمان : {doctor.department}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                               y=140)
        tk.CTkLabel(win, text=f"{doctor.person.birth_date} : تاریخ تولد", anchor='e', width=370, font=font_tuple).place(
            x=20, y=170)
        tk.CTkLabel(win, text=f"{doctor.person.username} : کد ملی", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                  y=200)
        tk.CTkLabel(win, text=f"{doctor.person.phone} : شماره تماس", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                                   y=230)
        tk.CTkLabel(win, text=f"{doctor.person.email} : ایمیل", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                              y=260)
        tk.CTkLabel(win, text=f"آدرس : {doctor.person.address}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                               y=290)
        tk.CTkLabel(win, text=f"تجربیات : {doctor.experience}", anchor='e', width=370, font=font_tuple).place(x=20,
                                                                                                              y=320)
        tk.CTkLabel(win, text=f"شناسه پزشک : {doctor.id}", anchor='e', width=370, font=font_tuple).place(x=20, y=350)

        win.mainloop()

    @classmethod
    # todo: کامل شود
    def show_menu(cls, self, doctor, p=1):
        all_doctors = doctor
        value = [['کدملی', 'ایمیل', 'همراه شماره', 'فوق', 'تخصص', 'کدملی', 'خانوادگی نام و نام ', 'آیدی']]

        num = len(all_doctors)
        for doctor in all_doctors[(p - 1) * 7:7 * p]:
            status = doctor.person.status
            if status == 1:
                status = "Available"
            if doctor.person.deleted == 0:
                _ = [doctor.person.username, doctor.person.email, doctor.person.phone, doctor.sub_specialty,
                     doctor.specialty, doctor.person.username, f"{doctor.person.name} {doctor.person.family}",
                     doctor.id]
                value.append(_)
        if num > 7:
            num = math.ceil(num / 7)
        else:
            num = 1
        font_tuple = ("Sahel", 14)
        x = 658 - num * 12
        for i in range(num):
            i += 1
            tk.CTkButton(self.win, text=f"{i}", width=15, font=font_tuple,
                         command=partial(cls.show_menu, self, p=i)).place(x=x,
                                                                          y=740)
            x += 25
        cls.table = CTkTable(master=self.win, row=8, column=8, font=font_tuple, wraplength=250, values=value)
        cls.table.place(x=20, y=430)
