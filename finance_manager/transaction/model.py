from datetime import datetime
from file_handler import Pickle_db
from exceptions import *
import re


class Transaction:

    transactions_db = Pickle_db("transactions_pickle.db")

    def __init__(self, action_type, date, amount, category, description='Not necessary'):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.action_type = action_type
        self.transactions_db.add_data(self)

    def __str__(self):
        return "action: {0}, date: {1}, amount: {2}, category: {3}, description: {4}".\
            format(self.action_type, self.date, self.amount,
                   self.category, self.description)

    @property
    def date(self):
        # dont show time
        return self._date.date()

    @date.setter
    def date(self, value):
        try:
            # I can use datetime object to compare two date
            self._date = datetime.strptime(value, "%Y-%m-%d")
        except InvalidDateFormat as err:
            print(err)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not re.match(r'^[0-9]+$', value):
            raise InvalidAmount
        self._amount = int(value)

    @classmethod
    def all_transactions(cls):
        try:
            # load_data methode load all data as a list
            return cls.transactions_db.load_data()
        except FileLoadingError as err:
            print(f"Error loading data: {e}")
            return []

