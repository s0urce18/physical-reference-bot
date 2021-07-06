import telebot
from telebot import types
from datetime import datetime, date, time

print("Bot is running")

bot = telebot.TeleBot('')

admin="0"
ausername="0"

#admin---------------------------------------------------------------------
@bot.message_handler(commands=['admin'])
def admin_message(message):
    global admin
    sent=bot.send_message(message.from_user.id, "Введи пароль")
    bot.register_next_step_handler(sent, admin_password)

def admin_password(message):
    global admin
    global ausername
    if message.text == "":
        admin=message.from_user.id
        print(admin)
        if bool(message.from_user.username)==True:
            ausername="@"+message.from_user.username
        else:
            ausername='"'+message.from_user.first_name+'"'
        bot.send_message(admin, "Ты теперь админ")
    else:
        bot.send_message(message.from_user.id, "Пароль неверный")
        bot.send_message(message.from_user.id, "Ты не админ")

@bot.message_handler(commands=['adminn'])
def admin_message(message):
    global admin
    global ausername
    if admin=="0":
        bot.send_message(message.from_user.id, "Админ не зарегистрирован")
    else:
        bot.send_message(message.from_user.id, ausername)
#/admin---------------------------------------------------------------------

@bot.message_handler(commands=['help'])
def help_messaage(message):
    bot.send_message(message.from_user.id, "/start - начать")
    bot.send_message(message.from_user.id, "/review - передать отзыв")
    bot.send_message(message.from_user.id, "/help - помощь")
    bot.send_message(message.from_user.id, "/about - об о мне")

@bot.message_handler(commands=['about'])
def about_messaage(message):
    bot.send_message(message.from_user.id, "Я бот-справочник физики")

@bot.message_handler(commands=['review'])
def review_message(message):
    global admin
    global rusername
    if bool(message.from_user.username)==True:
        rusername="@"+message.from_user.username
    else:
        rusername='"'+message.from_user.first_name+'"'
    sent=bot.send_message(message.from_user.id, "Напиши одним сообщением что ты хочешь что б я передал")
    bot.register_next_step_handler(sent, review_text)

def review_text(message):
    global admin
    global rusername
    bot.send_message(admin, "Новый отзыв от "+rusername+":")
    bot.send_message(admin, message.text)
    bot.send_message(message.from_user.id, "Передал:)")

@bot.message_handler(commands=['start'])
def welcome_message(message):
    user = bot.get_me()
    print("____Time____: "+str(datetime.today()))
    print("____Bot____: "+str(user))
    print("____User____: "+str(message))
    bot.send_message(message.from_user.id, "Привет")
    keyboard = types.InlineKeyboardMarkup()
    key_form = types.InlineKeyboardButton(text='Формулы', callback_data='form')
    keyboard.add(key_form)
    key_con = types.InlineKeyboardButton(text='Константы', callback_data='con')
    keyboard.add(key_con)
    key_dp = types.InlineKeyboardButton(text='Десятичные приставки', callback_data='dp')
    keyboard.add(key_dp)
    key_ei = types.InlineKeyboardButton(text='Единицы измерения', callback_data='ei')
    keyboard.add(key_ei)
    key_smre = types.InlineKeyboardButton(text='Соотношение между различными единицами', callback_data='smre')
    keyboard.add(key_smre)
    key_mch = types.InlineKeyboardButton(text='Масса частиц', callback_data='mch')
    keyboard.add(key_mch)
    key_pl = types.InlineKeyboardButton(text='Плотность', callback_data='pl')
    keyboard.add(key_pl)
    key_ute = types.InlineKeyboardButton(text='Удельная теплоемкость', callback_data='ute')
    keyboard.add(key_ute)
    key_mlm = types.InlineKeyboardButton(text='Молярные массы', callback_data='mlm')
    keyboard.add(key_mlm)
    key_tpl = types.InlineKeyboardButton(text='Плавление элементов', callback_data='tpl')
    keyboard.add(key_tpl)
    key_usp = types.InlineKeyboardButton(text='Удельное сопротивление', callback_data='usp')
    keyboard.add(key_usp)
    key_ma = types.InlineKeyboardButton(text='Масса атомов', callback_data='ma')
    keyboard.add(key_ma)
    question = 'Выбери раздел:'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #formulas----------------------------------------------------------------------------------------------------
    if call.data == 'form':
        keyboard = types.InlineKeyboardMarkup()
        key_meh = types.InlineKeyboardButton(text='Механика', callback_data='meh')
        keyboard.add(key_meh)
        key_zsm = types.InlineKeyboardButton(text='Законы сохранения в механике', callback_data='zsm')
        keyboard.add(key_zsm)
        key_kv = types.InlineKeyboardButton(text='Колебания и волны', callback_data='kv')
        keyboard.add(key_kv)
        key_mpty = types.InlineKeyboardButton(text='Молекулярная физика. Тепловые явления', callback_data='mpty')
        keyboard.add(key_mpty)
        key_gs = types.InlineKeyboardButton(text='Гидростатика', callback_data='gs')
        keyboard.add(key_gs)
        key_el = types.InlineKeyboardButton(text='Электродинамика', callback_data='el')
        keyboard.add(key_el)
        key_opt = types.InlineKeyboardButton(text='Оптика', callback_data='opt')
        keyboard.add(key_opt)
        key_kp = types.InlineKeyboardButton(text='Квантовая физика', callback_data='kp')
        keyboard.add(key_kp)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'meh':
        keyboard = types.InlineKeyboardMarkup()
        key_knm = types.InlineKeyboardButton(text='Кинематика', callback_data='knm')
        keyboard.add(key_knm)
        key_dnm = types.InlineKeyboardButton(text='Динамика', callback_data='dnm')
        keyboard.add(key_dnm)
        key_stt = types.InlineKeyboardButton(text='Статика', callback_data='stt')
        keyboard.add(key_stt)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'knm':
        bot.send_photo(call.from_user.id, photo=open('photos/Кинематика.png', 'rb'))
    elif call.data == 'dnm':
        bot.send_photo(call.from_user.id, photo=open('photos/Динамика.png', 'rb'))
    elif call.data == 'stt':
        bot.send_photo(call.from_user.id, photo=open('photos/Статика.png', 'rb'))
    elif call.data == 'zsm':
        keyboard = types.InlineKeyboardMarkup()
        key_zsi = types.InlineKeyboardButton(text='Закон сохранения импульса', callback_data='zsi')
        keyboard.add(key_zsi)
        key_zse = types.InlineKeyboardButton(text='Закон сохранения энергии', callback_data='zse')
        keyboard.add(key_zse)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'zsi':
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения импульса.png', 'rb'))
    elif call.data == 'zse':
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения энергии1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения энергии2.png', 'rb'))
    elif call.data == 'kv':
        bot.send_photo(call.from_user.id, photo=open('photos/Колебания и волны.png', 'rb'))
    elif call.data == 'mpty':
        bot.send_photo(call.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления2.png', 'rb'))
    elif call.data == 'gs':
        bot.send_photo(call.from_user.id, photo=open('photos/Гидростатика.png', 'rb'))
    elif call.data == 'el':
        bot.send_photo(call.from_user.id, photo=open('photos/Электродинамика1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Электродинамика2.png', 'rb'))
    elif call.data == 'opt':
        bot.send_photo(call.from_user.id, photo=open('photos/Оптика.png', 'rb'))
    elif call.data == 'kp':
        bot.send_photo(call.from_user.id, photo=open('photos/Квантовая физика.png', 'rb'))
    #other----------------------------------------------------------------------------------------------------
    elif call.data == 'con':
        bot.send_photo(call.from_user.id, photo=open('photos/Константы.png', 'rb'))
    elif call.data == 'dp':
        bot.send_photo(call.from_user.id, photo=open('photos/Десятичные приставки.png', 'rb'))
    elif call.data == 'ei':
	    keyboard = types.InlineKeyboardMarkup()
	    key_si = types.InlineKeyboardButton(text='СИ', callback_data='si')
	    keyboard.add(key_si)
	    key_psi = types.InlineKeyboardButton(text='Производные от СИ', callback_data='psi')
	    keyboard.add(key_psi)
	    key_osn = types.InlineKeyboardButton(text='Основные', callback_data='osn')
	    keyboard.add(key_osn)
	    key_tm = types.InlineKeyboardButton(text='Время', callback_data='tm')
	    keyboard.add(key_tm)
	    question = 'Выбери раздел:'
	    bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'si':
    	bot.send_photo(call.from_user.id, photo=open('photos/СИ1.png', 'rb'))
    	bot.send_photo(call.from_user.id, photo=open('photos/СИ2.png', 'rb'))
    elif call.data == 'psi':
    	bot.send_photo(call.from_user.id, photo=open('photos/Производные от СИ.png', 'rb'))
    elif call.data == 'osn':
    	bot.send_photo(call.from_user.id, photo=open('photos/Основные.png', 'rb'))
    elif call.data == 'tm':
    	bot.send_photo(call.from_user.id, photo=open('photos/Время.png', 'rb'))
    elif call.data == 'smre':
        bot.send_photo(call.from_user.id, photo=open('photos/Соотношение между различными единицами.png', 'rb'))
    elif call.data == 'mch':
        bot.send_photo(call.from_user.id, photo=open('photos/Масса частиц.png', 'rb'))
    elif call.data == 'pl':
        bot.send_photo(call.from_user.id, photo=open('photos/Плотность.png', 'rb'))
    elif call.data == 'ute':
        bot.send_photo(call.from_user.id, photo=open('photos/Удельная теплоемкость.png', 'rb'))
    elif call.data == 'mlm':
        bot.send_photo(call.from_user.id, photo=open('photos/Молярные массы.png', 'rb'))
    elif call.data == 'tpl':
        bot.send_photo(call.from_user.id, photo=open('photos/Плавление элементов.png', 'rb'))
    elif call.data == 'usp':
        bot.send_photo(call.from_user.id, photo=open('photos/Удельное сопротивление.png', 'rb'))
    elif call.data == 'ma':
        bot.send_photo(call.from_user.id, photo=open('photos/Масса атомов.png', 'rb'))


bot.polling(none_stop=True, interval=0)

#admin---------------------------------------------------------------------
@bot.message_handler(commands=['admin'])
def admin_message(message):
    global admin
    sent=bot.send_message(message.from_user.id, "Введи пароль")
    bot.register_next_step_handler(sent, admin_password)

def admin_password(message):
    global admin
    global ausername
    if message.text == "01gleb09":
        admin=message.from_user.id
        print(admin)
        if bool(message.from_user.username)==True:
            ausername="@"+message.from_user.username
        else:
            ausername='"'+message.from_user.first_name+'"'
        bot.send_message(admin, "Ты теперь админ")
    else:
        bot.send_message(message.from_user.id, "Пароль неверный")
        bot.send_message(message.from_user.id, "Ты не админ")

@bot.message_handler(commands=['adminn'])
def admin_message(message):
    global admin
    global ausername
    if admin=="0":
        bot.send_message(message.from_user.id, "Админ не зарегистрирован")
    else:
        bot.send_message(message.from_user.id, ausername)
#/admin---------------------------------------------------------------------

@bot.message_handler(commands=['help'])
def help_messaage(message):
    bot.send_message(message.from_user.id, "/start - начать")
    bot.send_message(message.from_user.id, "/review - передать отзыв")
    bot.send_message(message.from_user.id, "/help - помощь")
    bot.send_message(message.from_user.id, "/about - об о мне")

@bot.message_handler(commands=['about'])
def about_messaage(message):
    bot.send_message(message.from_user.id, "Я бот-справочник физики")

@bot.message_handler(commands=['review'])
def review_message(message):
    global admin
    global rusername
    if bool(message.from_user.username)==True:
        rusername="@"+message.from_user.username
    else:
        rusername='"'+message.from_user.first_name+'"'
    sent=bot.send_message(message.from_user.id, "Напиши одним сообщением что ты хочешь что б я передал")
    bot.register_next_step_handler(sent, review_text)

def review_text(message):
    global admin
    global rusername
    bot.send_message(admin, "Новый отзыв от "+rusername+":")
    bot.send_message(admin, message.text)
    bot.send_message(message.from_user.id, "Передал:)")

@bot.message_handler(commands=['start'])
def welcome_message(message):
    user = bot.get_me()
    print("____Time____: "+str(datetime.today()))
    print("____Bot____: "+str(user))
    print("____User____: "+str(message))
    bot.send_message(message.from_user.id, "Привет")
    keyboard = types.InlineKeyboardMarkup()
    key_form = types.InlineKeyboardButton(text='Формулы', callback_data='form')
    keyboard.add(key_form)
    key_con = types.InlineKeyboardButton(text='Константы', callback_data='con')
    keyboard.add(key_con)
    key_dp = types.InlineKeyboardButton(text='Десятичные приставки', callback_data='dp')
    keyboard.add(key_dp)
    key_smre = types.InlineKeyboardButton(text='Соотношение между различными единицами', callback_data='smre')
    keyboard.add(key_smre)
    key_mch = types.InlineKeyboardButton(text='Масса частиц', callback_data='mch')
    keyboard.add(key_mch)
    key_pl = types.InlineKeyboardButton(text='Плотность', callback_data='pl')
    keyboard.add(key_pl)
    key_ute = types.InlineKeyboardButton(text='Удельная теплоемкость', callback_data='ute')
    keyboard.add(key_ute)
    key_mlm = types.InlineKeyboardButton(text='Молярные массы', callback_data='mlm')
    keyboard.add(key_mlm)
    key_tpl = types.InlineKeyboardButton(text='Плавление элементов', callback_data='tpl')
    keyboard.add(key_tpl)
    key_usp = types.InlineKeyboardButton(text='Удельное сопротивление', callback_data='usp')
    keyboard.add(key_usp)
    key_ma = types.InlineKeyboardButton(text='Масса атомов', callback_data='ma')
    keyboard.add(key_ma)
    question = 'Выбери раздел:'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #formulas----------------------------------------------------------------------------------------------------
    if call.data == 'form':
        keyboard = types.InlineKeyboardMarkup()
        key_meh = types.InlineKeyboardButton(text='Механика', callback_data='meh')
        keyboard.add(key_meh)
        key_zsm = types.InlineKeyboardButton(text='Законы сохранения в механике', callback_data='zsm')
        keyboard.add(key_zsm)
        key_kv = types.InlineKeyboardButton(text='Колебания и волны', callback_data='kv')
        keyboard.add(key_kv)
        key_mpty = types.InlineKeyboardButton(text='Молекулярная физика. Тепловые явления', callback_data='mpty')
        keyboard.add(key_mpty)
        key_gs = types.InlineKeyboardButton(text='Гидростатика', callback_data='gs')
        keyboard.add(key_gs)
        key_el = types.InlineKeyboardButton(text='Электродинамика', callback_data='el')
        keyboard.add(key_el)
        key_opt = types.InlineKeyboardButton(text='Оптика', callback_data='opt')
        keyboard.add(key_opt)
        key_kp = types.InlineKeyboardButton(text='Квантовая физика', callback_data='kp')
        keyboard.add(key_kp)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'meh':
        keyboard = types.InlineKeyboardMarkup()
        key_knm = types.InlineKeyboardButton(text='Кинематика', callback_data='knm')
        keyboard.add(key_knm)
        key_dnm = types.InlineKeyboardButton(text='Динамика', callback_data='dnm')
        keyboard.add(key_dnm)
        key_stt = types.InlineKeyboardButton(text='Статика', callback_data='stt')
        keyboard.add(key_stt)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'knm':
        bot.send_photo(call.from_user.id, photo=open('photos/Кинематика.png', 'rb'))
    elif call.data == 'dnm':
        bot.send_photo(call.from_user.id, photo=open('photos/Динамика.png', 'rb'))
    elif call.data == 'stt':
        bot.send_photo(call.from_user.id, photo=open('photos/Статика.png', 'rb'))
    elif call.data == 'zsm':
        keyboard = types.InlineKeyboardMarkup()
        key_zsi = types.InlineKeyboardButton(text='Закон сохранения импульса', callback_data='zsi')
        keyboard.add(key_zsi)
        key_zse = types.InlineKeyboardButton(text='Закон сохранения энергии', callback_data='zse')
        keyboard.add(key_zse)
        question = 'Выбери раздел:'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    elif call.data == 'zsi':
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения импульса.png', 'rb'))
    elif call.data == 'zse':
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения энергии1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Закон сохранения энергии2.png', 'rb'))
    elif call.data == 'kv':
        bot.send_photo(call.from_user.id, photo=open('photos/Колебания и волны.png', 'rb'))
    elif call.data == 'mpty':
        bot.send_photo(call.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления2.png', 'rb'))
    elif call.data == 'gs':
        bot.send_photo(call.from_user.id, photo=open('photos/Гидростатика.png', 'rb'))
    elif call.data == 'el':
        bot.send_photo(call.from_user.id, photo=open('photos/Электродинамика1.png', 'rb'))
        bot.send_photo(call.from_user.id, photo=open('photos/Электродинамика2.png', 'rb'))
    elif call.data == 'opt':
        bot.send_photo(call.from_user.id, photo=open('photos/Оптика.png', 'rb'))
    elif call.data == 'kp':
        bot.send_photo(call.from_user.id, photo=open('photos/Квантовая физика.png', 'rb'))
    #other----------------------------------------------------------------------------------------------------
    elif call.data == 'con':
        bot.send_photo(call.from_user.id, photo=open('photos/Константы.png', 'rb'))
    elif call.data == 'dp':
        bot.send_photo(call.from_user.id, photo=open('photos/Десятичные приставки.png', 'rb'))
    elif call.data == 'smre':
        bot.send_photo(call.from_user.id, photo=open('photos/Соотношение между различными единицами.png', 'rb'))
    elif call.data == 'mch':
        bot.send_photo(call.from_user.id, photo=open('photos/Масса частиц.png', 'rb'))
    elif call.data == 'pl':
        bot.send_photo(call.from_user.id, photo=open('photos/Плотность.png', 'rb'))
    elif call.data == 'ute':
        bot.send_photo(call.from_user.id, photo=open('photos/Удельная теплоемкость.png', 'rb'))
    elif call.data == 'mlm':
        bot.send_photo(call.from_user.id, photo=open('photos/Молярные массы.png', 'rb'))
    elif call.data == 'tpl':
        bot.send_photo(call.from_user.id, photo=open('photos/Плавление элементов.png', 'rb'))
    elif call.data == 'usp':
        bot.send_photo(call.from_user.id, photo=open('photos/Удельное сопротивление.png', 'rb'))
    elif call.data == 'ma':
        bot.send_photo(call.from_user.id, photo=open('photos/Масса атомов.png', 'rb'))


bot.polling(none_stop=True, interval=0)
