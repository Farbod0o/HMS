from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.entity.doctor import Doctor
from HMS.model.tools.validator import Validator, pattern_validator


class MedicalService(Base):
    __tablename__ = "medical_services_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _medical_service = Column("medical_service", String(20), unique=True)
    _note = Column("note", String(255))
    _status = Column("status", Boolean, default=True)

    def __init__(self, medical_service, note, status=True):
        self.id = None
        self.medical_service = medical_service
        self.note = note
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def medical_service(self):
        return self._medical_service

    @medical_service.setter
    @pattern_validator(r"^[\u0600-\u06FF\sa-zA-Z]{3,30}$", "Invalid Medical Service Name")
    def medical_service(self, medical_service):
        self._medical_service = medical_service

    @property
    def note(self):
        return self._note

    @note.setter
    @pattern_validator(r'^.{1,100}$',"Invalid Note")
    def note(self, note):
        self._note = note

    def __repr__(self):
        return f"{self.__dict__}"
