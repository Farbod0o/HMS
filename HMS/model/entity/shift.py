from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, date_validator, date_time_validator, pattern_validator, time_validator


class Shift(Base):
    __tablename__ = "shifts_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _day = Column("shift_date", DateTime)
    _start_time = Column("start_time", DateTime)
    _end_time = Column("end_time", DateTime)
    _note = Column("note", String(255))
    _status = Column("status", Boolean, default=True)

    _medical_service = Column(Integer, ForeignKey("medical_services_tbl.id"))
    medical = relationship("MedicalService")

    _doctor_id = Column(Integer, ForeignKey("doctors_tbl.id"))
    doctor = relationship("Doctor")

    def __init__(self, day, start_time, end_time, doctor, medical_service,note="None",status=True):
        self._id = None
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
        self._medical_service = medical_service.id
        self._doctor_id = doctor.id
        self._note = note
        self._status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def day(self):
        return self._day

    @day.setter
    @date_validator("Invalid Date")
    def day(self, day):
        self._day = day

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    @time_validator("Invalid Start time")
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    @time_validator("Invalid End time")
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def medical_service(self):
        return self._medical_service

    @medical_service.setter
    def medical_service(self, medical_service):
        self._medical_service = medical_service

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, doctor_id):
        self._doctor_id = doctor_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validator.positive_int_validator(status, "Invalid Status")

    @property
    def note(self):
        return self._note

    @note.setter
    @pattern_validator(r'^.{1,100}$',"Invalid Note")
    def note(self, note):
        self._note = note

    def __repr__(self):
        return f"{self.__dict__}"