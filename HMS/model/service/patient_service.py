from sqlalchemy import create_engine, and_, or_, exc
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.patient import Patient
from HMS.model.service.service import Service


class PatientService(Service):
    @staticmethod
    def query_maker(name, family, userid, phone, gender, blood, birth_date):
        entity_da = DataAccess(Patient)
        a = entity_da.find_by_id(1)
        print(a)
        _ = {name: Patient.person._name}
        conditions = []
        for i in _.keys():
            if i != "":
                conditions.append(i == _[i])

        res = entity_da.find_by(and_(*conditions))
        return res
