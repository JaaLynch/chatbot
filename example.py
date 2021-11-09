from chatterbot import ChatBot


bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
)

# Print an example of getting one math based response
response = bot.get_response('What is 4 + 15?')
print(response)

# Print an example of getting one time based response
response = bot.get_response('How long until Christmas?')
print(response)