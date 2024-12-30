import json
from typing import List, Dict, Any
from pathlib import Path

class JsonStorage:
    def __init__(self, file_path: str = 'library_data.json'):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not Path(self.file_path).exists():
            self.save_data({'items': [], 'fines': {}})
    
    def load_data(self) -> Dict[str, Any]:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {'items': [], 'fines': {}}
    
    def save_data(self, data: Dict[str, Any]):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)