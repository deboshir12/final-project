# import telebot
# from telebot import types # для указание типов

# bot = telebot.TeleBot('6270091840:AAGTuqNNf4LrtiaLrJJzNigvVZmameg9jyM')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("👋 Поздороваться")
#     btn2 = types.KeyboardButton("🛤️ узнать маршрут")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для проекта по питону".format(message.from_user), reply_markup=markup)
    
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "👋 Поздороваться"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что пользуешься нашим ботом!)")
#     elif(message.text == "🛤️ узнать маршрут"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("🚌 автобус")
#         btn2 = types.KeyboardButton("🚎 троллейбус")
#         btn3 = types.KeyboardButton("🚃 трамвай")
#         back = types.KeyboardButton("🛑 Вернуться в главное меню") 
#         markup.add(btn1, btn2, btn3, back)
#         bot.send_message(message.chat.id, text="Выберите тип транспорта: ", reply_markup=markup)
    
#     elif(message.text == "🚌 автобус"):
#         bot.send_message(message.chat.id, "Введите номер маршрута: ")
        
#     elif(message.text == "🚎 троллейбус"):
#         bot.send_message(message.chat.id, "Введите номер маршрута: ")
    
#     elif message.text == "🚃 трамвай":
#         bot.send_message(message.chat.id, text="Введите номер маршрута: ")
    
#     elif (message.text == "🛑 Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("🛤️ узнать маршрут")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

# bot.polling(none_stop=True)



    