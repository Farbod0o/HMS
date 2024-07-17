from HMS.model.entity.department import Department
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def search_department(self):
    font_tuple = ("Sahel", 15,)
    text = ":فیلدهایی که قصد جست و جو بر اساس آن ها را دارید پر کرده و باقی را خالی بگذارید"
    tk.CTkLabel(self.win, text=text, width=600, anchor='e', font=font_tuple).place(x=650, y=200)

    self.department = TextWithLabel(self.win, ':شناسه دپارتمان', 1100, 250, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)

    departments = Service.find_all(Department)
    departments_list = []

    for _ in departments:
        departments_list.append(_.name)

    self.name = TextWithLabel(self.win, text=":نام دپارتمان", x=900, y=250, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=156, label_width=150, combo=departments_list)

    tk.CTkButton(self.win, text="جست و جو🔍", width=150, font=font_tuple, command=self.search_department).place(x=1105, y=330)
