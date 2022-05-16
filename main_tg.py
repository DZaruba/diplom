import environment_save_images as query_image

import classifier

import logging
from aiogram import Bot, Dispatcher, executor, types

from aiogram.dispatcher.filters.state import StatesGroup, State #Для подгрузки стейт-машины
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Объект бота
bot = Bot(token="1637085195:AAEhKwIRLz4UiDFrt6K8bf1xBs2HTdesyEU")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Для активации хранилища стейт-машины
dp = Dispatcher(bot, storage=MemoryStorage())
#Тело бота

@dp.message_handler(commands=['temp'], state=None)
async def create_st0_command(message: types.Message):
    #await message.answer('Операция в процессе') #Отправляем сообщение
    await message.answer('Температура окружающей среды у рабочего №1') #Отправляем сообщение
    await bot.send_photo(chat_id = message.chat.id, photo = query_image.cr_image())

@dp.message_handler(commands=['condition'], state=None)
async def create_st0_command(message: types.Message):
    await message.answer(classifier.class_acc_z()) #Отправляем сообщение

#Конец тела бота
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)