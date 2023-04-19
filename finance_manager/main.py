import argparse
from transaction import model
from transaction.functions import display_all_transaction, filter_category, filter_date, add_transaction


parser = argparse.ArgumentParser(prog='Finance Manager',
                                 description='Manage your transactions')

parser.add_argument('action', choices=['view', 'add', 'report'],
                    help='The action that available.')
# ==================== add gruop ===========================
group_add = parser.add_argument_group('add', 'Add a transaction.')
group_add.add_argument('--type', choices=['expense', 'income'], required=False)
group_add.add_argument('--date', required=False,
                       help='format must be like :YYYY-mm-dd .')
group_add.add_argument('--amount', required=False)
group_add.add_argument(
    '--category', choices=['salary', 'groceries', 'fee'], required=False)
group_add.add_argument(
    '--description', help='description of your transaction.', default='')
# ==================== view gruop ===========================
group_view = parser.add_argument_group('view', 'View transactions.')
group_view.add_argument('--start-date',  required=False)
group_view.add_argument('--end-date',  required=False)
# ==================== view gruop ===========================
group_report = parser.add_argument_group('report', 'report transactions.')
args = parser.parse_args()

if args.action == 'add':
    if not all([args.type, args.date, args.amount, args.category]):
        parser.error(
            'the following arguments are required: --type, --date, --amount, --category')
    else:
        add_transaction(args.type, args.date,
                        args.amount, args.category, args.description)


if args.action == 'view':
    if args.start_date and args.end_date:
        filter_date(args.start_date, args.end_date)
    elif args.category:
        filter_category(args.category)
    else:
        display_all_transaction()
