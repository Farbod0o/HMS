from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, date_validator, date_time_validator


class Appointment(Base):
    __tablename__ = "appointments_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _start_time = Column("start_time", DateTime, nullable=False)
    _end_time = Column("end_time", DateTime, nullable=False)
    _status = Column("status", Boolean, default=True)
    _cost = Column("cost", Integer, nullable=False)
    _payment_status = Column("payment_status", Boolean, default=True)

    _patient_id = Column(Integer, ForeignKey("patient_tbl.id"), nullable=False)
    _patient = relationship("Patient")

    _shift_id = Column(Integer, ForeignKey("shifts_tbl.id"), nullable=False)
    _shift = relationship("Shift")


    def __init__(self, shift, patient, start_time, end_time, cost=0, payment_status="pending"):
        self.id = None
        self._shift_id = shift
        self.start_time = start_time
        self.end_time = end_time
        self._patient_id = patient
        self.cost = cost
        self.payment_status = payment_status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validator.positive_int_validator(status, "Invalid Status")

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        self._payment_status = payment_status

