# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageCantBeDeleted
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_telegram import dp
from contextlib import suppress
from modules import main_config, createPDF
import random
from modules.txt_logic import *

@dp.message_handler(content_types=['text'])
async def get_text_messages(message: Message, state: FSMContext):
    text = message.text
    text_dict = []
    text_lines = text.split('\n')
    for i in text_lines:
        if i != '':
            text_dict.append(i)
    text_lines = text_dict
    if len(text_lines) > 5:
        await message.answer('<b>Пожалуйста, отправьте не более 5 строк текста.</b>')
    elif len(text_lines) < 1:
        await message.answer('<b>Пожалуйста, отправьте хотя бы одну строку текста.</b>')
    else:
        order_number = random.randint(100000000, 999999999)
        while order_number in read_used_order_numbers():
            order_number = random.randint(100000000, 999999999)

        pdf_path = createPDF.create_pdf(text_lines, order_number)

        with open(pdf_path, 'rb') as pdf_file:
            await message.answer_document(pdf_file)

        write_order_number(order_number)
        log_order(order_number, text_lines)