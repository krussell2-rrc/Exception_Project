"""
Description: A program that reads through transaction records and reports the results.
Author: ACE Faculty
Edited by: Kareem Russell
Date:October 13, 2023
Usage: This program will read transaction data from a .csv file, summarize and 
report the results.
"""
import csv
import os

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
valid_record = True 
error_message = ''

os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Reset valid record and error message for each iteration
            valid_record = True
            error_message = ''

            # Extract the customer ID from the first column
            customer_id = row[0]

            # Extract the transaction type from the second column
            transaction_type = row[1]

            # Extract the transaction amount from the third column
            transaction_amount = row[2]
        ### VALIDATION 1 ###
            if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message = "Invalid transaction type"
        ### VALIDATION 2 ###
            try:
                transaction_amount = float(row[2])
            except ValueError:
                valid_record = False
                error_message = "This is a non-numeric amount"

            if valid_record:
                transaction_amount = float(transaction_amount)
            # Initialize the customer's account balance if it doesn't already exist
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}
            # Update the customer's account balance based on the transaction type
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount
            # Record  transactions in the customer's transaction history
                customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
                transaction_count += 1
                total_transaction_amount += transaction_amount
            ### COLLECT INVALID RECORDS ###
            else:
                invalid_record = (row, error_message)
                rejected_records.append(invalid_record)

except FileNotFoundError as file_not_found:
    print(f"ERROR: {file_not_found}")
except Exception as e:
    print(f"ERROR: {e}")

print("PiXELL River Transaction Report\n===============================\n")

# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']
    print(f"\nCustomer {customer_id} has a balance of ${balance:.2f}.")
    print("Transaction History:")
    for amount, transaction_type in data['transactions']:
        print(f"{transaction_type.capitalize()}: ${amount:.2f}")
# Print the average transaction amount
if transaction_count > 0:
    average_transaction_amount = total_transaction_amount / transaction_count
    print(f"AVERAGE TRANSACTION AMOUNT: ${average_transaction_amount:.2f}")
else:
    print("AVERAGE TRANSACTION AMOUNT: No transactions available")
# Print rejected records
print("\nREJECTED RECORDS\n================")
for record in rejected_records:
    print("REJECTED:", record)


