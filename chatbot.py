# chatbot.py

import json
import difflib

def get_response(user_input):
    user_input = user_input.lower()

    with open("patterns.json", "r") as f:
        data = json.load(f)

    all_patterns = [pattern for item in data for pattern in item['patterns']]
    best_match = difflib.get_close_matches(user_input, all_patterns, n=1, cutoff=0.6)

    for item in data:
        if best_match and best_match[0] in item['patterns']:
            return item['response']

    return "Sorry, I didn't understand that. Can you try again?"
