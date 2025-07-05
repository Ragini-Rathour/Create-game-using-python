
import random
from textblob import TextBlob
import time

# Predefined responses based on mood
supportive_responses = {
    "positive": [
        "That's great to hear! Keep smiling 😊",
        "I'm glad you're feeling good! 🌟",
        "Awesome! Remember to keep doing what makes you happy 💖"
    ],
    "negative": [
        "I'm really sorry you're feeling this way. You're not alone 🤗",
        "It’s okay to feel sad. Take a deep breath and do something kind for yourself 💆",
        "I'm here for you. Maybe take a break or talk to someone you trust 💬"
    ],
    "neutral": [
        "I'm here if you want to talk or share something 💬",
        "It's okay to feel 'meh' sometimes. Want to try a quick breathing exercise?",
        "Let’s chat more. How are you feeling deep down?"
    ]
}

# Self-care tips
tips = [
    "🧘 Try 5 minutes of deep breathing",
    "📓 Write in a journal for 10 minutes",
    "🎵 Listen to your favorite relaxing song",
    "🚶‍♀️ Take a short walk or stretch your body",
    "🍵 Drink some water or herbal tea"
]

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def mental_health_chatbot():
    print("🤖 Hi! I'm your Mental Wellness Chatbot.")
    print("You can talk to me about how you feel. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Take care of yourself! 💖 You're doing your best.")
            break

        sentiment = get_sentiment(user_input)
        response = random.choice(supportive_responses[sentiment])
        print("Chatbot:", response)

        time.sleep(1)
        print("Chatbot: Here's a tip for you:", random.choice(tips))
        print("")

        







        