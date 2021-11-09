from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Buddy',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)

trainer.train(
    [
        'Hi',
        'Hello',
        'I have a complaint.',
        'Please elaborate your concern.'
    ]
)

response = bot.get_response('I have a complaint.')
print("Bot Response:", response)