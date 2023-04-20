# Personal Finance Manager Application

This is a Python-based personal finance manager application that helps users monitor their income and expenses. The application allows users to add income and expense transactions, view transactions within a specific date range or category, generate insightful reports on financial activities and provides a user-friendly command-line interface.

## Features

- Transaction Management: Allow users to add income and expense transactions. Each transaction should include the date, amount, category, and description. Validate and store transaction dates accurately using date & time operations.
- Viewing and Filtering Transactions: Display a comprehensive list of all transactions. Filter transactions based on a specific date range or category.   Utilize functional programming techniques such as lambdas, map, and filter for these tasks.
- Summary Reports: Generate a report showing the total income, total expenses, and the balance for a given date range. Display the total amount spent in each category within the specified date range.
- Data Storage and File Handling: Store transaction data using either the pickle or shelve module. Handle exceptions that may arise during the reading or writing process.
- Object-Oriented Programming: Implement the application using OOP concepts. Design classes and methods for managing transactions and generating reports.
- Command-line Interface: Create a user-friendly command-line interface using argparse. Enable users to add, view, and filter transactions, as well as generate reports through command-line arguments.

## Example Inputs and Outputs

Adding a transaction:

```python
>>> python finance_manager.py add --type income --date 2023-04-07 --amount 500.00 --category salary --description "April Salary"
Output:
Transaction added successfully

