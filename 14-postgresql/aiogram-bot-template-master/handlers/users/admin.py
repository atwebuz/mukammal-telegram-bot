import asyncio
from aiogram import types

from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(text='/reklama', user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text='reklama')
        await asyncio.sleep(0.05)
