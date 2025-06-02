import csv
import os
from datetime import datetime

FILE = 'budget.csv'

FIELDS = ['date', 'description', 'type', 'amount']


def init_file():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def add_entry(description, entry_type, amount, date=None):
    init_file()
    date = date or datetime.now().strftime('%Y-%m-%d')
    with open(FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            'date': date,
            'description': description,
            'type': entry_type,
            'amount': amount,
        })


def list_entries():
    init_file()
    with open(FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def total_balance():
    income = 0
    expense = 0
    for row in list_entries():
        amount = float(row['amount'])
        if row['type'] == 'income':
            income += amount
        else:
            expense += amount
    return income - expense


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Simple Budget Book')
    subparsers = parser.add_subparsers(dest='command')

    add_p = subparsers.add_parser('add', help='Add a new entry')
    add_p.add_argument('description')
    add_p.add_argument('type', choices=['income', 'expense'])
    add_p.add_argument('amount', type=float)
    add_p.add_argument('--date', help='YYYY-MM-DD')

    subparsers.add_parser('list', help='List all entries')
    subparsers.add_parser('balance', help='Show current balance')

    args = parser.parse_args()
    if args.command == 'add':
        add_entry(args.description, args.type, args.amount, args.date)
    elif args.command == 'list':
        for row in list_entries():
            print(f"{row['date']}\t{row['description']}\t{row['type']}\t{row['amount']}")
    elif args.command == 'balance':
        print(total_balance())
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
