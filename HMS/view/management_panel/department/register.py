from functools import partial
import tkinter.messagebox as msg
from HMS.controller.controller import Controller
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def edit(self, user_id):
    print(user_id)
    p1 = Controller.find_by_id(Department,user_id.text)
    print(p1)
    if p1:
        font_tuple = ("Sahel", 15,)
        self.clear_sc()
        registration(self, button=False)
        self.name.set_variable(p1.name)
        self.head_id.set_variable(p1._head_id)

        #todo: کامند دکمه درست شود
        tk.CTkButton(self.win, text="ویرایش دپارتمان", width=150, font=font_tuple, command=self.add_patient).place(x=1105,
                                                                                                               y=280)
    else:
        msg.showwarning("Warning", "دپارتمانی با این شناسه یافت نشد!")




def check(self):
    font_tuple = ("Sahel", 15)
    cid = self.head_id.text
    doctor = Service.find_by_id(Doctor, cid)
    if doctor:
        name = doctor.person.name
        family = doctor.person.family
        specialty = doctor.specialty
        sub = doctor.sub_specialty
        text = "{} {} {}({})".format(name, family, specialty, sub)
    else:
        text = "Not found"

    self._ = TextWithLabel(self.win, ':مشخصات رییس دپارتمان', 500, 200, font_conf=font_tuple, distance=0,
                           v_distance=35, entry_width=300, label_width=300, disabled=True)
    self._.set_variable(text)


def registration(self,button=True):
    font_tuple = ("Sahel", 15)
    self.name = TextWithLabel(self.win, ':نام دپارتمان', 1100, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)
    self.head_id = TextWithLabel(self.win, ':شناسه رییس دپارتمان', 900, 200, font_conf=font_tuple, distance=0,
                                 v_distance=35, entry_width=156, label_width=150)

    b1 = tk.CTkButton(self.win, text="✅", width=5, font=font_tuple, command=partial(check, self))
    b1.place(x=860, y=233)
    if button:
        tk.CTkButton(self.win, text="ثبت دپارتمان", width=150, font=font_tuple,
                     command=self.add_department).place(x=1105, y=280)
