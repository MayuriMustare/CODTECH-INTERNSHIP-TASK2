from datetime import datetime
from typing import Optional, Dict, Any

class LibraryItem:
    def __init__(
        self,
        id: str,
        title: str,
        creator: str,
        category: str,
        year: int,
        type: str
    ):
        self.id = id
        self.title = title
        self.creator = creator  # author or director
        self.category = category
        self.year = year
        self.type = type  # book, magazine, or DVD
        self.checked_out = False
        self.borrower = None
        self.checkout_date = None
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'creator': self.creator,
            'category': self.category,
            'year': self.year,
            'type': self.type,
            'checked_out': self.checked_out,
            'borrower': self.borrower,
            'checkout_date': self.checkout_date.isoformat() if self.checkout_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LibraryItem':
        item = cls(
            data['id'],
            data['title'],
            data['creator'],
            data['category'],
            data['year'],
            data['type']
        )
        item.checked_out = data['checked_out']
        item.borrower = data['borrower']
        item.checkout_date = datetime.fromisoformat(data['checkout_date']) if data['checkout_date'] else None
        return item