from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, date_validator, date_time_validator


class Shift(Base):
    __tablename__ = "shifts_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _day = Column("shift_date", DateTime, nullable=False)
    _start_time = Column("start_time", DateTime, nullable=False)
    _end_time = Column("end_time", DateTime, nullable=False)

    _doctor_id = Column(Integer, ForeignKey("doctor_tbl.id"), nullable=False)
    _doctor = relationship("Doctor")

    _medical_service = Column(Integer, ForeignKey("medical_services_tbl.id"), nullable=False)
    _medical = relationship("MedicalService")

    def __init__(self, day, start_time, end_time, doctor, medical_service):
        self.id = None
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.medical_service = medical_service
        self.doctor = doctor

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
    @date_validator
    def day(self, day):
        self._day = day

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    @date_time_validator
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    @date_time_validator
    def end_time(self, end_time):
        self._end_time = end_time
