from HMS.model.da.data_access import DataAccess
from HMS.model.entity.appointment import Appointment
from HMS.model.service.service import Service


class AppointmentService(Service):
    @classmethod
    def save(cls, shift, appointment):
        shift_id = shift.id
        appointments_list = cls.find_by_shift_id(shift_id)
        new_start = appointment.start_time
        new_end = appointment.end_time
        if cls.is_within_interval(new_start, new_end, shift.start_time, shift.end_time):
            if not cls.is_overlapping(new_start, new_end, appointments_list):
                entity_da = DataAccess(Appointment)
                entity_da.save(appointment)
                return appointment
            else:
                raise Exception("This time interval is overlapping appointment")
        else:
            raise ValueError("Appointment is outside interval")

    @classmethod
    def is_within_interval(cls, start, end, interval_start, interval_end):
        return start >= interval_start and end <= interval_end

    @classmethod
    def is_overlapping(cls, new_start, new_end, appointments_list):
        for appointment in appointments_list:
            app_end = appointment.end_time
            app_start = appointment.start_time
            if not (new_end <= app_start or new_start >= app_end):
                return True
        return False

    @classmethod
    def find_by_shift_id(cls, shift_id):
        entity_da = DataAccess(Appointment)
        return entity_da.find_by(Appointment.shift_id == shift_id)
