from HMS.controller.controller import Controller
from HMS.model.entity.patient import Patient
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk
import tkinter.messagebox as msg


def edit(self, user_id):
    p1 = Controller.find_by_username(user_id)
    if len(p1)>0:
        p2 = Controller.find_by(Patient, Patient._person_id == p1[0].id)
    if len(p1)>0 and len(p2) > 0:
        p1, p2 = p1[0],p2[0]
        font_tuple = ("Sahel", 15,)
        self.clear_sc()
        birth_date = p1.birth_date
        birth_date = f"{birth_date}"

        birth_date = birth_date.replace(" 00:00:00", "")
        registration(self, button=False)
        self.name.set_variable(p1.name)
        self.family.set_variable(p1.family)
        self.user.set_variable(p1.username)
        self.phone.set_variable(p1.phone)
        self.email.set_variable(p1.email)
        self.birthday.set_variable(birth_date)
        self.address.set_variable(p1.address)
        self.gender.set_variable(p2.gender)
        self.blood_type.set_variable(p2.blood_type)
        #todo: کامند دکمه درست شود
        tk.CTkButton(self.win, text="ویرایش بیمار", width=150, font=font_tuple, command=self.add_patient).place(x=895,
                                                                                                                y=392)
    else:
        msg.showwarning("Warning", "بیماری با این کد ملی یافت نشد!")


def registration(self, button=True):
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
    if button:
        tk.CTkButton(self.win, text="ثبت بیمار", width=150, font=font_tuple, command=self.add_patient).place(x=895,
                                                                                                             y=391)
