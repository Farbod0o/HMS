from HMS.model.da.data_access import DataAccess
from HMS.model.tools.decorators import exception_handling


class Service:
    @staticmethod
    def save(obj,entity):
        entity_da = DataAccess(entity)
        entity_da.save(obj)
        return obj

    @staticmethod
    def find_all(entity):
        entity_da = DataAccess(entity)
        return entity_da.find_all()

    @staticmethod
    def find_by_id(entity,id):
        entity_da = DataAccess(entity)
        return entity_da.find_by_id(id)

    @staticmethod
    def find_by_username(entity,username):
        entity_da = DataAccess(entity)
        return entity_da.find_by(entity._username == username)

    @staticmethod
    def find_by(entity,statement):
        entity_da = DataAccess(entity)
        return entity_da.find_by(statement)
    @staticmethod
    def edit(obj,entity):
        entity_da = DataAccess(entity)
        res = entity_da.edit(obj)
        return res



    # @staticmethod
    # def remove(id):
    #     ticket_da = DataAccess(Ticket)
    #     if ticket_da.find_by_id(id):
    #         return ticket_da.remove(id)
    #     else:
    #         raise TicketNotFoundError()

    # @staticmethod
    # def find_by_title(title):
    #     ticket_da = DataAccess(Ticket)
    #     return ticket_da.find_by(Ticket._title == title)
    #
    # @staticmethod
    # def find_by_text_content(text_content):
    #     ticket_da = DataAccess(Ticket)
    #     return ticket_da.check_word_in_text(text_content)
    #
    # @staticmethod
    # def date_range(start_date, end_date):
    #     ticket_da = DataAccess(Ticket)
    #     return ticket_da.find_by_date_range(start_date, end_date)