from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Union

CHANNELS = ['-1001786056810',]

async def check(user_id, channel: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    return member.is_chat_member()



check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
    ]]
)