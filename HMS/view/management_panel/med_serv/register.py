from functools import partial
import tkinter.messagebox as msg
from HMS.controller.controller import Controller
from HMS.model.entity.med_serv import MedicalService
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def registration(self,button=True):
    font_tuple = ("Sahel", 15)
    self.name = TextWithLabel(self.win, ':نام سرویس', 1100, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)
    self.note = TextWithLabel(self.win, ':یادداشت', 900, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)

    if button:
        tk.CTkButton(self.win, text="ثبت سرویس", width=150, font=font_tuple,
                     command=self.add_med_serv).place(x=1105, y=290)

def edit(self, user_id):
    p2 = Controller.find_by(MedicalService, MedicalService._id == user_id.text)
    if len(p2) > 0:
        p2 = p2[0]
        font_tuple = ("Sahel", 15,)
        self.clear_sc()

        registration(self, button=False)
        self.name.set_variable(p2.medical_service)
        self.note.set_variable(p2.note)
        self.status = TextWithLabel(self.win, ':وضعیت', 700, 200, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=156, label_width=150)
        self.status.set_variable(p2._status)
        #todo: کامند دکمه درست شود
        tk.CTkButton(self.win, text="ویرایش سرویس", width=150, font=font_tuple, command=self.add_patient).place(x=1105,
                                                                                                                y=292)
    else:
        msg.showwarning("Warning", "سرویسی با این ایدی یافت نشد!")
