from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Training Example'
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

#response = bot.get_response('Hello')
#print("Bot Response:", response)

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
