from transaction.model import Transaction
from datetime import datetime
import re

# Transaction.all_transactions() = Transaction.all_transactions()


def report_date(start: str, end: str) -> None:
    total_income, total_expence = 0, 0
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        print('Invalid date format')

    for obj in filter(lambda x: start_date < x.date < end_date, Transaction.all_transactions()):
        total_income += obj.amount if obj.action_type == 'income' else total_expence + obj.amount
    print(
        f'total_income: {total_income} , totlal_expence: {total_expence}, balance: {total_income-total_expence}')


def display_all_transaction() -> None:
    for obj in Transaction.all_transactions():
        print(
            f'type: {obj.action_type}, date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')


def filter_category(catg: str) -> None:
    for obj in filter(lambda x: x.category == catg, Transaction.all_transactions()):
        print(
            f'type: {obj.action_type}, date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')


def filter_date(start: str, end: str) -> None:
    try:
        # converted to datetime object
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        print('Invalid date format')

    for obj in filter(lambda x: start_date < x.date < end_date, Transaction.all_transactions()):
        print(
            f'type: {obj.action_type}, date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')


def add_transaction(action_type: str, date: str, amount: str, category: str, description: str) -> None:
    Transaction(action_type, date, amount, category, description)
    print('Transaction added successfully')
