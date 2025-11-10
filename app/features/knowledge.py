import wikipedia

class KnowledgeService:
    def __init__(self):
        wikipedia.set_lang("en")
        
        # Simple QA database
        self.qa_database = {
            "capital of france": "Paris",
            "capital of germany": "Berlin", 
            "capital of italy": "Rome",
            "capital of india": "New Delhi",
            "height of mount everest": "8,849 meters",
            "inventor of telephone": "Alexander Graham Bell",
            "speed of light": "299,792,458 meters per second",
            "largest planet": "Jupiter"
        }
    
    def answer_question(self, question):
        """Answer general knowledge questions"""
        question_lower = question.lower().strip('? ')
        
        # Check our simple database first
        for key, answer in self.qa_database.items():
            if key in question_lower:
                return answer
        
        # Try Wikipedia for other questions
        try:
            # Get a short summary
            summary = wikipedia.summary(question, sentences=1)
            return summary
        except:
            return "I don't know the answer to that question. Try asking something else!"