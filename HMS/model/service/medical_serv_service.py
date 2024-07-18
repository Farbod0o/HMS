from sqlalchemy import and_
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.person import Person
from HMS.model.service.service import Service


class MedicalServService(Service):
    @staticmethod
    def find_by_name(name):
        entity_da = DataAccess(MedicalService)
        return entity_da.find_by(MedicalService._medical_service == name)
