from homeapp.telegrambot import start_bot
import asyncio
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Start Telegram bot"

    def handle(self, *args, **kwargs):
        asyncio.run(start_bot())
