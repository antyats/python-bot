import random
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio
import aioschedule
from telebot.async_telebot import AsyncTeleBot

API_TOKEN = '5848918037:AAG25vdzTrdvtD9G_yI96nQJ-6DisU7wzPk'
bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
async def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Камень, ножницы, бумага")
    item2 = types.KeyboardButton("Орел или решка")
    item3 = types.KeyboardButton("Таймер")
    item4 = types.KeyboardButton("Загадать число")
    item5 = types.KeyboardButton("Картинка дня")
    markup.add(item1, item2, item3, item4, item5)

    await bot.send_message(message.chat.id,
                           'Привет, {0.first_name}!\n''Я — <b>Название</b>\n''Выбирай режим и играй\n'.format(
                               message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
async def questions(message):
    # 1 - камень; 2 - ножницы; 3 - бумага
    if message.text == "Камень, ножницы, бумага":
        await bot.send_message(message.chat.id, "Я выбрал штуку - теперь твоя очередь")
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Камень", callback_data='Камень')
        item2 = types.InlineKeyboardButton("Ножницы", callback_data='Ножницы')
        item3 = types.InlineKeyboardButton("Бумага", callback_data='Бумага')
        markup.add(item1, item2, item3)
        await bot.send_message(message.chat.id, "Я выбираю", reply_markup=markup)
    elif message.text == "Орел или решка":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Орел", callback_data='Орел')
        item2 = types.InlineKeyboardButton("Решка", callback_data='Решка')
        markup.add(item1, item2)
        await bot.send_message(message.chat.id, "На что ставишь?", reply_markup=markup)
    elif message.text == "Таймер":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("10 секунд", callback_data='10 секунд')
        item2 = types.InlineKeyboardButton("20 секунд", callback_data='20 секунд')
        item3 = types.InlineKeyboardButton("30 секунд", callback_data='30 секунд')
        markup.add(item1, item2, item3)
        await bot.send_message(message.chat.id, "На сколько поставить?", reply_markup=markup)
    elif message.text == "Загадать число":
        await bot.send_message(message.chat.id, f'Твое случайное число: {random.randint(0, 10)}')
    elif message.text == "Картинка дня":
        parrots = {1: 'https://cindygurmann.files.wordpress.com/2018/06/ea2530ad-e913-4d5b-8036-762b5b227c04.jpeg',
                   2: 'https://cherepah.ru/wp-content/uploads/2/2/8/228937ec782b8755993a3241e1d6c039.jpeg',
                   3: 'https://kotsobaka.com/wp-content/uploads/2018/08/2748131046_8a253489b5_b.jpg',
                   4: 'https://bestpopugai.ru/wp-content/uploads/2022/05/1-5.jpg',
                   5: 'https://i.artfile.ru/1920x1200_952300_[www.ArtFile.ru].jpg',
                   6: 'https://s1.1zoom.ru/big0/612/Parrots_Birds_Ara_(genus)_Hyacinth_macaw_Blue_570002_1280x853.jpg'}
        r = random.randint(1, 6)
        await bot.send_photo(message.chat.id, parrots[r])

async def beep(chat_id):
    await bot.send_message(chat_id, text='Время вышло!')
    aioschedule.clear(chat_id)
    return aioschedule.CancelJob

@bot.callback_query_handler(func=lambda call: True)
async def callback_inline(call):
    if call.message:
        cmci = call.message.chat.id
        if call.data == "Камень":
            bot_choice = random.randint(0, 3)
            await bot.send_message(call.message.chat.id, f'{bot_choice}')
            if bot_choice == 1:
                await bot.send_message(call.message.chat.id, "Ничья, у меня камень")
            elif bot_choice == 2:
                await bot.send_message(call.message.chat.id, "Я проиграл, у меня ножницы")
            elif bot_choice == 3:
                await bot.send_message(call.message.chat.id, "Я выиграл, у меня бумага")
        elif call.data == "Бумага":
            bot_choice = random.randint(0, 3)
            await bot.send_message(call.message.chat.id, f'{bot_choice}')
            if bot_choice == 1:
                await bot.send_message(call.message.chat.id, "Я проиграл, у меня камень")
            elif bot_choice == 2:
                await bot.send_message(call.message.chat.id, "Я проиграл, у меня ножницы")
            elif bot_choice == 3:
                await bot.send_message(call.message.chat.id, "Ничья, у меня бумага")
        elif call.data == "Ножницы":
            bot_choice = random.randint(0, 3)
            await bot.send_message(call.message.chat.id, f'{bot_choice}')
            if bot_choice == 1:
                await bot.send_message(call.message.chat.id, "Я выиграл, у меня камень")
            elif bot_choice == 2:
                await bot.send_message(call.message.chat.id, "Ничья, у меня ножницы")
            elif bot_choice == 3:
                await bot.send_message(call.message.chat.id, "Проиграл, у меня бумага")
        elif call.data == "Орел":
            bot_choice = random.randint(0, 1)
            if bot_choice == 0:
                await bot.send_message(call.message.chat.id, "Хорош, угадал")
            elif bot_choice == 1:
                await bot.send_message(call.message.chat.id, "Плох, не угадал")
        elif call.data == "Решка":
            bot_choice = random.randint(0, 1)
            if bot_choice == 1:
                await bot.send_message(call.message.chat.id, "Хорош, угадал")
            elif bot_choice == 0:
                await bot.send_message(call.message.chat.id, "Плох, не угадал")
        elif call.data == "10 секунд":
            await bot.send_message(call.message.chat.id, "Запустил таймер")
            aioschedule.every(10).seconds.do(beep, call.message.chat.id).tag(call.message.chat.id)
        elif call.data == "20 секунд":
            aioschedule.every(20).seconds.do(beep, call.message.chat.id).tag(call.message.chat.id)
        elif call.data == "30 секунд":
            aioschedule.every(30).seconds.do(beep, call.message.chat.id).tag(call.message.chat.id)

async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())
