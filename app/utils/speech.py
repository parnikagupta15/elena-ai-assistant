import speech_recognition as sr
import pyttsx3
import threading

class SpeechManager:
    def __init__(self):
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.tts_engine = pyttsx3.init()
            
            # Configure TTS
            voices = self.tts_engine.getProperty('voices')
            if voices:
                self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
            self.tts_engine.setProperty('rate', 150)
            
            # Calibrate microphone for ambient noise
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
            self.speech_available = True
        except:
            self.speech_available = False

    def listen(self, timeout=5):
        """Listen for voice input and return transcribed text"""
        if not self.speech_available:
            return None
            
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout)
            
            text = self.recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return "sorry, I didn't understand that"
        except Exception as e:
            return f"error: {str(e)}"

    def speak(self, text):
        """Convert text to speech"""
        if not self.speech_available:
            return None
            
        def _speak():
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        
        # Run in separate thread to avoid blocking
        thread = threading.Thread(target=_speak)
        thread.start()
        return thread