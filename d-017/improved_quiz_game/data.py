"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Improved Quiz Game
Ref: https://opentdb.com/api_config.php

NOTE: This may benefit from using asynchronous operations (e.g. `async` and
`await`), to do so we must import "aiohttp" and "asyncio"!
"""
import urllib.request
import urllib.error
import json
import html

# Define API options
q_amount = 10
q_difficulty = "medium"
q_format = "boolean"

# Create API query URL
opentdb_api_url = "https://opentdb.com/api.php?"
opentdb_api_url += f"amount={q_amount}"
opentdb_api_url += "&category=9"  # General Knowledge
opentdb_api_url += f"&difficulty={q_difficulty}"
opentdb_api_url += f"&type={q_format}"

# Safely perform the request and get response
try:
    with urllib.request.urlopen(opentdb_api_url) as response:
        status_code = response.status
        if status_code == 200:
            try:
                # NOTE: Unsure if better to allow this to fail if it will!
                json_data = json.loads(response.read().decode())
            except json.JSONDecodeError as e:
                print(e)
        else:
            print(f"HTTP Response Code: {status_code}")
            json_data = None
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)

if json_data is not None:
    # print(f"Response: {json_data}")
    # question_data = json_data['results']
    question_data = []
    # Model the question data to match the original format
    for q in json_data['results']:
        question_data.append({
            'text': html.unescape(q['question']),
            'answer': q['correct_answer']
        })
else:
    # Fallback to the original set of questions
    print("Open Trivia Database unavailable, using default questions!")
    question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.",
         "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.",
         "answer": "True"},
        {"text": "The total surface area of a human lungs is the size of a "
         "football pitch.", "answer": "True"},
        {"text": "In West Virginia, USA, if you accidentally hit an animal "
         "with your car, you are free to take it home to eat.",
         "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of "
         "Parliament, you are entitled to a state funeral.",
         "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.",
         "answer": "True"},
        {"text": "You can lead a cow down stairs but not up stairs.",
         "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.",
         "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more "
         "than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can to kill a small dog.",
         "answer": "True"}
    ]
