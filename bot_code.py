from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo
import webbrowser, sqlite3, telebot
platform = ''


bot = Bot("7381967574:AAG5AFZjoYqJOml34yQKLE9boCSH96Y1ALM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    connect = sqlite3.connect("Date_User.sql")
    curs = connect.cursor(connect)
    
    curs.execute("CREATE TABLE IF NOT EXISTS Users (id int primary key, platform TEXT NOT NULL, login TEXT NOT NULL, pass TEXT NOT NULL)")
    
    connect.commit()
    connect.close()
    
    await message.answer("Здравствуйте! Вот команды для пользования этим ботом:\n/start - Запуск бота\n/socials - Открыть меню пользования соц-сетями\n/datebase - Зарегистрироваться в базе данных бота")

@dp.message_handler(commands=['socials'])
async def start_cmd(message: types.Message):
    markup_inl = types.InlineKeyboardMarkup() 
    markup_rpl = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    
    yt = types.InlineKeyboardButton("YouTube", url="https://www.youtube.com/")
    tg = types.InlineKeyboardButton("Telegram", url="https://web.telegram.org/a/")
    vk = types.InlineKeyboardButton("VKontakte", url="https://vk.com/feed") 
    
    markup_inl.row(yt, tg)
    markup_inl.row(vk)
       
    ytt = types.KeyboardButton("YouTube", web_app=WebAppInfo(url='https://www.youtube.com/'))
    tgg = types.KeyboardButton("Telegram", web_app=WebAppInfo(url='https://web.telegram.org/a/'))
    vkk = types.KeyboardButton("VK", web_app=WebAppInfo(url='https://vk.com/feed'))
    
    markup_rpl.row(ytt, tgg)
    markup_rpl.row(vkk)
    
    await message.reply("Вот список соц-сетей. Нажмите на кнопку, чтобы перейти.", reply_markup=markup_inl)
    await message.answer("Также вы можете открыть прилжение соц-сети прямо здесь.", reply_markup=markup_rpl)
    
@dp.message_handler(commands=['datebase'])
async def db(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    
    markup.add(types.InlineKeyboardButton("Зарегистрироваться", callback_data='db'))
    
    await message.answer("Вы можете вписать пароль для какой-то платформы.", reply_markup=markup)

@dp.callback_query_handler()
async def db(call):
    if call.data == 'db':
        await call.message.reply("Вы начали процесс регистрации. Напишите <B>платформу</B>, для которой хотите создать пароль.", parse_mode ='HTML')
        dp.register_message_handler(next_step)
        
#@dp.message_handler(content_types=['text'])
#async def next_step(message: types.Message):
    #platform = message.text#
    #await message.answer(platform)


executor.start_polling(dp)