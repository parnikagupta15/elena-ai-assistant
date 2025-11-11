import json
import os
import random
from datetime import datetime, timedelta

class EnhancedAIAssistant:
    def __init__(self):
        self.qa_database = {
            # Geography
            "capital of france": "Paris",
            "capital of germany": "Berlin", 
            "capital of italy": "Rome",
            "capital of india": "New Delhi",
            "capital of japan": "Tokyo",
            "capital of usa": "Washington D.C.",
            "capital of uk": "London",
            "capital of china": "Beijing",
            "capital of russia": "Moscow",
            "capital of brazil": "Brasília",
            
            # Science
            "height of mount everest": "8,849 meters (29,032 feet)",
            "speed of light": "299,792,458 meters per second",
            "largest planet": "Jupiter",
            "closest planet to sun": "Mercury",
            "chemical symbol for gold": "Au",
            "chemical symbol for water": "H2O",
            "human body temperature": "37°C or 98.6°F",
            
            # History
            "inventor of telephone": "Alexander Graham Bell",
            "inventor of light bulb": "Thomas Edison",
            "inventor of computer": "Charles Babbage",
            "first man on moon": "Neil Armstrong",
            "founder of microsoft": "Bill Gates",
            "founder of apple": "Steve Jobs",
            
            # General Knowledge
            "current year": "2024",
            "colors in rainbow": "Red, Orange, Yellow, Green, Blue, Indigo, Violet",
            "largest ocean": "Pacific Ocean",
            "longest river": "Nile River",
            "largest animal": "Blue Whale",
            "fastest land animal": "Cheetah"
        }
        
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why couldn't the bicycle stand up by itself? It was two tired!"
        ]
        
        self.weather_data = {
            "mumbai": {"temp": 32, "condition": "Humid", "humidity": 75},
            "delhi": {"temp": 30, "condition": "Smoggy", "humidity": 60},
            "bangalore": {"temp": 26, "condition": "Pleasant", "humidity": 65},
            "hyderabad": {"temp": 28, "condition": "Warm", "humidity": 55},
            "ahmedabad": {"temp": 31, "condition": "Hot", "humidity": 50},
            "chennai": {"temp": 34, "condition": "Hot", "humidity": 70},
            "kolkata": {"temp": 31, "condition": "Humid", "humidity": 75},
            "surat": {"temp": 30, "condition": "Warm", "humidity": 65},
            "pune": {"temp": 27, "condition": "Pleasant", "humidity": 60},
            "jaipur": {"temp": 29, "condition": "Dry", "humidity": 45},
            "kanpur": {"temp": 28, "condition": "Clear", "humidity": 55},
            "lucknow": {"temp": 29, "condition": "Warm", "humidity": 60},
            "nagpur": {"temp": 32, "condition": "Hot", "humidity": 50},
            "indore": {"temp": 28, "condition": "Clear", "humidity": 55},
            "patna": {"temp": 30, "condition": "Humid", "humidity": 65},
            "london": {"temp": 15, "condition": "Cloudy", "humidity": 80},
            "new york": {"temp": 22, "condition": "Sunny", "humidity": 65},
            "tokyo": {"temp": 25, "condition": "Partly Cloudy", "humidity": 70},
            "dubai": {"temp": 35, "condition": "Hot", "humidity": 40}
        }
        
        # Initialize files
        self.reminders_file = 'reminders.json'
        self.notes_file = 'notes.json'
        self._init_files()
    
    def _init_files(self):
        """Initialize data files"""
        for file in [self.reminders_file, self.notes_file]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    json.dump([], f)
    
    def _read_json(self, filename):
        """Read JSON file"""
        with open(filename, 'r') as f:
            return json.load(f)
    
    def _write_json(self, filename, data):
        """Write JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def process_command(self, text):
        """Process user command and return response"""
        text_lower = text.lower()
        
        if 'weather' in text_lower:
            return self._handle_weather(text_lower) 
        # Greeting
        if any(word in text_lower for word in ['hello', 'hi', 'hey']):
            return self._handle_greeting()
        
        # Goodbye
        elif any(word in text_lower for word in ['bye', 'goodbye', 'exit', 'quit']):
            return "Goodbye! Have a great day! 👋"
        
        # Time
        elif any(word in text_lower for word in ['time', 'current time']):
            return self._handle_time()
        
        # Date
        elif any(word in text_lower for word in ['date', 'today', 'today\'s date']):
            return self._handle_date()
        
        # Jokes
        elif any(word in text_lower for word in ['joke', 'funny', 'make me laugh']):
            return self._tell_joke()
        
        # Reminders
        elif any(word in text_lower for word in ['remind', 'reminder']):
            return self._handle_reminder(text)
        
        # Notes
        elif any(word in text_lower for word in ['note', 'remember that']):
            return self._handle_note(text)
        
        # Show reminders
        elif 'show reminders' in text_lower:
            return self._show_reminders()
        
        # Show notes
        elif 'show notes' in text_lower:
            return self._show_notes()
        
        # Calculator
        elif any(word in text_lower for word in ['calculate', 'what is']):
            return self._handle_calculation(text)
        
        # Questions
        else:
            return self._answer_question(text)
    
    def _handle_greeting(self):
        """Return time-appropriate greeting"""
        hour = datetime.now().hour
        if hour < 12:
            return "Good morning! ☀️ How can I help you today?"
        elif hour < 18:
            return "Good afternoon! 🌤️ How can I assist you?"
        else:
            return "Good evening! 🌙 What can I do for you?"
    
    def _handle_time(self):
        """Return current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"🕒 The current time is {current_time}"
    
    def _handle_date(self):
        """Return current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {current_date}"
    
    def _handle_weather(self, text):
        text_lower = text.lower()
        cities = {
            "mumbai": "🌤️ **Weather in Mumbai:**\n• Temperature: 32°C (feels like 34°C)\n• Conditions: Humid and warm\n• Humidity: 75%\n• Wind: 12 km/h SW\n• High/Low: 34°C / 28°C",
            "delhi": "🌤️ **Weather in Delhi:**\n• Temperature: 30°C (feels like 32°C)\n• Conditions: Partly cloudy\n• Humidity: 60%\n• Wind: 10 km/h NW\n• High/Low: 33°C / 26°C",
            "bangalore": "🌤️ **Weather in Bangalore:**\n• Temperature: 26°C (feels like 28°C)\n• Conditions: Pleasant and clear\n• Humidity: 65%\n• Wind: 8 km/h NE\n• High/Low: 29°C / 22°C",
            "chennai": "🌤️ **Weather in Chennai:**\n• Temperature: 34°C (feels like 36°C)\n• Conditions: Hot and sunny\n• Humidity: 70%\n• Wind: 14 km/h SE\n• High/Low: 36°C / 28°C",
            "kolkata": "🌤️ **Weather in Kolkata:**\n• Temperature: 31°C (feels like 33°C)\n• Conditions: Humid\n• Humidity: 75%\n• Wind: 11 km/h S\n• High/Low: 33°C / 27°C",
            "hyderabad": "🌤️ **Weather in Hyderabad:**\n• Temperature: 28°C (feels like 30°C)\n• Conditions: Warm and clear\n• Humidity: 55%\n• Wind: 9 km/h W\n• High/Low: 32°C / 24°C",
            "ahmedabad": "🌤️ **Weather in Ahmedabad:**\n• Temperature: 31°C (feels like 33°C)\n• Conditions: Hot and dry\n• Humidity: 50%\n• Wind: 13 km/h NW\n• High/Low: 34°C / 26°C",
            "pune": "🌤️ **Weather in Pune:**\n• Temperature: 27°C (feels like 29°C)\n• Conditions: Pleasant\n• Humidity: 60%\n• Wind: 7 km/h NE\n• High/Low: 30°C / 22°C",
            "jaipur": "🌤️ **Weather in Jaipur:**\n• Temperature: 29°C (feels like 31°C)\n• Conditions: Dry and clear\n• Humidity: 45%\n• Wind: 12 km/h NW\n• High/Low: 32°C / 25°C",
            "kanpur": "🌤️ **Weather in Kanpur:**\n• Temperature: 28°C (feels like 30°C)\n• Conditions: Clear sky\n• Humidity: 55%\n• Wind: 10 km/h NW\n• High/Low: 32°C / 24°C",
            "lucknow": "🌤️ **Weather in Lucknow:**\n• Temperature: 29°C (feels like 31°C)\n• Conditions: Warm\n• Humidity: 60%\n• Wind: 9 km/h N\n• High/Low: 32°C / 25°C",
            "nagpur": "🌤️ **Weather in Nagpur:**\n• Temperature: 32°C (feels like 34°C)\n• Conditions: Hot\n• Humidity: 50%\n• Wind: 11 km/h W\n• High/Low: 35°C / 27°C",
            "indore": "🌤️ **Weather in Indore:**\n• Temperature: 28°C (feels like 30°C)\n• Conditions: Clear\n• Humidity: 55%\n• Wind: 8 km/h NE\n• High/Low: 31°C / 23°C",
            "patna": "🌤️ **Weather in Patna:**\n• Temperature: 30°C (feels like 32°C)\n• Conditions: Humid\n• Humidity: 65%\n• Wind: 10 km/h E\n• High/Low: 33°C / 26°C",
            "london": "🌤️ **Weather in London:**\n• Temperature: 15°C (feels like 13°C)\n• Conditions: Cloudy\n• Humidity: 80%\n• Wind: 15 km/h W\n• High/Low: 17°C / 12°C",
            "new york": "🌤️ **Weather in New York:**\n• Temperature: 22°C (feels like 20°C)\n• Conditions: Sunny\n• Humidity: 65%\n• Wind: 12 km/h NE\n• High/Low: 24°C / 18°C",
            "tokyo": "🌤️ **Weather in Tokyo:**\n• Temperature: 25°C (feels like 27°C)\n• Conditions: Partly cloudy\n• Humidity: 70%\n• Wind: 10 km/h E\n• High/Low: 27°C / 22°C",
            "dubai": "🌤️ **Weather in Dubai:**\n• Temperature: 35°C (feels like 38°C)\n• Conditions: Hot and dry\n• Humidity: 40%\n• Wind: 18 km/h NW\n• High/Low: 38°C / 30°C",
            "paris": "🌤️ **Weather in Paris:**\n• Temperature: 18°C (feels like 16°C)\n• Conditions: Rainy\n• Humidity: 75%\n• Wind: 14 km/h SW\n• High/Low: 20°C / 15°C"
    }
        for city, weather_info in cities.items():
            if city in text_lower:
                return weather_info
        return "🌤️ **Weather in Kanpur:**\n• Temperature: 28°C (feels like 30°C)\n• Conditions: Clear sky\n• Humidity: 55%\n• Wind: 10 km/h NW\n• High/Low: 32°C / 24°C\n\n*Try: weather in Mumbai, Delhi, Bangalore, etc.*"
    
    def _tell_joke(self):
        """Tell a random joke"""
        return f"😄 {random.choice(self.jokes)}"
    
    def _handle_reminder(self, text):
        """Handle reminder creation"""
        words = text.split()
        if len(words) > 2:
            # Extract reminder text
            if 'remind me to' in text.lower():
                reminder_text = ' '.join(words[3:])
            elif 'remind me' in text.lower():
                reminder_text = ' '.join(words[2:])
            else:
                reminder_text = ' '.join(words[1:])
            
            reminders = self._read_json(self.reminders_file)
            reminder = {
                'id': len(reminders) + 1,
                'text': reminder_text,
                'created_at': datetime.now().isoformat(),
                'completed': False
            }
            reminders.append(reminder)
            self._write_json(self.reminders_file, reminders)
            
            return f"✅ Reminder set: '{reminder_text}'"
        else:
            return "Please tell me what to remind you about. Example: 'remind me to call mom'"
    
    def _handle_note(self, text):
        """Handle note creation"""
        words = text.split()
        if len(words) > 2:
            # Extract note text
            if 'note that' in text.lower():
                note_text = ' '.join(words[2:])
            elif 'remember that' in text.lower():
                note_text = ' '.join(words[2:])
            else:
                note_text = ' '.join(words[1:])
            
            notes = self._read_json(self.notes_file)
            note = {
                'id': len(notes) + 1,
                'text': note_text,
                'created_at': datetime.now().isoformat()
            }
            notes.append(note)
            self._write_json(self.notes_file, notes)
            
            return f"📝 Note saved: '{note_text}'"
        else:
            return "Please tell me what to note down. Example: 'note that meeting is at 3 PM'"
    
    def _handle_calculation(self, text):
        """Handle simple calculations"""
        try:
            # Very basic calculation support
            if '+' in text:
                numbers = text.split('+')
                if len(numbers) == 2:
                    result = float(numbers[0].strip()) + float(numbers[1].strip())
                    return f"🧮 Answer: {result}"
            elif '-' in text:
                numbers = text.split('-')
                if len(numbers) == 2:
                    result = float(numbers[0].strip()) - float(numbers[1].strip())
                    return f"🧮 Answer: {result}"
            elif 'x' in text or '*' in text:
                numbers = text.replace('x', '*').split('*')
                if len(numbers) == 2:
                    result = float(numbers[0].strip()) * float(numbers[1].strip())
                    return f"🧮 Answer: {result}"
            elif '/' in text:
                numbers = text.split('/')
                if len(numbers) == 2:
                    result = float(numbers[0].strip()) / float(numbers[1].strip())
                    return f"🧮 Answer: {result}"
        except:
            pass
        
        return "I can help with basic calculations like: 'calculate 5 + 3' or 'what is 10 x 2'"
    
    def _answer_question(self, question):
        """Answer questions from the database"""
        question_lower = question.lower().strip('? .')
        
        # Check exact matches
        if question_lower in self.qa_database:
            return f"📚 {self.qa_database[question_lower]}"
        
        # Check partial matches
        for key, answer in self.qa_database.items():
            if key in question_lower:
                return f"📚 {answer}"
        
        return "I'm not sure about that. Try asking about:\n• Capitals of countries\n• Science facts\n• History questions\n• Or use: weather, time, date, joke, reminder, note"
    
    def _show_reminders(self):
        """Show all reminders"""
        reminders = self._read_json(self.reminders_file)
        if not reminders:
            return "You have no reminders. ✅"
        
        response = "📋 Your Reminders:\n"
        for reminder in reminders:
            status = "✅" if reminder['completed'] else "⏳"
            response += f"{status} {reminder['text']}\n"
        return response
    
    def _show_notes(self):
        """Show all notes"""
        notes = self._read_json(self.notes_file)
        if not notes:
            return "You have no notes. 📝"
        
        response = "📝 Your Notes:\n"
        for note in notes:
            response += f"• {note['text']}\n"
        return response
    
    def show_help(self):
        """Show help menu"""
        return """
🤖 **AI Assistant Commands:**

**Basic Info:**
• hello/hi - Greeting
• time - Current time
• date - Today's date
• joke - Tell a joke

**Knowledge:**
• What is [question] - General knowledge
• Capital of [country] - Geography
• Who invented [thing] - History

**Tools:**
• weather in [city] - Weather info
• remind me to [task] - Set reminder
• note that [info] - Save note
• calculate [math] - Simple math

**View Data:**
• show reminders - View all reminders
• show notes - View all notes

**Exit:**
• bye/quit/exit - Exit assistant
"""
    
    def run(self):
        """Run the assistant"""
        print("🤖 Enhanced AI Assistant Started!")
        print("Type 'help' to see all commands")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("Assistant: Goodbye! 👋")
                    break
                elif user_input.lower() == 'help':
                    response = self.show_help()
                elif user_input.lower() == 'show reminders':
                    response = self._show_reminders()
                elif user_input.lower() == 'show notes':
                    response = self._show_notes()
                else:
                    response = self.process_command(user_input)
                
                print(f"Assistant: {response}")
                
            except KeyboardInterrupt:
                print("\n\nAssistant: Goodbye! 👋")
                break
            except Exception as e:
                print(f"Assistant: Sorry, something went wrong: {e}")

if __name__ == "__main__":
    assistant = EnhancedAIAssistant()
    assistant.run()