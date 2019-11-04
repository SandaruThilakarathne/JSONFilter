"""
Working as connector, Making connection between Data showing showing and Filtering functions.

"""

from Handlers.QueryFilter import get_user, get_organization, get_tickets, get_searchable_keys


class Hub:
    # connecting user data searching function
    @classmethod
    def find_user(self, keyword, value):
        return get_user(keyword, value)

    # connecting organization searching function
    @classmethod
    def find_organization(self, keyword, value):
        return get_organization(keyword, value)

    # connecting ticket data searching function
    @classmethod
    def find_ticket(self, keyword, value):
        return get_tickets(keyword, value)

    @classmethod
    def get_keys(self):
        return get_searchable_keys()

