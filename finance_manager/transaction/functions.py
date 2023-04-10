from transaction.model import Transaction
from datetime import datetime
import re

transactions_list = Transaction.all_transactions()


def display_all_transaction() -> str:
    for obj in transactions_list:
        print(
            f'date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')


def filter_category(catg: str) -> str:
    for obj in filter(lambda x: x.category == catg, transactions_list):
        print(
            f'date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')


def filter_date(start, end):
    try:
        # converted to datetime object
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        print('Invalid date format')

    for obj in filter(lambda x: start_date < x.date < end_date, transactions_list):
        print(
            f'date: {obj.date}, category: {obj.category}, amount: {obj.amount}, description: {obj.description}')
