from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, pattern_validator


class Doctor(Base):
    __tablename__ = "doctors_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _specialty = Column("specialty", String(20), nullable=False)
    _sub_specialty = Column("sub_specialty", String(20), nullable=False)
    _experience = Column("experience", String(255))
    _department = Column("department", String(30))

    _person_id = Column(Integer, ForeignKey("person_tbl.id"), nullable=False)
    person = relationship("Person", lazy='joined')

    def __init__(self, person, specialty, department, sub_specialty=None, experience=None):
        self._id = None
        self._specialty = specialty
        self._sub_specialty = sub_specialty
        self._experience = experience
        self._department = department
        self._person_id = person.id

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
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        self._specialty = Validator.specialty_validator(specialty, "Invalid specialty")

    @property
    def sub_specialty(self):
        return self._sub_specialty

    @sub_specialty.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid sub_specialty")
    def sub_specialty(self, sub_specialty):
        self._sub_specialty = sub_specialty

    @property
    def experience(self):
        return self._experience

    @experience.setter
    @pattern_validator(r'^.{1,100}$',"Invalid Experience")
    def experience(self, experience):
        self._experience = experience

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
