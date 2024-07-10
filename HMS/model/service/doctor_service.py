from sqlalchemy import and_
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.person import Person
from HMS.model.service.service import Service


class DoctorService(Service):
    @staticmethod
    def query_builder(name, family, userid, phone, speciality, sub, department, birth_date):
        entity_da = DataAccess(Doctor)
        _ = {name: Person._name, family: Person._family, userid: Person._username, phone: Person._phone,
             birth_date: Person._birth_date, speciality: Doctor._specialty, sub: Doctor._sub_specialty,
             department: Doctor._department, }
        conditions = []
        for i in _.keys():
            if i != "":
                conditions.append(i == _[i])

        res = entity_da.find_by_conditions(and_(*conditions), Doctor._person_id == Person._id, Person)
        return res
