# CODTECH-INTERNSHIP-TASK2
Name: MAYURI MUSTARE
Company: CODTECH IT SOLUTION
ID: CT08EYS
Domain: Python Programming Intern
Duration: December 2024 to January 2025 
Mentor: SRAVANI GOUNI

Objective
The code implements a Library Resource Management System that provides a command-line interface (CLI) to manage library resources. It allows users to perform operations like adding, checking out, returning items, searching for items, listing all items, and displaying overdue fines. This system is designed to streamline library management and track items and borrowers efficiently.

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
