from HMS.controller.controller import Controller
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk
import tkinter.messagebox as msg


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
        self.specialty.set_variable(p2.specialty)
        self.sub_specialty.set_variable(p2.sub_specialty)
        self.experience.set_variable(p2.experience)
        self.department.set_variable(p2.department)

        #todo: کامند دکمه درست شود
        tk.CTkButton(self.win, text="ویرایش پزشک", width=150, font=font_tuple, command=self.add_patient).place(x=1100,
                                                                                                               y=450)
    else:
        msg.showwarning("Warning", "پزشکی با این کد ملی یافت نشد!")


def registration(self, button=True):
    font_tuple = ("Sahel", 15)

    self.name = TextWithLabel(self.win, ':نام پزشک', 1100, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)
    self.family = TextWithLabel(self.win, ':نام خانوادگی', 900, 200, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=156, label_width=150)
    self.user = TextWithLabel(self.win, ':کد ملی', 700, 200, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=156, label_width=150)
    self.phone = TextWithLabel(self.win, ':تلفن همراه', 500, 200, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=156, label_width=150)
    self.address = TextWithLabel(self.win, ':آدرس', 150, 200, font_conf=font_tuple, distance=0,
                                 v_distance=35, entry_width=301, label_width=300)
    self.birthday = TextWithLabel(self.win, ':تاریخ تولد', 1100, 280, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=150, label_width=150)
    self.password = TextWithLabel(self.win, ':رمز عبور', 900, 280, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=156, label_width=150)
    self.password2 = TextWithLabel(self.win, ':تکرار رمز عبور', 700, 280, font_conf=font_tuple, distance=0,
                                   v_distance=35, entry_width=156, label_width=150)
    self.email = TextWithLabel(self.win, ':ایمیل', 150, 280, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=301, label_width=300)

    specialties = [
        "Oncologist", "Hematologist", "Rheumatologist", "Endocrinologist", "Neurologist", "Psychiatrist",
        "Neurosurgeon", "Orthopedic Surgeon", "Plastic Surgeon", "Urological Surgeon", "Pediatric Surgeon",
        "Neonatologist", "Cardiologist", "Dermatologist", "Ophthalmologist", "General Surgeon",
        "Radiologist", "Emergency Medicine", "Anesthesiologist", "Pathologist", "Pediatrician",
    ]
    departments = Service.find_all(Department)
    departments_list = []

    for _ in departments:
        departments_list.append(_.name)

    self.specialty = TextWithLabel(self.win, text=":تخصص", x=1100, y=360, font_conf=font_tuple, distance=0,
                                   v_distance=35, entry_width=156, label_width=150, combo=specialties)
    self.sub_specialty = TextWithLabel(self.win, text=":فوق تخصص", x=900, y=360, font_conf=font_tuple, distance=0,
                                       v_distance=35, entry_width=156, label_width=150)
    self.department = TextWithLabel(self.win, text=":دپارتمان", x=500, y=280, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=156, label_width=150, combo=departments_list)
    self.experience = TextWithLabel(self.win, text=":سابقه", x=500, y=360, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=350, label_width=350)
    if button:
        tk.CTkButton(self.win, text="ثبت پزشک", width=150, font=font_tuple, command=self.add_doctor).place(x=1105,
                                                                                                           y=450)
