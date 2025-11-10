from flask import Flask, render_template, request, jsonify
from .main import EnhancedAIAssistant
import json
from datetime import datetime
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
    template_folder=os.path.join(current_dir, 'templates'),
    static_folder=os.path.join(current_dir, 'static')
)

assistant = EnhancedAIAssistant()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'Please enter a message.'})
        
        # Process the message through your AI assistant
        bot_response = assistant.process_command(user_message)
        
        # Return both user message and bot response
        return jsonify({
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now().strftime("%H:%M")
        })
        
    except Exception as e:
        return jsonify({'response': f'Sorry, I encountered an error: {str(e)}'})

@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    reminders = assistant._read_json(assistant.reminders_file)
    return jsonify(reminders)

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = assistant._read_json(assistant.notes_file)
    return jsonify(notes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)