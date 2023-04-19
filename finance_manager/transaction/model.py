from datetime import datetime
from file_handler import Pickle_db
import re


class Transaction:

    transactions_db = Pickle_db("transactions_pickle.db")
    # transactions_list = []

    def __init__(self, action_type, date, amount, category, description=''):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.action_type = action_type
        # self.transactions_list.append(self)
        self.transactions_db.add_data(self)

    @property
    def date(self):
        #dont show time
        return self._date.date()

    @date.setter
    def date(self, value):
        try:
            # I can use datetime object to compare two date
            self._date = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not re.match(r'^[0-9]+$', value):
            raise ValueError("Invalid amount")
        self._amount = int(value)

    @classmethod
    def all_transactions(cls):
        # load_data methode load all data as a list
        return cls.transactions_db.load_data()


# Transaction('action_type', '2020-04-24', '150', 'category')