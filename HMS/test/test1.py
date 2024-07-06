from HMS.controller.controller import Controller
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.patient import Patient
from HMS.model.entity.department import Department
from HMS.model.entity.person import Person
from datetime import datetime

# status,per = Controller.add_person("farbod","orang","1311744009","123","123",
#                                    "1998-04-04","Admin","09122655738","dafa@gmail.com","dds")
# print(status,per)
natcode = 1909499393

# for i in range(30):
#     natcode = natcode + 1
#     status, doc = Controller.add_doctor("farbod","orang",f"{natcode}","1234","1234","1998-04-04",
#                                          "Doctor","09122655738","adad@gmail.com","adafdasf",
#                                          "Oncologist","test","sub","exp")

status , person = Controller.add_patient("farbod","family","1587777889","123a","123a",
                       "1998-04-04","Patient","09122655738","adad@gmail.com",
                       "aad asdad ","Male","A+")

print(status,person)

# status, dep = controller.add_department("test", doc.id)
# print(status, dep)
#
