from aiogram import types, executor, Dispatcher, Bot
from aiogram.dispatcher import filters
import game
import configs


TOKEN = configs.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(filters.IDFilter(user_id=737483058), commands='start')
async def send_keyboard(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Показать стамину', 'Запустить бои', 'Собрать SKILL', 'Перевести SKILL на мейн', 'Собрать XP',
               'Показать баланс']
    keyboard.add(*buttons)
    await message.answer('Выберите команду:', reply_markup=keyboard)

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Показать баланс')
async def check_balance(message: types.Message):
    for confg in configs.conf:
        keyboard_balance = types.InlineKeyboardMarkup(row_width=1)
        main_address = confg.split(';')[0]
        keyboard_balance.add(types.InlineKeyboardButton(text=f'{game.check_bnb_balance(main_address)} BNB',
                                                        callback_data=main_address))
        await message.answer(text=main_address, reply_markup=keyboard_balance)

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Показать стамину')
async def check_char_stamina(message: types.Message):
    for confg in configs.conf:
        keyboard_stamina = types.InlineKeyboardMarkup(row_width=4)
        main_address = confg.split(';')[0]
        all_chars = game.character(main_address)
        buttons_stamina = []
        for char in all_chars:
            character = game.call_char(char)
            buttons_stamina.append(types.InlineKeyboardButton(text=f'{character["stamina"]}',
                                                              callback_data=character["id"]))
        keyboard_stamina.add(*buttons_stamina)
        await message.answer('Стамина на адресе: ' + main_address, reply_markup=keyboard_stamina)

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Запустить бои')
async def fight(message: types.Message):
    for confg in configs.conf:
        keyboard_fight = types.InlineKeyboardMarkup(row_width=2)
        main_address = confg.split(';')[0]
        private_key = confg.split(';')[1]
        all_chars = game.character(main_address)
        all_weapons = game.weapons(main_address)
        for allw in all_weapons:
            try:
                weapon = game.call_weapon(allw)
                if type(weapon) == dict:
                    break
            except Exception:
                pass
        buttons_fight = []
        for char in game.get_winner_chance(all_chars, weapon['id']):  # weapon['id']
            buttons_fight.append(types.InlineKeyboardButton(text=game.call_figth(char['charId'], char['weaponId'],
                                                                                 char['targetEnemy'],
                                                                                 char['winChance'],
                                                                                 main_address, private_key),
                                                            callback_data=char['charId']))
        keyboard_fight.add(*buttons_fight)
        await message.answer(main_address, reply_markup=keyboard_fight)
    await message.answer(text='Закончил бои')

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Собрать SKILL')
async def get_skill_rewards(message: types.Message):
    for confg in configs.conf:
        main_address = confg.split(';')[0]
        private_key = confg.split(';')[1]
        await message.answer(text=game.claim_rewards(main_address, private_key))

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Перевести SKILL на мейн')
async def send_skill_to_main(message: types.Message):
    for confg in configs.conf:
        main_address = confg.split(';')[0]
        private_key = confg.split(';')[1]
        main = configs.address
        skill_balance = game.check_skill_balance(main_address)
        await message.answer(text=game.transfer(main_address, private_key, skill_balance, main))

@dp.message_handler(filters.IDFilter(user_id=737483058), lambda message: message.text == 'Собрать XP')
async def get_xp_rewards(message: types.Message):
    for confg in configs.conf:
        main_address = confg.split(';')[0]
        private_key = confg.split(';')[1]
        await message.answer(text=game.claim_xp_chars(main_address, private_key))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
