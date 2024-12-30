# CODTECH-INTERNSHIP-TASK2
Name: MAYURI MUSTARE

Company: CODTECH IT SOLUTION

ID: CT08EYS

Domain: Python Programming Intern

Duration: December 2024 to January 2025 

Mentor: SRAVANI GOUNI

# Overview of the Project:

# Project: Library Management System

# A] objective:
   The code implements a Library Resource Management System that provides a command-line interface (CLI) to manage library resources. It allows users to perform operations like adding, checking out, returning items, searching for items, listing all items, and displaying overdue fines. This system is designed to streamline library management and track items and borrowers efficiently.

# B] Key Activities:

1. Setup Argument Parsing:
The setup_argparse function defines CLI commands and their respective arguments.
Subcommands include add, checkout, return, search, list, and fines.

2. Adding Items:
Users can add a new library item (book, magazine, or DVD) with attributes like ID, title, creator, category, publication year, and type.

3. Checking Out Items:
Allows a borrower to check out a library item using its unique ID and borrower's name.

4. Returning Items:
Facilitates returning an item. If overdue, it calculates and displays the fine.

5. Searching Items:
Users can search for library items using a query. Results include item details and their availability status.

6. Listing Items:
Lists all library items, categorizing them as "Available" or "Checked Out."

7. Displaying Fines:
Shows all outstanding fines for overdue items.

8. Error Handling:
Ensures graceful handling of errors, such as duplicate IDs, invalid operations, or missing items.

# C] Technologies Used:

1. Python Standard Library:
argparse: For parsing command-line arguments and subcommands.
datetime: (Presumably used in other modules like LibraryService) to manage date and time operations, such as calculating overdue fines.

2. Custom Modules:
models.item: Defines the LibraryItem class, which represents a library resource.
services.library_service: Implements the LibraryService class, handling core library operations like adding items, checking out, returning, and fine calculations.

3. Object-Oriented Programming (OOP):
Encapsulation of library items and operations in classes (LibraryItem and LibraryService).

4. Command-Line Interface (CLI):
Provides a user-friendly interface for managing library resources via commands.

5. How It Works:
The main function initializes the CLI parser and processes user commands.
Based on the command, the appropriate operation is executed using the LibraryService class.
Outputs are printed to the console, indicating the success or failure of operations.

# D] Commands to Check Output:

# Add a new book
python main.py add --id "B001" --title "The Great Gatsby" --creator "F. Scott Fitzgerald" --category "Fiction" --year 1925 --type book

# Check out an item
python main.py checkout --id "B001" --borrower "John Doe"

# Search for items
python main.py search --query "Gatsby"

# List all items
python main.py list

# Return an item
python main.py return --id "B001"

# View fines
python main.py fines
