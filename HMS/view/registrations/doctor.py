from HMS.model.entity.department import Department
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def registration(self):
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

    tk.CTkButton(self.win, text="ثبت پزشک", width=150, font=font_tuple, command=self.add_doctor).place(x=1105, y=450)
