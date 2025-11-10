import json
import os
from datetime import datetime

class ReminderManager:
    def __init__(self):
        self.file_path = 'data/reminders.json'
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """Create data file if it doesn't exist"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def _read_reminders(self):
        """Read reminders from JSON file"""
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    def _write_reminders(self, reminders):
        """Write reminders to JSON file"""
        with open(self.file_path, 'w') as f:
            json.dump(reminders, f, indent=2)
    
    def create_reminder(self, title, reminder_time=None, description=None):
        """Create a new reminder"""
        reminders = self._read_reminders()
        
        reminder = {
            'id': len(reminders) + 1,
            'title': title,
            'description': description,
            'reminder_time': reminder_time or "soon",
            'created_at': datetime.now().isoformat()
        }
        
        reminders.append(reminder)
        self._write_reminders(reminders)
        return reminder
    
    def get_all_reminders(self):
        """Get all reminders"""
        return self._read_reminders()
    
    def format_reminders_response(self, reminders):
        """Format reminders list into natural language response"""
        if not reminders:
            return "You have no reminders."
        
        response = "Here are your reminders:\n"
        for i, reminder in enumerate(reminders, 1):
            response += f"{i}. {reminder['title']}"
            if reminder.get('description'):
                response += f" - {reminder['description']}"
            response += f" (set for {reminder['reminder_time']})\n"
        
        return response