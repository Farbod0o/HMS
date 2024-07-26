from sqlalchemy import and_
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.person import Person
from HMS.model.service.service import Service


class DepartmentService(Service):
    @staticmethod
    def query_builder(name, uid):
        try:
            uid = int(uid)
        except:
            pass
        entity_da = DataAccess(Department)
        _ = {name: Department._name, uid: Department._id}
        conditions = []
        for i in _.keys():
            if i != "":
                conditions.append(i == _[i])
        res = entity_da.find_by_conditions(and_(*conditions), Department._head_id == Doctor._id, Doctor)
        return res

    @staticmethod
    def find_by_department(entity,department):
        entity_da = DataAccess(entity)
        return entity_da.find_by(entity._department == department)
