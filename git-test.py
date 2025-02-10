import datetime
import random

messages = [
    "You're doing great. Keep going. 🚀",
    "Some days are tough, but so are you. 💪",
    "You're enough just as you are. 🌿",
    "Take a deep breath—you're right where you need to be. 🌊",
    "Keep shining, even when no one's watching. ✨",
    "A small step forward is still progress. Keep moving. 🏃‍♂️",
    "You're not alone. You've got this. 💙"
]

def daily_message():
    today = datetime.date.today()
    message = random.choice(messages)
    return f"📅 {today}\n💭 {message}"

print(daily_message())
