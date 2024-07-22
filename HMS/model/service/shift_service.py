from sqlalchemy import and_
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.patient import Patient
from HMS.model.entity.person import Person
from HMS.model.entity.shift import Shift
from HMS.model.service.service import Service


class ShiftService(Service):
    @staticmethod
    def query_builder(doc_id, med_serv_id, date_):
        print("******:",doc_id, med_serv_id, date_)
        entity_da = DataAccess(Shift)
#todo: سرویس؟؟؟؟؟؟
        _ = {doc_id: Shift._doctor_id,date_:Shift._day}
        conditions = []
        for i in _.keys():
            if i != "":
                conditions.append(i == _[i])
        print(conditions)
        res = entity_da.find_by_conditions(and_(*conditions),Shift._doctor_id == Doctor._id,Doctor)
        return res
