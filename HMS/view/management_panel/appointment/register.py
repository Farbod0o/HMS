import datetime
from functools import partial
from HMS.controller.controller import Controller
from HMS.model.entity.appointment import Appointment
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.patient import Patient
from HMS.model.entity.person import Person
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
        registration(self)
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
    tk.CTkLabel(self.win, text=f" ", width=1270, height=500, font=("Sahel", 14), text_color="#D9E9FF",
                corner_radius=10).place(x=10, y=350)
    font_tuple = ("Sahel", 15)
    doc_id = self.doctor.text
    try:
        doc_id = int(doc_id.split("(")[-1].replace(")", ""))
    except:
        pass
    try:
        medserv_id = Controller.find_medserv_by_name(self.medserv.text)[0].id
    except:
        medserv_id = ""

    status, shifts = Controller.search_by_shifts(doc_id, medserv_id, self.date_.text)
    if len(shifts) < 1:
        MessageBox.show_error("هیچ شیفت فعالی برای شما یافت نشد!!!")

    y = 300
    n = 0
    for shift in shifts:
        if shift.status and n < 3 and shift._medical_service == medserv_id:
            x = 20
            y += 50
            doc_name = Controller.find_by_id(Doctor, shift.doctor_id)
            date_ = f"{shift.day}"
            date_ = date_.replace("00:00:00", "")
            type_ = Controller.find_by_id(MedicalService, medserv_id)
            tk.CTkLabel(self.win,
                        text=f"{doc_name.person.name} {doc_name.person.family} ({doc_name._specialty}) - {date_} ({type_._medical_service})",
                        width=1220, height=20, font=("Sahel", 14), fg_color="#217171", text_color="#D9E9FF",
                        corner_radius=10).place(x=x, y=y)
            y += 40
            n += 1
            next_app = shift.start_time
            apps = Controller.find_by(Appointment, Appointment._shift_id == shift.id)
            for app in apps:
                if app._patient_id is None:
                    tk.CTkButton(self.win, text=f"{app.start_time} - {app.end_time}", width=5, fg_color="#4F7942", font=font_tuple,
                                 command=partial(get_appointment, self,app.id)).place(x=x, y=y)
                else:
                    tk.CTkButton(self.win, text=f"{app.start_time} - {app.end_time}", width=5, fg_color="#D22B2B",
                                 hover_color="#D22B2B", font=font_tuple).place(x=x, y=y)
                x += 110
                if x > 1200:
                    x = 20
                    y += 40

        else:
            pass

def get_appointment(self,app_id):
    ap1 = Controller.find_by_id(Appointment, app_id)
    p1 = Controller.find_by_username(self.name)[0]
    p1 = Controller.find_by(Patient, Patient._person_id == p1.id)[0]
    ap1._patient_id = p1.id
    status ,edited = Controller.edit(Appointment, ap1)
    if status:
        MessageBox.show_checkmark(self, "این نوبت رزرو شد!!!", option1="باشه")
def registration(self):
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
