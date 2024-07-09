from sqlalchemy import create_engine, and_, or_, exc
from HMS.model.da.data_access import DataAccess
from HMS.model.entity.appointment import Appointment
from HMS.model.entity.shift import Shift
from HMS.model.service.service import Service


class AppointmentService(Service):
    @classmethod
    def save(cls, shift, appointment):
        if appointment.end_time > appointment.start_time:
            check1 = cls.shift_check(shift, appointment)
            if check1:
                check2 = cls.appointment_check(appointment)
                if not check2:
                    entity_da = DataAccess(Appointment)
                    entity_da.save(appointment)
                    return appointment
                else:
                    raise ValueError("Appointment already exists")
            else:
                raise ValueError("The appointment must be in a shift")
        else:
            raise ValueError("start time must be less than end time")

    @classmethod
    def shift_check(cls, shift, appointment):
        shift_id = shift.id
        start = appointment.start_time
        end = appointment.end_time

        entity_da = DataAccess(Shift)
        res = entity_da.find_by(and_(
            Shift._id == shift_id,
            start >= Shift._start_time,
            end <= Shift._end_time))
        return res

    @classmethod
    def appointment_check(cls, appointment):
        start = appointment.start_time
        end = appointment.end_time
        entity_da = DataAccess(Appointment)
        a = entity_da.find_by(or_(
            Appointment._start_time.between(start, end),
            Appointment._end_time.between(start, end)
        ))

        return a
    @classmethod
    def find_by_shift_id(cls, shift_id):
        entity_da = DataAccess(Appointment)
        return entity_da.find_by(Appointment.shift_id == shift_id)
