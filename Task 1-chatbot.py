import re

user_name = None
user_preferences = {}

def simple_chatbot(user_input):
    global user_name, user_preferences
    user_input = user_input.lower()

    rules = {
        r'hello|hi|hey|hlo': lambda match: f'Hello, {user_name}! How can I help you today?' if user_name else 'Hello! How can I help you?',
        r'what is your name': lambda match: f'My name is FRIDAY I am a Chatbot Created by SRIRAM. What\'s your name?',
        r'my name is (\w+)': lambda match: set_user_name(match.group(1)),
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'\bthanks\b|\bthank you\b': 'You\'re welcome!',
        r'\b(what can you do)\b': 'I can help you with information, answer questions, or just chat with you.',
        r'\b(your favorite)\b': 'I don\'t have preferences; I\'m just a chatbot.',
        r'\b(how do you work)\b': 'I process and analyze text based on predefined patterns to generate responses.',
        r'\b(who created you)\b': 'I was created by SRIRAM.',
        r'\b(who are you)\b': 'I am a language model created by SRIRAM called FRIDAY.',
        r'\b(what time is it)\b': 'I don\'t have real-time capabilities, but you can check your device for the current time.',
        r'\b(what is the weather today)\b': 'I don\'t have real-time data, but you can check a weather website or app for the current conditions.',
        r'\b(tell me a joke)\b': 'Why don\'t scientists trust atoms? Because they make up everything!',
        r'\b(tell me about yourself)\b': 'I\'m just a computer program designed to assist with information and chat with users.',
        r'\b(who is the president of the United States)\b': 'I don\'t have real-time information. Please check the latest news for the current president.',

        r'\b(how old are you)\b': 'I don\'t have an age. I exist in the digital realm.',
        r'\b(what is the meaning of life)\b': 'The meaning of life is a philosophical question. I don\'t have a definitive answer.',
        r'\b(favorite color)\b': 'I change colors like a chameleon depending on the mood of the conversation!',
        r'\b(what is your favorite topic)\b': lambda match: f'I don\'t have a favorite topic, {user_name}. What topics are you interested in?',
        r'\b(my favorite topic is (\w+))\b': lambda match: set_user_preference(match.group(2)),
        r'\b(tell me something about my favorite topic)\b': lambda match: get_user_preference_info(match.group(1)),
        
        r'\b(what time is it)\b': 'I don\'t have real-time capabilities, but you can check your device for the current time.',
        r'\b(what day is it today)\b': 'I don\'t have real-time capabilities, but you can check your device for the current date.',
        r'\b(set a reminder for (\d+:\d+) today)\b': lambda match: f'Reminder set for {match.group(2)} today.',
        r'\b(set a reminder for (\d+:\d+) tomorrow)\b': lambda match: f'Reminder set for {match.group(2)} tomorrow.',
        r'\b(tell me a story)\b': 'Once upon a time, in a land of code, there was a chatbot named FRIDAY...',
        r'\b(play a game)\b': 'Let\'s play a game! I\'ll think of something, and you try to guess what it is. Ready?',
        r'\b(yes)\b': lambda match: 'Great! I\'m thinking of an animal. Can you guess which one?',
        r'\b(no)\b': 'No worries! Let me know if you change your mind.',
        r'\b(dog)\b': 'Yes, you got it! I was thinking of a dog. Well done!',
        r'\b(how can I contact support)\b': 'For support, please contact our customer service at support@example.com.',
        r'\b(learn something new)\b': 'Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!',
        r'\b(tell me a joke)\b': 'Why don\'t scientists trust atoms? Because they make up everything!',
        r'\b(tell me a pun)\b': 'I used to be a baker because I kneaded dough.',
        r'\b(tell me a pop culture reference)\b': 'May the Force be with you! (Star Wars)',
        r'\b(\d+ \+ \d+)\b': lambda match: str(eval(match.group())),
        r'\b(who invented the telephone)\b': 'Alexander Graham Bell is credited with inventing the telephone.',
    }

    for pattern, response in rules.items():
        if callable(response):
            match = re.search(pattern, user_input)
            if match:
                return response(match)
        elif re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def set_user_name(name):
    global user_name
    user_name = name
    return f'Nice to meet you, {name}! How can I assist you today?'

def set_user_preference(topic):
    global user_preferences
    user_preferences['favorite_topic'] = topic
    return f'Got it! I see that {user_name}\'s favorite topic is {topic}. Anything specific you want to know about {topic}?'

def get_user_preference_info(topic):
    global user_preferences
    return f'Here\'s an interesting fact about {topic}: [Your interesting fact about {topic}]'

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
