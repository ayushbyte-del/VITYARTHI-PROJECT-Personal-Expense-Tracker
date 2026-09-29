# Project Statement & Scope

## Problem Statement

Most people struggle to keep track of where their money goes every month. Small, frequent cash or digital expenses often go unrecorded, leading to unexpected budget shortages at the end of the month. While complex apps and spreadsheets exist, they are often tedious to set up and use daily. There is a need for a straightforward, lightweight tool where users can quickly enter transactions, stay aware of their monthly limits, and review basic spending statistics.

## Scope of the Project

This project covers the fundamental requirements for personal expense management:

* **Transaction Handling:** Ability to add, edit, list, and delete expenses during an active terminal session.
* **Categorization:** Classifying costs under pre-defined heads like food, travel, shopping, bills, health, fun, and other.
* **Basic Analytics:** Calculating key statistics like total expenditure, median, average expense, and highlighting top expenses.
* **Budget Tracking:** Comparing total spending against a custom monthly budget limit.
* **Input Protection:** Handling user typing errors gracefully without crashing the application.

*Out of Scope:* Persistent database storage across application restarts and GUI interfaces (reserved for future updates).

## Target Users

1. **College Students:** Who need a quick way to manage pocket money and monthly allowances.
2. **Beginners in Budgeting:** Anyone looking for a simple tool to monitor daily spending habits.
3. **Command Line Users:** People who prefer simple, distraction-free terminal applications over heavy mobile apps.

## Key Features

| ID | Feature Name | Description |
| --- | --- | --- |
| **F-01** | Expense Operations | Add, update, view, and delete expense entries with auto IDs. |
| **F-02** | Receipt Code Generation | Creates short unique code identifiers for transactions. |
| **F-03** | Spending Analytics | Computes total spending, average, median, and highest expenses. |
| **F-04** | Category Breakdown | Summarizes total spending per category. |
| **F-05** | Budget Checker | Warns if spending exceeds the user-defined budget. |
| **F-06** | Input Validation | Prevents wrong inputs (text in amount fields, bad numbers, etc.). |