import json
from datetime import datetime
from _collections import _count_elements
import os


print("Welcome to the Dream Theme Analyzer")
theme = {"flying": "freedom", "water": "Emotion", "rain": "pain", "falling":"relationship","nude":"fear of embarrassment","Death":"Anxiety,anxiety regarding death"}
user_dream = input("What did you dream about today? ")
date = datetime.today().strftime('%Y-%m-%d')
print(date)
data = []
if os.path.exists('data.json'):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []
for i in theme:
    if i in user_dream.lower():
        print(theme[i])
        new_dream_entry = {
            "date": date,
            "themes": theme[i],
            "description":"user_dream"
        }
        data.append(new_dream_entry)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("data saved to data.json!")
response = input("Do you want to get a summary of your dreams ?? yes or no ??")
count = 0
if response.lower() == "yes":
    for i in file:
        count += 1
        count1 = {"Coun":"count","name":"file"}
        print(count1)
else:
    print('ok! Have a great day')


