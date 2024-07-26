from HMS.controller.controller import Controller
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.patient import Patient
from HMS.model.entity.shift import Shift
import random as rand
day = "2024/07/07"
# status, service = Controller.add_service("visit", "Note")
# print(status, service)
#
natcode = 1311755003
# for i in range(40):
#     specialties = [
#         "Oncologist", "Hematologist", "Rheumatologist", "Endocrinologist", "Neurologist", "Psychiatrist",
#         "Neurosurgeon", "Orthopedic Surgeon", "Plastic Surgeon", "Urological Surgeon", "Pediatric Surgeon",
#         "Neonatologist", "Cardiologist", "Dermatologist", "Ophthalmologist", "General Surgeon",
#         "Radiologist", "Emergency Medicine", "Anesthesiologist", "Pathologist", "Pediatrician",
#     ]
#     spe = rand.choice(specialties)
#     natcode = natcode + i
#     name = ["فربد","محمد","رضا","احسان","فرشاد","فرامرز","محمدرضا","شهرام"]
#     name = rand.choice(name)
#     family = ["اورنگ","افشار","مصباح","فلاح","رنجبران","محبوب","خوشبخت","پورمحمد"]
#     family = rand.choice(family)
#     phone = f"0912{rand.randint(1000000,9000000)}"
#     status, doc = Controller.add_doctor(name, family, f"{natcode}", "1234", "1234", f"{rand.randint(1950,1998)}-04-04",
#                                         "Doctor", phone, "adad@gmail.com", "address",
#                                         spe, "test", "sub", "exp")

status, shift = Controller.add_shift(day, f"{day} 12:00:00", f"{day} 19:00:00", 2, "تست",30,50000,"ندارد")
#
# for i in range(40):
#     natcode = natcode + i
#     name = ["فربد","محمد","رضا","احسان","فرشاد","فرامرز","محمدرضا","شهرام"]
#     name = rand.choice(name)
#     print("===========",name)
#     family = ["اورنگ","افشار","مصباح","فلاح","رنجبران","محبوب","خوشبخت","پورمحمد"]
#     family = rand.choice(family)
#     phone = f"0912{rand.randint(1000000,9000000)}"
#     blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "O-", "O+"]
#     bt = rand.choice(blood_types)
#     gender = ["Male", "Female"]
#     gender = rand.choice(gender)
#     status, person = Controller.add_patient(name, family, natcode, "123a", "123a",
#                                             f"{rand.randint(1950,1998)}-04-04", "Patient", phone, "adad@gmail.com",
#                                             "address ", gender, bt)
#
# shift = Controller.find_by_id(Shift,1)
# person = Controller.find_by_id(Patient,1)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 13:33:00", f"{day} 13:34:00", )
# print(status)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 13:30:00", f"{day} 14:30:00", )
# print(status)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 14:00:00", f"{day} 15:00:00", )
# print(status)
#

