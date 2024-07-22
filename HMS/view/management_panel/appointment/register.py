import datetime
from functools import partial

from HMS.controller import controller
from HMS.controller.controller import Controller
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.shift import Shift
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk
import tkinter.messagebox as msg

from HMS.view.component.msg_handler import MessageBox


def edit(self, user_id):
    p1 = Controller.find_by_username(user_id)
    if len(p1) > 0:
        p2 = Controller.find_by(Doctor, Doctor._person_id == p1[0].id)
    else:
        p2 = []

    if len(p1) > 0 and len(p2) > 0:
        p1, p2 = p1[0], p2[0]
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
        self.specialty.set_variable(p2.specialty)
        self.sub_specialty.set_variable(p2.sub_specialty)
        self.experience.set_variable(p2.experience)
        self.department.set_variable(p2.department)

        # todo: کامند دکمه درست شود
        tk.CTkButton(self.win, text="ویرایش پزشک", width=150, font=font_tuple, command=self.add_patient).place(x=1100,
                                                                                                               y=450)
    else:
        msg.showwarning("Warning", "پزشکی با این کد ملی یافت نشد!")


def check1(self):
    if self.name.text == "" or self.department.text == "":
        MessageBox.show_warning("ابتدا کدملی و دپارتمان مورد نظر را انتخاب کنید")
    font_tuple = ("Sahel", 15)
    patient = Controller.find_by_username(self.name)[0]
    status, doctors_list = Controller.find_doc_by_department(self.department.text)
    _list = []
    for doctor in doctors_list:
        _list.append(f"{doctor.person.name} {doctor.person.family} ({doctor.id})")

    self.doctor = TextWithLabel(self.win, ':نام پزشک', 300, 240, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=156, label_width=150, combo=_list)
    self.date_ = TextWithLabel(self.win, ':تاریخ', 100, 240, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=156, label_width=150)

    self.family = TextWithLabel(self.win, ":مشخصات بیمار", 500, 240, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=156, label_width=150)
    self.family.set_variable(f"{patient._name} {patient._family}")
    b2 = tk.CTkButton(self.win, text="🔍", width=5, font=font_tuple, command=partial(check2, self))
    b2.place(x=60, y=275)


def check2(self):
    font_tuple = ("Sahel", 15)
    doc_id = self.doctor.text
    try:
        doc_id = int(doc_id.split("(")[-1].replace(")", ""))
        medserv_id = Controller.find_medserv_by_name(self.medserv.text)[0].id
    except:
        medserv_id = ""
    status, shifts = Controller.search_by_shifts(doc_id, medserv_id, self.date_.text)
    if len(shifts) < 1:
        MessageBox.show_error("هیچ شیفت فعالی برای شما یافت نشد!!!")

    y = 300
    n = 0
    for shift in shifts:
        y += 90
        x = 20
        if shift.status and n < 3:
            n += 1
            next_app = shift.start_time
            while True:
                start = next_app.strftime("%H:%M")
                print(shift.start_time, shift.end_time, shift.duration)
                next_app = next_app + datetime.timedelta(minutes=shift.duration)
                next_v = next_app.strftime("%H:%M")
                print("----", next_app)
                if next_app <= shift.end_time:
                    tk.CTkButton(self.win, text=f"{start} - {next_v}", width=5, font=font_tuple,
                                 command=partial(check1, self)).place(x=x, y=y)
                    x += 110
                    if x > 1200:
                        x = 20
                        y += 40

                else:
                    break
        else:
            print("no")


def registration(self, button=True):
    font_tuple = ("Sahel", 15)
    text = ":فیلد هایی که قصد جست و جو بر اساس آن ها را دارید پر کرده و باقی را خالی بگذارید"
    tk.CTkLabel(self.win, text=text, width=600, anchor='e', font=font_tuple).place(x=650, y=200)

    self.name = TextWithLabel(self.win, ':کدملی بیمار', 1100, 240, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)

    departments = Service.find_all(Department)
    departments_list = []

    for _ in departments:
        departments_list.append(_.name)

    self.department = TextWithLabel(self.win, text=":دپارتمان", x=900, y=240, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=156, label_width=150, combo=departments_list)
    status, services = Controller.find_all(MedicalService)
    services_name = []
    for service in services:
        services_name.append(service.medical_service)
    self.medserv = TextWithLabel(self.win, text=":سرویس", x=700, y=240, font_conf=font_tuple, distance=0,
                                 v_distance=35, entry_width=156, label_width=150, combo=services_name)

    b1 = tk.CTkButton(self.win, text="✅", width=5, font=font_tuple, command=partial(check1, self))
    b1.place(x=660, y=272)
