import telebot
from telebot import types
# -- Крч не буду комментировать, разбирайтесь сами
bot = telebot.TeleBot('Вставьте айпи сюды :)))))))))))))))))))))')
restaurant_info = {
    "Название": "Вкусно и точка",
    "Рабочее время": "9:00 - 22:00",
    "Адрес": "проспект Ленина, 26"
}

Menu = {
    "Бургер": 300,
    "Салат Цезарь": 350,
    "Чичевичный суп": 250,
    "Наполеон": 200,
}

Tables = {
    1: "Свободен",
    2: "Занят",
    3: "Свободен",
    4: "Занят"
}


@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Используйте команды для взаимодействия")
@bot.message_handler(commands= ['info'])
def info(message):
    info_text =f"Название: {restaurant_info['Название']}Рабочее время: {restaurant_info['Рабочее время']}Адрес: {restaurant_info['Адрес']}"
    bot.send_message(message.chat.id, info_text)
@bot.message_handler(commands=['menu'])
def show_menu(message):
    menu_text = "Меню:\n" + "\n".join([f"{dish}: {price} руб." for dish, price in Menu.items()])
    bot.send_message(message.chat.id, menu_text)
@bot.message_handler(commands=['tables'])
def show_tables(message):
    tables_text = "Столики:\n" + "\n".join([f"Столики {num}: {status}" for num, status in Tables.items()])
    bot.send_message(message.chat.id, tables_text)
@bot.message_handler(commands=['reserve'])
def reserve_table(message):
    bot.send_message(message.chat.id, "Введите номер столика для бронирования")
@bot.message_handler(func=lambda message:message.text.isdigit())
def reserve_table_confirm(message):
    table_number = int(message.text)
    if table_number in Tables and Tables[table_number] == "Свободен":
        Tables[table_number] = "Занят"
        bot.send_message(message.chat.id, f"Столик {table_number} успешно забронирован!")
    else:
        bot.send_message(message.chat.id, "Столик занят или не существует")
    
@bot.message_handler(commands=['order'])
def order_food(message):
    bot.send_message(message.chat.id, "Введите название блюда для заказа: ")

@bot.message_handler(func=lambda message:message.text in Menu)
def order_food_confirm(message):
    bot.send_message(message.chat.id, f"Вы заказали {message.text}. Ожидайте!")
@bot.message_handler(commands=['review'])
def leave_review(message):
    bot.send_message(message.chat.id, "Введите ваш отзыв: ")

@bot.message_handler(func=lambda message: True)
def save_review(message):
    bot.send_message(message.chat.id, "Ваш отзыв оставлен")

@bot.message_handler(commands= ['loyalty'])
def loyalty_system(message):
    bot.send_message(message.chat.id, "Система лояльности: каждые 10 заказов - 1 бесплатно")

bot.polling()
