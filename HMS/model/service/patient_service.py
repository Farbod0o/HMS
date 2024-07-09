from sqlalchemy import and_
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.patient import Patient
from HMS.model.entity.person import Person
from HMS.model.service.service import Service


class PatientService(Service):
    @staticmethod
    def query_builder(name, family, userid, phone, gender, blood, birth_date):
        entity_da = DataAccess(Patient)
        _ = {name: Person._name,family: Person._family,userid:Person._username,phone:Person._phone,
             birth_date:Person._birth_date,gender:Patient._gender,blood:Patient._blood_type}
        conditions = []
        for i in _.keys():
            if i != "":
                conditions.append(i == _[i])

        res = entity_da.find_by_conditions(and_(*conditions),Patient._person_id == Person._id,Person)
        return res

