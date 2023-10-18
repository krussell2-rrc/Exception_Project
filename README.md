# Project Name
Exception Project

## Description
In this program, troubleshooting and exception handling will be used to ensure all programs are correct and accurate and overall improve the quality of the PiXELL Transaction Report.

## Author
Kareem Russell

## Assignment
Assignment 4: Troubleshooting and Exception Handling

## Code Modification:
Added try-except block to handle exceptions if the input file cannot be located and any other general exceptions. 

## Code Modification:
Added an else statement to "if_valid record:" statement at line 66 to collect and print invalid records

## Code Modification:
Added if statement under ### VALIDATION 1 ### to return an error message if the transaction_type is not in the list valid_transaction_types

## Code Modification:
Added try-except block under ### VALIDATION 2 ### to try to convert the transaction amount to a float and to print an error message if it fails to.

## Code Modification:
Changed "withdrawal" at line 58 to "withdraw" because it was an invalid transaction type.

## Code Modification:
Changed if statement at line 56 to update customer's account balance by either adding or subtracting the transaction amount based on the transaction type.

## Code Modification: 
Added if-else at line 85 block to calculate the average transaction amount of transactions in the bank_data.csv file.

## Code Modification:
Added code to line 61 to keep count of transactions to be able to calculate the average transaction amount.

## Code Modification:
Modified code to print transaction history at line 81

## Code Modification: 
Added "$:2.f" to variables with currency values.





