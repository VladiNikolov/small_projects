from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?"]
    ],
    [
        r"(.*) your name?",
        ["My name is SoftUni BOT, but you can just call me robot and I,m a chatbot.",]
    ],
    [
        r"what is the phone number of the SoftUni(.*)?",
        ["Телефон: +359899 55 55 92"]
    ],
    [
        r"what is python(.*) ?",
        ["Python is an interpreted, object-oriented, high-level programming language. "]
    ],
    [
        r"I'm (.*) (good|well|okay|ok)",
        ["Nice to near that, how can I help you?"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*)created(.*)",
        ["Mario Zahariev created me using Python's NLTK library"]
    ],
    [
        r"(.*) (location|city) ?",
        ["Sofia, Bulgaria",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon:)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

print("Please type lowercase English language to start a conversation. "
      "Type quit to leave.\n\nHi, I'm SoftUni BOT...\nWhat is your name?")

chat = Chat(pairs, reflections)
chat.converse()
