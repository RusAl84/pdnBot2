from webbrowser import get
import telebot;

bot = telebot.TeleBot('5982175377:AAG9_9nyODx2tgpqg5qYgKqAIuhUdhPukTg');

def gl(login='rusal'):
    import json
    fileObject = open("data.json", "r")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            dataDict=item['data']
            for key in dataDict:
                result+=" " + key
    print(result)
    return result


def gd(login='rusal', getpdn='passport'):
    getpdn = getpdn.lower()
    import json
    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            result=item['data'][getpdn]
    return str(result)

def gn(login='rusal'):
    import json
    fileObject = open("data.json", "r",encoding="UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            result=item['name']
    return result

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Список команд: /gl - получить список хранимых данных;   /gd ""имя данных"" - получить данные; /name получить имя владельца даных  ")
    elif str(message.text).lower() == "/gl":
        # print(message.chat.id)
        bot.send_message(message.from_user.id, "Хранимые персональные данные: " + gl(message.chat.id))
    elif str(message.text).lower() == "/name":
        bot.send_message(message.from_user.id, "Имя вледльца данных: " + gn(message.chat.id))
    elif splitted_text[0] == "/gd":
        if len(splitted_text)>1:
            bot.send_message(message.from_user.id, "Хранимые персональные данные по полю " + splitted_text[1] + ": " + gd(message.chat.id, splitted_text[1]))
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")

bot.polling(none_stop=True, interval=0)