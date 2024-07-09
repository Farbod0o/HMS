from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def search_patient(self):
    font_tuple = ("Sahel", 15,)
    text = ":فیلدهایی که قصد جست و جو بر اساس آن ها را دارید پر کرده و باقی را خالی بگذارید"
    tk.CTkLabel(self.win, text=text, width=600, anchor='e', font=font_tuple).place(x=650, y=200)

    self.name = TextWithLabel(self.win, ':نام بیمار', 1100, 250, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.family = TextWithLabel(self.win, ':نام خانوادگی', 900, 250, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150)
    self.user = TextWithLabel(self.win, ':کد ملی', 700, 250, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.phone = TextWithLabel(self.win, ':تلفن همراه', 500, 250, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=155, label_width=150)
    self.gender = TextWithLabel(self.win, ':جنسیت', 1100, 330, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150, combo=["Male", "Female", "Other"])
    blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "O-", "O+"]
    self.blood_type = TextWithLabel(self.win, ':گروه خونی', 900, 330, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=155, label_width=150, combo=blood_types)

    self.birthday = TextWithLabel(self.win, ':تاریخ تولد', 700, 330, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=150, label_width=150)

    tk.CTkButton(self.win, text="جست و جو🔍", width=150, font=font_tuple, command=self.search_patient).place(x=505, y=360)
