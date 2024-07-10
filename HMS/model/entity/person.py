from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from HMS.model.da.data_access import Base
from HMS.model.tools.validator import Validator, pattern_validator, date_validator


class Person(Base):
    __tablename__ = "person_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _username = Column("username", String(20), nullable=False, unique=True)
    _password = Column("password", String(255), nullable=False)
    _birth_date = Column("birth_date", DateTime, nullable=False)
    _role = Column("role", String(20), nullable=False)
    _phone = Column("phone", String(20))
    _email = Column("email", String(50))
    _address = Column("address", String(255))
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, family, username, password, birth_date, role,
                 phone=None, email=None, address=None, status=True, deleted=False):
        self._id = None
        self._name = name
        self._family = family
        self._username = username
        self._password = password
        self._birth_date = birth_date
        self._role = role
        self._phone = phone
        self._email = email
        self._address = address
        self._status = status
        self._deleted = deleted

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
    @pattern_validator(r"^[\u0600-\u06FF\s]{2,30}$", "Invalid Name")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[\u0600-\u06FF\s]{2,30}$", "Invalid Family")
    def family(self, family):
        self._family = family

    @property
    def username(self):
        return self._username

    @username.setter
    @pattern_validator(r"(^\d{10}$|^\d{3}-\d{6}-\d{1}$)", "Invalid Username")
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    @pattern_validator(r"^[\w@!#$%^&*()=\s]{2,16}$", "Invalid Password")
    def password(self, password):
        self._password = password

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    @date_validator("Invalid date of birth")
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = Validator.role_validator(role, "Invalid Role")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    @pattern_validator(r"^(09|\+989)\d{9}$","Invalid Phone Number")
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    @pattern_validator(r"(^.{3,}@(gmail|yahoo)\.com$)","Invalid Email Address")
    def email(self, email):
        self._email = email

    @property
    def address(self):
        return self._address

    @address.setter
    @pattern_validator(r'^.{1,100}$',"Invalid Address")
    def address(self, address):
        self._address = address

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validator.positive_int_validator(status, "Invalid Status")

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = Validator.positive_int_validator(deleted, "Invalid Deleted")
