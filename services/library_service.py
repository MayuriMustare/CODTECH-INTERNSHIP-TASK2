from datetime import datetime, timedelta
from typing import List, Optional
from models.item import LibraryItem
from storage.json_storage import JsonStorage

class LibraryService:
    FINE_RATE = 0.50  # $0.50 per day
    
    def __init__(self):
        self.storage = JsonStorage()
    
    def add_item(self, item: LibraryItem) -> bool:
        data = self.storage.load_data()
        if any(i['id'] == item.id for i in data['items']):
            return False
        data['items'].append(item.to_dict())
        self.storage.save_data(data)
        return True
    
    def get_item(self, item_id: str) -> Optional[LibraryItem]:
        data = self.storage.load_data()
        item_data = next((i for i in data['items'] if i['id'] == item_id), None)
        return LibraryItem.from_dict(item_data) if item_data else None
    
    def checkout_item(self, item_id: str, borrower: str) -> bool:
        item = self.get_item(item_id)
        if not item or item.checked_out:
            return False
            
        data = self.storage.load_data()
        for i in data['items']:
            if i['id'] == item_id:
                i['checked_out'] = True
                i['borrower'] = borrower
                i['checkout_date'] = datetime.now().isoformat()
                break
                
        self.storage.save_data(data)
        return True
    
    def return_item(self, item_id: str) -> float:
        item = self.get_item(item_id)
        if not item or not item.checked_out:
            return 0.0
            
        days_late = self._calculate_days_late(item.checkout_date)
        fine = max(0, days_late * self.FINE_RATE)
        
        data = self.storage.load_data()
        for i in data['items']:
            if i['id'] == item_id:
                i['checked_out'] = False
                i['borrower'] = None
                i['checkout_date'] = None
                break
                
        if fine > 0:
            data['fines'] = data.get('fines', {})
            data['fines'][item_id] = data['fines'].get(item_id, 0) + fine
            
        self.storage.save_data(data)
        return fine
    
    def search_items(self, query: str) -> List[LibraryItem]:
        data = self.storage.load_data()
        query = query.lower()
        results = []
        
        for item_data in data['items']:
            if (query in item_data['title'].lower() or
                query in item_data['creator'].lower() or
                query in item_data['category'].lower()):
                results.append(LibraryItem.from_dict(item_data))
                
        return results
    
    def list_items(self) -> dict:
        data = self.storage.load_data()
        categorized = {'Available': [], 'Checked Out': []}
        
        for item_data in data['items']:
            item = LibraryItem.from_dict(item_data)
            key = 'Checked Out' if item.checked_out else 'Available'
            categorized[key].append(item)
            
        return categorized
    
    def get_fines(self) -> dict:
        data = self.storage.load_data()
        return data.get('fines', {})
    
    def _calculate_days_late(self, checkout_date: datetime) -> int:
        if not checkout_date:
            return 0
        due_date = checkout_date + timedelta(days=1)  # 2-week checkout period
        days_late = (datetime.now() - due_date).days
        return max(0, days_late)