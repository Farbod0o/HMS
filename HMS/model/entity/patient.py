from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, pattern_validator


class Patient(Base):
    __tablename__ = "patients_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _gender = Column("gender", String(20), nullable=False)
    _current_conditions = Column("current_conditions", String(20), nullable=False)
    _blood_type = Column("blood_type", String(30))

    _person_id = Column(Integer, ForeignKey("person_tbl.id"), nullable=False)
    _person = relationship("Person")

    # appointments = relationship("Appointment", back_populates="patient")

    def __init__(self, person, gender, blood_type, current_conditions="None"):
        self.id = None
        self.gender = gender
        self.blood_type = blood_type
        self.current_conditions = current_conditions
        self.person_id = person.id

    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = Validator.gender_validator(gender, "Invalid Gender")

    @property
    def blood_type(self):
        return self._blood_type

    @blood_type.setter
    def blood_type(self, blood_type):
        self._blood_type = Validator.blood_type_validator(blood_type, "Invalid Blood Type")

    @property
    def current_conditions(self):
        return self._current_conditions

    @current_conditions.setter
    @pattern_validator(r'^.{1,100}$',"Invalid condition")
    def current_conditions(self, current_conditions):
        self._current_conditions = current_conditions


