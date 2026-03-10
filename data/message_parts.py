import random

openings = [
    "My dearest love,",
    "To the love of my life,",
    "My sweet darling,",
    "My beautiful soulmate,"
]

feelings = [
    "Every day I wake up grateful that you are in my life.",
    "Your love makes my world brighter than the morning sun.",
    "You are the most beautiful part of my life.",
    "Thinking about you fills my heart with peace and happiness."
]

memories = [
    "Every memory with you is a treasure I will always keep.",
    "Your smile is the light that guides my darkest days.",
    "The laughter we share is my favorite sound.",
]

future = [
    "I dream of a future where we grow together every day.",
    "No matter what life brings, I will always choose you.",
    "Our love story is my favorite story ever written."
]

closings = [
    "Forever yours.",
    "With all my love.",
    "Always thinking of you.",
]

def random_letter():

    return f"""
{random.choice(openings)}

{random.choice(feelings)}

{random.choice(memories)}

{random.choice(future)}

{random.choice(closings)}
"""