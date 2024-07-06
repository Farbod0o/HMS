from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, pattern_validator


class Department(Base):
    __tablename__ = "departments_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _head_id = Column(Integer, ForeignKey("doctors_tbl.id"), nullable=False)
    _person = relationship("Doctor")

    def __init__(self, name, head):
        self.id = None
        self.name = name
        self.head_id = head.id

    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$","Invalid Department Name")
    def name(self, name):
        self._name = name

    @property
    def head_id(self):
        return self._head_id

    @head_id.setter
    def head_id(self, head_id):
        self._head_id = head_id


