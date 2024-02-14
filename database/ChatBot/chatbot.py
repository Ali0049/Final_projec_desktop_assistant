import random

Hello = ('hello', 'hey', 'hii', 'hi', 'hi there', 'hey there', 'greetings', 'howdy', 'salutations', 'yo', 'hiya', 'hiyah', 'hey yo', 'hi there', 'hi buddy', 'hey friend', 'how are ya', 'hello there', 'hi sunshine', 'hiya there')

reply_Hello = ('Hello Sir, I am Jarvis.',
               "Hey, what's up?",
               "Hey, how are you?",
               "Hello Sir, nice to meet you again.",
               "Of course Sir, hello.",
               "Greetings, how can I assist you?",
               "Howdy! What can I do for you today?",
               "Yo! What's going on?",
               "Hiya! How can I help you?",
               "Hey yo! Nice to see you.",
               "Hi there! What brings you here?",
               "Hi buddy! What's on your mind?",
               "Hey friend! How can I assist you today?",
               "How are ya? Ready for some action?",
               "Hello there! What can I do for you today?",
               "Hi sunshine! How's your day going?",
               "Hiya there! Anything I can help you with?")

Bye = ('bye', 'exit', 'sleep', 'go', 'goodbye', 'see you later', 'farewell', 'adios', 'take care', 'later', 'ciao', 'so long', 'till we meet again', 'bye-bye', 'cheerio', 'catch you later', 'bye now', 'goodnight', 'farewell', 'until next time', 'take it easy')

reply_bye = ('Bye Sir.',
            "It's okay.",
            "It will be nice to meet you.",
            "Goodbye.",
            "Thanks.",
            "Okay.",
            "Farewell! Take care.",
            "See you later.",
            "Adios!",
            "Ciao!",
            "So long!",
            "Till we meet again.",
            "Later!",
            "Bye-bye!",
            "Cheerio!",
            "Catch you later!",
            "Bye now!",
            "Goodnight!",
            "Farewell!",
            "Until next time!",
            "Take it easy!",
            "Au revoir!",
            "Peace out!")

How_Are_You = ('how are you', 'are you fine', 'how do you do', 'how are you doing', 'what\'s up', 'how\'s it going', 'what\'s happening', 'how\'s everything', 'how\'s life', 'what\'s good', 'how\'s your day', 'how\'s your mood', 'how are things')

reply_how = ('I am fine.',
             "Excellent.",
             "Moj ho rhi hai.",
             "Absolutely fine.",
             "I'm fine.",
             "Thanks for asking.",
             "I'm doing well, thank you.",
             "Pretty good, how about you?",
             "I'm functioning at optimal capacity.",
             "I'm good, what's happening with you?",
             "Everything's going well, how about yourself?",
             "I'm fine and dandy, how about you?",
             "Life's good, thanks for asking.",
             "Things are great, how about you?",
             "Fantastic as always, how about yourself?",
             "I'm doing well, thank you for asking.",
             "My mood is upbeat and positive.",
             "I'm feeling great today.",
             "Everything is going smoothly.",
             "Life is good, thanks for checking in.",
             "I'm in a good mood, thank you.")

nice = ('nice', 'good', 'thanks', 'awesome', 'great', 'fantastic', 'amazing', 'wonderful', 'splendid', 'terrific', 'excellent', 'outstanding', 'superb', 'stellar', 'brilliant', 'fabulous', 'super', 'marvelous', 'terrific', 'grand', 'lovely', 'super', 'good job', 'well done', 'impressive', 'cool', 'neat', 'beautiful')

reply_nice = ('Thanks.',
              "Oh, it's okay.",
              "Thanks to you.",
              "You're awesome.",
              "Fantastic!",
              "Amazing!",
              "Great!",
              "Wonderful!",
              "Splendid!",
              "Terrific!",
              "Excellent!",
              "Outstanding!",
              "Superb!",
              "Stellar!",
              "Brilliant!",
              "Fabulous!",
              "Super!",
              "Marvelous!",
              "Terrific!",
              "Grand!",
              "Nice!",
              "Good!",
              "Thanks!",
              "Awesome!",
              "Good job!",
              "Well done!",
              "Impressive!",
              "Cool!",
              "Neat!",
              "Beautiful!")

Functions = ['functions', 'abilities', 'what can you do', 'features', 'tasks', 'commands', 'operations', 'capabilities', 'tasks', 'skills', 'tasks', 'assistance', 'commands', 'help', 'support', 'tasks', 'functions', 'options', 'abilities', 'tasks', 'operations']

replay_Functions = ('I can perform many tasks or varieties of tasks. How can I help you?',
                    'I can message your mom that you are not studying...',
                    "Let me ask you first, how can I help you?",
                    "If you want me to tell my features, call: Print Features!",
                    "I can assist you with various commands and operations.",
                    "My capabilities include a wide range of functions.",
                    "I can perform tasks and operations based on your commands.",
                    "Feel free to explore my various capabilities.",
                    "I possess a variety of skills to assist you.",
                    "I'm capable of handling a multitude of tasks and providing assistance.",
                    "I'm here to help! Just let me know what you need.",
                    "Need support or information? I'm at your service.",
                    "I can execute a variety of commands. What would you like me to do?",
                    "If you have any tasks, feel free to assign them to me.")

sorry_reply = ("Sorry, that's beyond my abilities.",
              "Sorry, I can't do that.",
              "Sorry, that's above me.",
              "Apologies, I can't assist with that.",
              "Regrettably, I'm not capable of that.",
              "I'm afraid I can't help with that.",
              "Unfortunately, I cannot perform that task.",
              "I'm sorry, I don't have the capability for that.",
              "Apologies, but that's not something I can do for you.",
              "Regretfully, I'm not able to assist with that request.",
              "I apologize, but that's outside my capabilities.",
              "I'm sorry, I can't fulfill that request.",
              "Apologies, but I don't have the ability to do that.",
              "I'm afraid I cannot comply with that request.",
              "Sorry, that's not within my capabilities.",
              "Apologies, but that's not something I can handle.",
              "I'm sorry, but I cannot perform that action.",
              "Regrettably, that's not something I can assist with.",
              "I apologize, but I'm not equipped to handle that task.",
              "Sorry, but I can't assist with that.")

def ChatterBot(Text):
    
    Text = str(Text)

    for word in Text.split():
        if word in Hello:
            return random.choice(reply_Hello)
    
        elif word in Bye:
            return random.choice(reply_bye)

        elif word in How_Are_You:
            return random.choice(reply_how)

        elif word in nice:
            return random.choice(reply_nice)

        elif word in Functions:
            return random.choice(replay_Functions)
        
    return random.choice(sorry_reply)

# Example usage:
value = ChatterBot('abilities')
print(value)
