import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

responses_dict = {
    "if": [
        "That's a tough one, but it could happen.",
        "Only time will tell.",
        "It's highly uncertain.",
        "If everything aligns perfectly, yes.",
        "It depends on the circumstances.",
        "That’s a possibility, but don't bet on it.",
        "It's a long shot, but it could work."
    ],
    "will": [
        "Yes, without a doubt!",
        "Chances are high.",
        "It looks promising!",
        "The outlook is good.",
        "Absolutely, just wait for it.",
        "I'm sure of it!",
        "Yes, but with caution."
    ],
    "can": [
        "You can, but it'll take some effort.",
        "Yes, if you try hard enough.",
        "Anything's possible!",
        "You have the power to make it happen.",
        "With determination, yes.",
        "It depends on your actions.",
        "The odds are in your favor."
    ],
    "is": [
        "Yes, that's true.",
        "Certainly!",
        "It's likely to be the case.",
        "Signs point to yes.",
        "Yes, but it's complicated.",
        "That's a bit unclear, try again.",
        "The answer lies within you."
    ],
    "which": [
        "The first option seems better.",
        "Go with the second choice.",
        "Neither, there's a better one waiting for you.",
        "It's hard to tell, both have their merits.",
        "The choice is yours, but the first looks promising.",
        "Trust your instincts on this one."
    ],
    "who": [
        "The person you least expect.",
        "Someone close to you.",
        "An unexpected stranger.",
        "The answer is hidden in plain sight.",
        "Someone who has been waiting for this moment.",
        "You will soon find out who."
    ],
    "where": [
        "Somewhere far, but worth the journey.",
        "Closer than you think.",
        "A place you’ve been dreaming of.",
        "It’s right around the corner.",
        "You’ll know the place when you see it.",
        "Far off, but keep moving."
    ],
    "when": [
        "Sooner than you expect.",
        "In the near future.",
        "Timing is unclear, but it’s coming.",
        "When the time is right, you’ll know.",
        "Not too far from now.",
        "In due time, patience is key."
    ],
    "default": [
        "I'm not sure about that.",
        "That’s not for me to say.",
        "Ask again later.",
        "I cannot predict that right now.",
        "It's better if you don't know.",
        "Let me think about that... ask again.",
        "I don't have a clear answer for that."
    ]
}

def get_question_type(question):
    question_words = question.lower().split()
    if not question_words:
        return 'default'
    
    first_word = question_words[0]
    
    if first_word in responses_dict:
        return first_word
    else:
        return 'default'

def magic_8_ball():
    print(Fore.CYAN + Style.BRIGHT + "\n✨ Welcome to the Advanced Smart Magic 8-Ball! 🎱 ✨")
    print(Fore.CYAN + "Ask any question starting with words like 'If', 'Will', 'Can', 'Is', 'Which', 'Who', 'Where', 'When', etc.")
    print(Fore.CYAN + "Type 'exit' when you want to quit.\n")
    
    while True:
        question = input(Fore.YELLOW + Style.BRIGHT + "🔮 What is your question? (type 'exit' to quit): " + Style.RESET_ALL).strip()
        
        if question.lower() == 'exit':
            print(Fore.GREEN + "\nThank you for playing! See you next time! 🎉")
            break

        question_type = get_question_type(question)

        print(Fore.MAGENTA + "\nShaking the Magic 8-Ball... 🌟")
        time.sleep(2)

        answer = random.choice(responses_dict[question_type])
        
        print(Fore.BLUE + Style.BRIGHT + f"\n🎱 The Magic 8-Ball says: {answer}\n")

if __name__ == "__main__":
    magic_8_ball()
