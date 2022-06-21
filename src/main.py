from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from os import environ, path
from asyncio import run

bot = AsyncTeleBot(environ.get("TOKEN"), parse_mode=None)

sticker = open(path.join("assets/") + "hi_sticker.webp", "rb")

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
    await bot.send_sticker(message.chat.id, sticker)
    await bot.send_message(
        message.chat.id,
        "*Пр-р-ривет!*\n\n"
        + "Я - попугай *Кеша*. Я *повторяю* за *тобой* *все* сообщения! *Кар-р!*",
        parse_mode="Markdown",
    )


@bot.message_handler(content_types=["text"])
async def echo_text(message: Message):
    await bot.send_message(
        message.chat.id, "_" + message.text.strip("_*") + "_", parse_mode="Markdown"
    )


@bot.message_handler(content_types=["sticker"])
async def echo_sticker(message: Message):
    await bot.send_message(
        message.chat.id, "*Кр-р-рутой стикер-р!*", parse_mode="Markdown"
    )


@bot.message_handler(content_types=["animation", "photo", "video", "video_note"])
async def echo_video(message: Message):
    await bot.send_message(
        message.chat.id, "*Выглядит кр-р-руто!*", parse_mode="Markdown"
    )


@bot.message_handler(content_types=["audio", "voice"])
async def echo_audio(message: Message):
    await bot.send_message(
        message.chat.id, "*Звучит невер-р-роятно!*", parse_mode="Markdown"
    )


@bot.message_handler(content_types=["pinned_message"])
async def echo_pinned(message: Message):
    await bot.send_message(message.chat.id, "*Кар-р-р!*", parse_mode="Markdown")


@bot.message_handler(content_types=["new_chat_members"])
async def echo_new_chat_members(message: Message):
    reply_text = "*Пр-р-ривет"
    if len(message.new_chat_members) == 1:
        reply_text += f", _{message.new_chat_members[0].first_name}_!*"
    else:
        reply_text += " _всем_!*"
    await bot.send_message(
        message.chat.id,
        reply_text,
        parse_mode="Markdown",
    )


@bot.message_handler(content_types=all_content_types)
async def echo_all(message: Message):
    await bot.send_message(message.chat.id, "*Кар-р-р!*", parse_mode="Markdown")


run(bot.infinity_polling(allowed_updates=["message"]))
