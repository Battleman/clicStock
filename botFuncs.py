from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import googleSheets

commands = {'list':'List all items in stock', 'help':'This command help :)','quit':'stop the bot. For everyone. Forever.'}

updater = Updater(token='512461432:AAFylLRostkwNvAxP43IcHI1cJ5NpRVqZko')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")    
def quit(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Thanks for talking with me. By by !")
    updater.stop()
    exit()
def listItems(bot, update):
    serv = googleSheets.init()
    values = googleSheets.getAllValues(serv)
    titre = "{}\t\t{}\t\t{}\n".format(values[0][0],values[0][1],values[0][2])
    content="\n".join(["{}\t\t{}\t\t{}".format(v[0],v[1],v[2]) for v in values[1:]])
    s = titre + content
    bot.send_message(chat_id=update.message.chat_id, text="The following articles are in stock:\n{}".format(s))
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
def helper(bot, update):
    helpHeader = "Hi! This is the help message for ClicStock_Bot. Here are the various commands you can use:\n\n"
    helpBody = "\n".join(["{}\t\t{}".format(x, commands[x]) for x in commands])
    bot.send_message(chat_id=update.message.chat_id, text=helpHeader+helpBody)
def echo(bot, update):
    print(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)