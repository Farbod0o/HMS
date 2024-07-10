from HMS.model.entity.department import Department
from HMS.model.service.service import Service
from HMS.view.component.label_text import TextWithLabel
import customtkinter as tk


def search_doctor(self):
    font_tuple = ("Sahel", 15,)
    text = ":فیلدهایی که قصد جست و جو بر اساس آن ها را دارید پر کرده و باقی را خالی بگذارید"
    tk.CTkLabel(self.win, text=text, width=600, anchor='e', font=font_tuple).place(x=650, y=200)

    self.name = TextWithLabel(self.win, ':نام پزشک', 1100, 250, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.family = TextWithLabel(self.win, ':نام خانوادگی', 900, 250, font_conf=font_tuple, distance=0,
                                v_distance=35, entry_width=155, label_width=150)
    self.user = TextWithLabel(self.win, ':کد ملی', 700, 250, font_conf=font_tuple, distance=0,
                              v_distance=35, entry_width=155, label_width=150)
    self.phone = TextWithLabel(self.win, ':تلفن همراه', 500, 250, font_conf=font_tuple, distance=0,
                               v_distance=35, entry_width=155, label_width=150)

    self.birthday = TextWithLabel(self.win, ':تاریخ تولد', 500, 330, font_conf=font_tuple, distance=0,
                                  v_distance=35, entry_width=150, label_width=150)
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

    self.specialty = TextWithLabel(self.win, text=":تخصص", x=1100, y=330, font_conf=font_tuple, distance=0,
                                   v_distance=35, entry_width=156, label_width=150, combo=specialties)
    self.sub_specialty = TextWithLabel(self.win, text=":فوق تخصص", x=900, y=330, font_conf=font_tuple, distance=0,
                                       v_distance=35, entry_width=156, label_width=150)
    self.department = TextWithLabel(self.win, text=":دپارتمان", x=700, y=330, font_conf=font_tuple, distance=0,
                                    v_distance=35, entry_width=156, label_width=150, combo=departments_list)

    tk.CTkButton(self.win, text="جست و جو🔍", width=150, font=font_tuple, command=self.search_doctor).place(x=295, y=365)
