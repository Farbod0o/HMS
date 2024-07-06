from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def registration(self):
    font_tuple = ("Sahel", 15,)

    self.name = TextWithLabel(self.win, ':نام بیمار', 1100, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.family = TextWithLabel(self.win, ':نام خانوادگی', 900, 200, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150)
    self.user = TextWithLabel(self.win, ':کد ملی', 700, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.phone = TextWithLabel(self.win, ':تلفن همراه', 500, 200, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=155, label_width=150)
    self.address = TextWithLabel(self.win, ':آدرس', 150, 200, font_conf=font_tuple, distance=0,
                                 v_distance=35, entry_width=300, label_width=300)

    self.gender = TextWithLabel(self.win, ':جنسیت', 1100, 280, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150, combo=["Male", "Female", "Other"])
    blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "O-", "O+"]
    self.blood_type = TextWithLabel(self.win, ':گروه خونی', 900, 280, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=155, label_width=150, combo=blood_types)
    self.password = TextWithLabel(self.win, ':رمز عبور', 700, 280, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=155, label_width=150)
    self.password2 = TextWithLabel(self.win, ':تکرار رمز عبور', 500, 280, font_conf=font_tuple, distance=0,
                                   v_distance=35, entry_width=155, label_width=150)
    self.email = TextWithLabel(self.win, ':ایمیل', 150, 280, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=300, label_width=300)
    self.birthday = TextWithLabel(self.win, ':تاریخ تولد', 1100, 360, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=150, label_width=150)

    tk.CTkButton(self.win, text="ثبت بیمار", width=150, font=font_tuple, command=self.add_patient).place(x=895, y=390)
