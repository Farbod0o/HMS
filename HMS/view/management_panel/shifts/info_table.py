from functools import partial
from CTkTable import *
from HMS.controller.controller import Controller
import math
import customtkinter as tk

from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.shift import Shift
from HMS.model.service.service import Service


def view(self, p=1):
    self.clear_sc()
    status, all_services = Controller.find_all(Shift)
    font_tuple = ("Sahel", 15,)
    value = [[ 'هزینه', 'مدت', 'پایان', 'شروع','سرویس', 'پزشک', 'شناسه شیفت']]

    num = len(all_services)
    for service in all_services[(p - 1) * 15:15 * p]:
        status = service._status
        if status == 1:
            status = "Available"
            med = Controller.find_by_id(MedicalService, service._medical_service)
            doc = Controller.find_by_id(Doctor, service._doctor_id)
            _ = [ service.cost, service.duration, service.end_time, service.start_time,
                 med.medical_service, f'{doc.person._name} {doc.person._family}',service.id]
            value.append(_)
    if num > 15:
        num = math.ceil(num / 15)
    else:
        num = 1
    font_tuple = ("Sahel", 15)
    x = 658 - num * 12
    for i in range(num):
        i += 1
        tk.CTkButton(self.win, text=f"{i}", width=15, font=font_tuple, command=partial(view, self, p=i)).place(x=x,
                                                                                                               y=740)
        x += 25
    table = CTkTable(master=self.win, row=16, column=7, width=175, values=value, font=font_tuple)
    table.place(x=20, y=200)

