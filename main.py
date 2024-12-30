import argparse
from datetime import datetime
from models.item import LibraryItem
from services.library_service import LibraryService

def setup_argparse():
    parser = argparse.ArgumentParser(description='Library Resource Management System')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add item
    add_parser = subparsers.add_parser('add', help='Add a new item')
    add_parser.add_argument('--id', required=True, help='Unique ID')
    add_parser.add_argument('--title', required=True, help='Item title')
    add_parser.add_argument('--creator', required=True, help='Author/Director')
    add_parser.add_argument('--category', required=True, help='Category')
    add_parser.add_argument('--year', required=True, type=int, help='Publication year')
    add_parser.add_argument('--type', required=True, choices=['book', 'magazine', 'dvd'], help='Item type')
    
    # Checkout
    checkout_parser = subparsers.add_parser('checkout', help='Checkout an item')
    checkout_parser.add_argument('--id', required=True, help='Item ID')
    checkout_parser.add_argument('--borrower', required=True, help='Borrower name')
    
    # Return
    return_parser = subparsers.add_parser('return', help='Return an item')
    return_parser.add_argument('--id', required=True, help='Item ID')
    
    # Search
    search_parser = subparsers.add_parser('search', help='Search for items')
    search_parser.add_argument('--query', required=True, help='Search query')
    
    # List
    subparsers.add_parser('list', help='List all items')
    
    # Fines
    subparsers.add_parser('fines', help='Display all fines')
    
    return parser

def main():
    parser = setup_argparse()
    args = parser.parse_args()
    library = LibraryService()
    
    try:
        if args.command == 'add':
            item = LibraryItem(
                args.id,
                args.title,
                args.creator,
                args.category,
                args.year,
                args.type
            )
            if library.add_item(item):
                print(f"Added {args.type}: {args.title}")
            else:
                print(f"Error: Item with ID {args.id} already exists")
                
        elif args.command == 'checkout':
            if library.checkout_item(args.id, args.borrower):
                print(f"Checked out item {args.id} to {args.borrower}")
            else:
                print(f"Error: Unable to checkout item {args.id}")
                
        elif args.command == 'return':
            fine = library.return_item(args.id)
            print(f"Returned item {args.id}")
            if fine > 0:
                print(f"Late fee: ${fine:.2f}")
                
        elif args.command == 'search':
            results = library.search_items(args.query)
            if results:
                print("\nSearch results:")
                for item in results:
                    status = "Checked out" if item.checked_out else "Available"
                    print(f"- {item.title} ({item.type}) by {item.creator} - {status}")
            else:
                print("No items found")
                
        elif args.command == 'list':
            items = library.list_items()
            print("\nAvailable items:")
            for item in items['Available']:
                print(f"- {item.title} ({item.type}) by {item.creator}")
            print("\nChecked out items:")
            for item in items['Checked Out']:
                print(f"- {item.title} ({item.type}) by {item.creator} - Borrowed by: {item.borrower}")
                
        elif args.command == 'fines':
            fines = library.get_fines()
            if fines:
                print("\nOverdue fines:")
                for item_id, amount in fines.items():
                    print(f"Item {item_id}: ${amount:.2f}")
            else:
                print("No outstanding fines")
                
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()