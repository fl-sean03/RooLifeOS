# Module F: Financial Plan Instructions

This document provides instructions for interacting with `Financial_Plan.xlsx` within Module F.

## Interacting with `Financial_Plan.xlsx`
Since Roo cannot directly edit Excel files, modifications to `Financial_Plan.xlsx` will be handled by providing Python code snippets. These snippets will use the `pandas` library to read, modify, and write the Excel file.

## Initial Setup
- The `Financial_Plan.xlsx` file should be created as an empty Excel file with two sheets: "Income\_Expenses" and "Investments".

## Example: Logging an Expense
When asked to log an expense, provide a Python snippet similar to this:

```python
import pandas as pd

# Load the Excel file
file_path = 'Module_F_Personal_Resource_Optimization/Financial_Plan.xlsx'
df_expenses = pd.read_excel(file_path, sheet_name='Income_Expenses')

# Add a new expense row
new_expense = ['2025-06-01', 'Coffee', 4.50, 'Daily']
df_expenses.loc[len(df_expenses)] = new_expense

# Save the updated DataFrame back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_expenses.to_excel(writer, sheet_name='Income_Expenses', index=False)
```

## Example: Updating an Investment Record
When asked to update an investment record, provide a Python snippet similar to this:

```python
import pandas as pd

# Load the Excel file
file_path = 'Module_F_Personal_Resource_Optimization/Financial_Plan.xlsx'
df_investments = pd.read_excel(file_path, sheet_name='Investments')

# Example: Update an existing investment (e.g., change amount for 'Stock A')
# Assuming 'Investment_Name' is a column in your Investments sheet
df_investments.loc[df_investments['Investment_Name'] == 'Stock A', 'Amount'] = 1500.00

# Save the updated DataFrame back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_investments.to_excel(writer, sheet_name='Investments', index=False)
```

## Git Commands
After providing the Python snippet, always include the `git add` and `git commit` commands for the Excel file:

```bash
git add Module_F_Personal_Resource_Optimization/Financial_Plan.xlsx
git commit -m "Module F: Update Financial_Plan.xlsx"