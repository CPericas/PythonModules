#Create a Python program using a custom module that asks the user how they are feeling 
# today and responds with a custom message based on the mood entered.


def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "I'm glad to hear that! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "angry": "It's okay to feel angry sometimes. Take a deep breath.",
        "excited": "That's awesome! Ride that wave of excitement and enjoy your day!",
        "tired": "Make sure to get some rest and take care of yourself.",
        "bored": "How about trying something new today?",
        "anxious": "Take it one step at a time. You've got this."
    }
    
    return responses.get(mood, "I'm not sure how to respond to that mood, but I hope you have a great day!")


