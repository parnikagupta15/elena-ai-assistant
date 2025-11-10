from flask import Flask, render_template, request, jsonify
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import EnhancedAIAssistant
except ImportError:
    # Try relative import
    from .main import EnhancedAIAssistant

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
            static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)