import logging
from aiogram import Bot, Dispatcher, executor, types
from subscribe import CHANNELS, check, check_button
API_TOKEN = '5329247960:AAGxnZEHH6Wbv9hRuSfCnPZdrkuFyNHFj4c' #'2109989557:AAENUnDFz40vdLAZlITxH8Vjpa9uWlm_caM'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """    This handler will be called when user sends `/start` or `/help` command
    """
    channels = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        print(chat)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'> Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)


@dp.message_handler()
async def translator(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    from translate import translater
    await message.answer(translater(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)