from CTkTable import *
import customtkinter as tk

from HMS.view.component.CTkXYFrame import CTkXYFrame


class DoctorInfo:
    @classmethod
    def show(cls,self, doctor):
        win = tk.CTk()
        win.title("Doctor Info")
        win.geometry("400x450")
        font_tuple = ("Sahel", 14,)
        try:
            self.table.destroy()
        except Exception as e:
            print(e)
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
    def show_menu(cls, self, doctor):
        all_doctors = doctor
        value = [['کدملی', 'ایمیل', 'همراه شماره', 'دپارتمان', 'فوق', 'تخصص', 'کدملی', 'خانوادگی نام و نام ', 'شناسه پزشک']]
        font_tuple = ("Sahel", 13)
        xy_frame = CTkXYFrame(self.win, width=1540, height=430)
        xy_frame.place(x=20, y=410)
        for doctor in all_doctors:
            if doctor.person.deleted == 0:
                _ = [doctor.person.username, doctor.person.email, doctor.person.phone, doctor.department,
                     doctor.sub_specialty, doctor.specialty, doctor.person.username,
                     f"{doctor.person.name} {doctor.person.family}", doctor.id]
                value.append(_)

        cls.table = CTkTable(master=xy_frame, row=len(value), column=9,width=133, font=font_tuple, wraplength=250, values=value)
        cls.table.pack(fill="both", expand=True, padx=5, pady=5)
