from core.file_handler import *
from datetime import datetime
import re


class Transaction:

    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    @property
    def date(self):
        return self._date

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
        self._amount = value
