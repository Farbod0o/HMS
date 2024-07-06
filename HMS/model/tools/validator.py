import re
from datetime import datetime


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text, str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_validator(message):
    def inner1(function_name):
        def inner2(self, date_param):
            if isinstance(date_param, datetime):
                result = function_name(self, date_param)
            elif isinstance(date_param, str):
                date_param = date_param.replace('/', '-')
                try:
                    date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
                    result = function_name(self, date_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, datetime):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def boolean_validator(message):
    def inner1(function_name):
        def inner2(self, bool_param):
            if isinstance(bool_param, bool):
                result = function_name(self, bool_param)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


class Validator:

    @classmethod
    def positive_int_validator(cls, int_value, message):
        if isinstance(int_value, int) and int_value >= 0:
            return int_value
        else:
            raise ValueError(message)

    @classmethod
    def role_validator(cls, role, message):
        roles = ["Doctor", "Patient", "Admin", ]
        if isinstance(role, str) and role in roles:
            return role
        else:
            raise ValueError(message)

    @classmethod
    def gender_validator(cls, gender, message):
        genders = ["Male", "Female", "Other"]
        if isinstance(gender, str) and gender in genders:
            return gender
        else:
            raise ValueError(message)

    @classmethod
    def blood_type_validator(cls, blood_type, message):
        blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "O-", "O+"]
        if isinstance(blood_type, str) and blood_type in blood_types:
            return blood_type
        else:
            raise ValueError(message)

    @classmethod
    def specialty_validator(cls, specialty, message):
        specialties = [
            "Oncologist", "Hematologist", "Rheumatologist", "Endocrinologist", "Neurologist", "Psychiatrist",
            "Neurosurgeon", "Orthopedic Surgeon", "Plastic Surgeon", "Urological Surgeon", "Pediatric Surgeon",
            "Neonatologist", "Cardiologist", "Dermatologist", "Ophthalmologist", "General Surgeon",
            "Radiologist", "Emergency Medicine", "Anesthesiologist", "Pathologist", "Pediatrician",
        ]
        if isinstance(specialty, str) and specialty in specialties:
            return specialty
        else:
            raise ValueError(message)
