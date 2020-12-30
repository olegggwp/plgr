from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений


@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)
    bot.send_message(message.chat.id, AUTHOR+VERSION_OF_BOT)

@bot.message_handler(commands=['author']) 
def send_author(message):
    bot.send_message(message.chat.id, 'oleg ggwp gang')
    bot.send_message(message.chat.id, AUTHOR+VERSION_OF_BOT)

@bot.message_handler(commands=['console'])
def console_control(message):
    try:
        f = open(str(message.chat.id) + "_rights.txt", "r")
        if(f.readline() == 'true'):
            bot.send_message(message.chat.id, 'Hello again, king')
        else:
            bot.send_message(message.chat.id, 'You have not rights of developer\nWanna get them?')
            bot.register_next_step_handler(message, want_password);
 
    except:
        f = open(str(message.chat.id) + "_rights.txt", "x")
        bot.send_message(message.chat.id, 'you are new')
        bot.send_message(message.chat.id, 'neeew')
        f = open(str(message.chat.id) + "_rights.txt", "x")
        f.write('false');

def want_password(message):
    bot.send_message(message.chat.id, 'Enter password')
    bot.register_next_step_handler(message, check_password);

def check_password(message):
    if(message.text == '123'):
       bot.send_message(message.chat.id, 'You are welcome!') 
       f = open(str(message.chat.id) + "_rights.txt", "w")
       f.write('true');
    elif(message.text == 'exit' or message.text == '/exit'):
        bot.send_message(message.chat.id, 'OK, go to main menu')
    else:
        bot.send_message(message.chat.id, 'Incorrect')
        bot.register_next_step_handler(message, want_password);


@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, AUTHOR+VERSION_OF_BOT)


if __name__ == '__main__':
    bot.polling(none_stop=True)