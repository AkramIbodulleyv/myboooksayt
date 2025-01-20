import os
import django
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from .models import Botmodel
from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'myboooksayt.settings')
django.setup()

BOT_TOKEN = '7983188565:AAHO7nlZ_oUuKsso1m29rNVyk3N1Jw6YuIk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

async def delete_webhook():
    await bot.delete_webhook()

@dp.message(Command('start'))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Assalomu alaykum! Shikoyatlaringizni menga yuboring.")

@sync_to_async
def save_complaint_to_db(user_id, username, message_text):
    complaint = Botmodel.objects.create(
        user_id=user_id,
        username=username,
        message=message_text,
    )
    complaint.save()

@dp.message()
async def save_complaint(message: types.Message):
    await save_complaint_to_db(message.from_user.id, message.from_user.username, message.text)

    await message.reply("Shikoyatingiz qabul qilindi. Rahmat!")
async def start_bot():
    await delete_webhook()
    await dp.start_polling(bot)