from transaction.model import Transaction
from exceptions import *
from datetime import datetime
import re


def filter_transactions_by_date(start: str, end: str):
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
    except InvalidDateFormat as err:
        print(err)
        return []

    return filter(lambda x: start_date < x.date < end_date, Transaction.all_transactions())


def report_date(start: str, end: str) -> None:
    totals = {'income': 0, 'expense': 0}
    for obj in filter_transactions_by_date(start, end):
        totals[obj.action_type] += obj.amount

    print(f'total_income: {totals["income"]}, total_expense: {totals["expense"]}')


def filter_date(start: str, end: str) -> None:
    for obj in filter_transactions_by_date(start, end):
        print(obj)


def display_all_transaction() -> None:
    for obj in Transaction.all_transactions():
        print(obj)


def filter_category(catg: str) -> None:
    for obj in filter(lambda x: x.category == catg, Transaction.all_transactions()):
        print(obj)


def add_transaction(action_type: str, date: str, amount: str, category: str, description: str) -> None:
    Transaction(action_type, date, amount, category, description)
    print('Transaction added successfully')
