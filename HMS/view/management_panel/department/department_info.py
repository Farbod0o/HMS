
from CTkTable import *
import customtkinter as tk

from HMS.controller.controller import Controller
from HMS.view.component.CTkXYFrame import CTkXYFrame
from datetime import datetime


class DepartmentInfo:
    @classmethod
    def show_menu(cls, self, department):
        font_tuple = ("Sahel", 18)
        department = department[0]
        label = tk.CTkLabel(self.win, text=f"دپارتمان {department.name}", width=1250, height=50, font=font_tuple, fg_color="#0F6BAE",
                            text_color="#D0E0FF", corner_radius=10)
        label.place(x=20, y=380)
        status , doctors_list = Controller.find_doc_by_department(department.name)
        value = [['ایمیل', 'شماره همراه', 'دپارتمان', 'فوق', 'تخصص', 'کدملی', 'مشخصات پزشک ', 'شناسه پزشک']]
        font_tuple = ("Sahel", 13)
        xy_frame = CTkXYFrame(self.win, width=1550, height=385)
        xy_frame.place(x=25, y=450)
        for doctor in doctors_list:
            if doctor.person.deleted == 0:
                _ = [ doctor.person.email, doctor.person.phone, doctor.department,
                     doctor.sub_specialty, doctor.specialty, doctor.person.username,
                     f"{doctor.person.name} {doctor.person.family}", doctor.id]
                value.append(_)

        cls.table = CTkTable(master=xy_frame, row=len(value), column=8,width=150, font=font_tuple, wraplength=180, values=value)
        cls.table.pack(fill="both", expand=True, padx=5, pady=5)

