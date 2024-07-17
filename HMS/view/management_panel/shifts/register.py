from functools import partial

from HMS.controller.controller import Controller
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.patient import Patient
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk
import tkinter.messagebox as msg


def check(self):
    print("hi")
    font_tuple = ("Sahel", 15)
    cid = self.doctor_id.text
    doctor = Service.find_by_id(Doctor, cid)
    if doctor:
        name = doctor.person.name
        family = doctor.person.family
        specialty = doctor.specialty
        sub = doctor.sub_specialty
        text = "{} {} {}({})".format(name, family, specialty, sub)
    else:
        text = "Not found"
    print(text)

    self._.set_variable(text)


def edit(self, user_id):
    p1 = Controller.find_by_username(user_id)
    if len(p1) > 0:
        p2 = Controller.find_by(Patient, Patient._person_id == p1[0].id)
    if len(p1) > 0 and len(p2) > 0:
        p1, p2 = p1[0], p2[0]
        font_tuple = ("Sahel", 15,)
        self.clear_sc()
        birth_date = p1.birth_date
        birth_date = f"{birth_date}"
        print(birth_date)
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
    status, services = Controller.find_all(MedicalService)
    services_name = []
    for service in services:
        services_name.append(service.medical_service)
    self.name = TextWithLabel(self.win, ':سرویس', 1100, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150, combo=services_name)
    self.family = TextWithLabel(self.win, ':زمان شروع', 900, 200, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150)
    self.user = TextWithLabel(self.win, ':زمان پایان', 700, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.phone = TextWithLabel(self.win, ':مدت زمان هر ملاقات', 500, 200, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=155, label_width=150)
    self.phone = TextWithLabel(self.win, ':یادداشت', 500, 280, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=155, label_width=150)
    self.gender = TextWithLabel(self.win, ':تاریخ شروع', 1100, 280, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150)
    self.blood_type = TextWithLabel(self.win, ':تایخ پایان', 900, 280, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=155, label_width=150)
    self.password = TextWithLabel(self.win, ':هزینه هر ملاقات', 700, 280, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=155, label_width=150)
    self.doctor_id = TextWithLabel(self.win, ':شناسه پزشک', 1100, 360, font_conf=font_tuple, distance=0,
                                   v_distance=35, entry_width=156, label_width=150)
    self._ = TextWithLabel(self.win, ':مشخصات پزشک', 705, 360, font_conf=font_tuple, distance=0,
                           v_distance=35, entry_width=340, label_width=340, disabled=True)

    b1 = tk.CTkButton(self.win, text="✅", width=5, font=font_tuple, command=partial(check, self))
    b1.place(x=1055, y=396)

    #todo: شناسه دکتر شیفت اضافه شود
    tk.CTkLabel(self.win, text="این شیفت را برای کدام روزهای هفته انتخاب میکنید؟", width=300, anchor='e',
                font=font_tuple).place(x=105, y=210)
    self.shanbe = tk.CTkCheckBox(master=self.win, text="شنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.shanbe.place(x=350, y=260)
    self.yek = tk.CTkCheckBox(master=self.win, text="یکشنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.yek.place(x=250, y=260)
    self.do = tk.CTkCheckBox(master=self.win, text="دوشنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.do.place(x=150, y=260)
    self.se = tk.CTkCheckBox(master=self.win, text="سه شنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.se.place(x=50, y=260)
    self.char = tk.CTkCheckBox(master=self.win, text="چهارشنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.char.place(x=250, y=300)
    self.panj = tk.CTkCheckBox(master=self.win, text="پنجشنبه", onvalue="on", offvalue="off", font=font_tuple)
    self.panj.place(x=150, y=300)
    self.jome = tk.CTkCheckBox(master=self.win, text="جمعه", onvalue="on", offvalue="off", font=font_tuple)
    self.jome.place(x=50, y=300)
    if button:
        tk.CTkButton(self.win, text="ثبت شیفت ها", width=150, font=font_tuple, command=self.add_patient).place(x=505,
                                                                                                               y=396)
