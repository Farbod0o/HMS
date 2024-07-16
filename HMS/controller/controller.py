from HMS.model.entity.appointment import Appointment
from HMS.model.entity.department import Department
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.med_serv import MedicalService
from HMS.model.entity.patient import Patient
from HMS.model.entity.person import Person
from HMS.model.entity.shift import Shift
from HMS.model.service.appointment_sercvice import AppointmentService
from HMS.model.service.doctor_service import DoctorService
from HMS.model.service.patient_service import PatientService
from HMS.model.service.service import Service
from HMS.model.tools.decorators import exception_handling


class Controller:
    @classmethod
    @exception_handling
    def login_check(cls, username, password):
        p1 = Service.find_by_username(Person, username)
        try:
            p1 = p1[0]
        except IndexError:
            return False, f"Username {username} not found"
        return True, p1

    @classmethod
    @exception_handling
    def add_person(cls, name, family, user, password, password2, birth, role, phone, email, address, ):
        if password != password2:
            print("Passwords do not match")
            return False, "Passwords do not match"
        person = Person(name, family, user, password, birth, role, phone, email, address, )
        return True, Service.save(person, Person)

    @classmethod
    @exception_handling
    def add_department(cls, name, head_id):
        head = cls.find_by_id(Doctor, head_id)
        department = Department(name, head)
        return True, Service.save(department, Department)

    @classmethod
    @exception_handling
    def add_doctor(cls, name, family, user, password, pas2, birth, role, phone, email, address, specialty, department,
                   sub, exp):
        status, person = cls.add_person(name, family, user, password, pas2, birth, role, phone, email, address)
        dr = Doctor(person, specialty, department, sub, exp)
        return True, Service.save(dr, Doctor)

    @classmethod
    @exception_handling
    def add_patient(cls, name, family, user, password, password2, birth, role, phone, email, address, gender, blood):
        status, person = cls.add_person(name, family, user, password, password2, birth, role, phone, email, address)
        patient = Patient(person, gender, blood)
        return True, Service.save(patient, Patient)

    @classmethod
    @exception_handling
    def add_service(cls, service_name, note):
        med_service = MedicalService(service_name, note)
        print(med_service)
        return True, Service.save(med_service, MedicalService)

    @classmethod
    @exception_handling
    def add_shift(cls, day, start, end, doc, service):
        shift = Shift(day, start, end, doc, service)
        return True, Service.save(shift, Shift)

    @classmethod
    @exception_handling
    def find_all(cls, entity):
        return True, Service.find_all(entity)

    @classmethod
    @exception_handling
    def find_by_id(cls, entity, user_id):
        return Service.find_by_id(entity, user_id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return Service.find_by_username(Person, username.text)

    @classmethod
    @exception_handling
    def find_by(cls, entity, statement):
        return Service.find_by(entity, statement)

    @classmethod
    @exception_handling
    def add_appointment(cls, shift, patient, start_time, end_time):
        appointment = Appointment(shift, patient, start_time, end_time)
        return True, AppointmentService.save(shift, appointment)

    @staticmethod
    @exception_handling
    def search_by_patient(name, family, userid, phone, gender, blood, birth_date):
        return True, PatientService.query_builder(name, family, userid, phone, gender, blood, birth_date)

    @staticmethod
    @exception_handling
    def search_by_doctor(name, family, userid, phone, speciality, sub, department, birth_date):
        return True, DoctorService.query_builder(name, family, userid, phone, speciality, sub, department, birth_date)
