from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from os import environ
from asyncio import run

bot = AsyncTeleBot(environ.get("TOKEN"), parse_mode=None)

all_content_types = [
    "text",
    "photo",
    "video",
    "audio",
    "document",
    "sticker",
    "voice",
    "video_note",
    "contact",
    "location",
    "venue",
    "new_chat_members",
    "left_chat_member",
    "new_chat_title",
    "new_chat_photo",
    "delete_chat_photo",
    "group_chat_created",
    "supergroup_chat_created",
    "channel_chat_created",
    "migrate_to_chat_id",
    "migrate_from_chat_id",
    "pinned_message",
]


@bot.message_handler(commands=["start", "help"])
async def start(message: Message):
    await bot.send_message(
        message.chat.id,
        "*Кар-р!* *Карр-р-р!*\n\n"
        + "Я - попугай *Кеша*. Я *повторяю* за *тобой* *все* сообщения! *Кар-р!*",
        parse_mode="Markdown",
    )


@bot.message_handler(content_types=["text"])
async def echo_text(message: Message):
    await bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=["sticker"])
async def echo_sticker(message: Message):
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


@bot.message_handler(content_types=["animation"])
async def echo_gif(message: Message):
    await bot.send_animation(message.chat.id, message.animation.file_id)


@bot.message_handler(content_types=all_content_types)
async def echo_all(message: Message):
    await bot.send_message(message.chat.id, "*Кар-р-р!*", parse_mode="Markdown")


run(bot.infinity_polling())
