// Set welcome message time
document.getElementById('welcomeTime').textContent = getCurrentTime();

function getCurrentTime() {
    return new Date().toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: true 
    });
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendQuickMessage(message) {
    document.getElementById('userInput').value = message;
    sendMessage();
}

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addMessageToChat(message, 'user');
    userInput.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        hideTypingIndicator();
        
        // Add bot response to chat
        addMessageToChat(data.bot_response, 'bot', data.timestamp);
        
    } catch (error) {
        hideTypingIndicator();
        addMessageToChat('Sorry, I encountered an error. Please try again.', 'bot');
        console.error('Error:', error);
    }
    
    // Scroll to bottom
    scrollToBottom();
}

function addMessageToChat(message, sender, timestamp = null) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const time = timestamp || getCurrentTime();
    
    if (sender === 'user') {
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-text">${message}</div>
                <div class="message-time">${time}</div>
            </div>
            <div class="message-avatar">
                <i class="fas fa-user"></i>
            </div>
        `;
    } else {
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="message-content">
                <div class="message-text">${formatMessage(message)}</div>
                <div class="message-time">${time}</div>
            </div>
        `;
    }
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function formatMessage(message) {
    // Convert line breaks to HTML
    return message.replace(/\n/g, '<br>');
}

function showTypingIndicator() {
    const chatMessages = document.getElementById('chatMessages');
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typingIndicator';
    typingDiv.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-robot"></i>
        </div>
        <div class="message-content">
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    
    chatMessages.appendChild(typingDiv);
    scrollToBottom();
}

function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function scrollToBottom() {
    const chatMessages = document.getElementById('chatMessages');
    // Use multiple methods to ensure scrolling works
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    // Additional method for better compatibility
    setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 100);
}


// Add typing indicator CSS
const style = document.createElement('style');
style.textContent = `
    .typing-indicator {
        display: flex;
        align-items: center;
        height: 20px;
    }
    
    .typing-indicator span {
        height: 8px;
        width: 8px;
        background: #94a3b8;
        border-radius: 50%;
        display: inline-block;
        margin: 0 2px;
        animation: typing 1s infinite;
    }
    
    .typing-indicator span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-indicator span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
`;
document.head.appendChild(style);

// Focus on input when page loads
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('userInput').focus();
});