from HMS.controller.controller import Controller
from HMS.model.entity.patient import Patient
from HMS.model.entity.shift import Shift
day = "2024/07/07"
# status, service = Controller.add_service("visit", "Note")
# print(status, service)
#
# natcode = 1909229193
# status, doc = Controller.add_doctor("farbod", "orang", f"{natcode}", "1234", "1234", "1998-04-04",
#                                     "Doctor", "09122655738", "adad@gmail.com", "address",
#                                     "Oncologist", "test", "sub", "exp")
#
# status, shift = Controller.add_shift(day, f"{day} 12:00:00", f"{day} 22:00:00", doc, service)
#
# status, person = Controller.add_patient("farbod", "family", "1585577781", "123a", "123a",
#                                         "1998-04-04", "Patient", "09122655738", "adad@gmail.com",
#                                         "address ", "Male", "A+")

# shift = Controller.find_by_id(Shift,1)
# person = Controller.find_by_id(Patient,1)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 13:33:00", f"{day} 13:34:00", )
# print(status)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 13:30:00", f"{day} 14:30:00", )
# print(status, app1)
# status, app1 = Controller.add_appointment(shift, person, f"{day} 14:00:00", f"{day} 15:00:00", )
# print(status, app1)

status , searched = Controller.search_by_patient("farbod","oeswo","123454","0911211231","None","","")
print(searched)