import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class SimpleIntentClassifier:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        
        # Simple pattern-based intent detection
        self.intent_patterns = {
            'weather': ['weather', 'temperature', 'rain', 'forecast', 'hot', 'cold'],
            'reminder': ['remind', 'remember', 'alarm', 'notify'],
            'time': ['time', 'clock', 'current time'],
            'question': ['what', 'who', 'when', 'where', 'why', 'how'],
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'goodbye': ['bye', 'goodbye', 'see you', 'exit', 'quit']
        }
    
    def predict_intent(self, text):
        """Simple rule-based intent detection"""
        text_lower = text.lower()
        
        # Check for exact matches first
        if any(word in text_lower for word in ['weather', 'temperature']):
            return 'weather', 0.9
        elif any(word in text_lower for word in ['remind', 'remember', 'alarm']):
            return 'reminder', 0.9
        elif any(word in text_lower for word in ['time', 'clock']):
            return 'time', 0.9
        elif any(word in text_lower for word in ['hello', 'hi', 'hey']):
            return 'greeting', 0.9
        elif any(word in text_lower for word in ['bye', 'goodbye', 'exit']):
            return 'goodbye', 0.9
        elif any(word in text_lower for word in ['what', 'who', 'when', 'where']):
            return 'question', 0.8
        
        # Default to question for anything else
        return 'question', 0.5
    
    def extract_entities(self, text, intent):
        """Extract basic entities from text"""
        entities = {}
        
        if intent == 'weather':
            # Look for location words
            locations = ['london', 'paris', 'new york', 'delhi', 'mumbai']
            for location in locations:
                if location in text.lower():
                    entities['location'] = location
                    break
        
        elif intent == 'reminder':
            # Extract time and content
            time_words = ['at', 'on', 'tomorrow', 'today']
            words = text.split()
            time_index = -1
            
            for i, word in enumerate(words):
                if word.lower() in time_words and i < len(words) - 1:
                    time_index = i
                    break
            
            if time_index != -1:
                entities['time'] = ' '.join(words[time_index:time_index+2])
                entities['content'] = ' '.join(words[2:time_index])
        
        return entities