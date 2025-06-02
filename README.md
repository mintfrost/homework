# homework

This repository contains a simple CLI budget book written in Python.

## Requirements

- Python 3

## Usage

Add an entry (expense or income):

```bash
python3 budget.py add "description" expense 12.50
python3 budget.py add "salary" income 1000
```

List all entries:

```bash
python3 budget.py list
```

Show current balance (income - expenses):

```bash
python3 budget.py balance
```

All entries are stored in a `budget.csv` file in the same directory.
