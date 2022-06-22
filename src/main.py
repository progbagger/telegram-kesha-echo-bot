from telebot import TeleBot
from telebot.types import Message
from os import environ, path

bot = TeleBot(environ.get("TOKEN"), parse_mode=None)

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
def start(message: Message):
    sticker = open(path.join("assets/", "hi_sticker.webp"), "rb")
    bot.send_sticker(message.chat.id, sticker)
    sticker.close()
    bot.send_message(
        message.chat.id,
        "*Пр-р-ривет!*\n\n"
        + "Я - попугай *Кеша*. Я *повторяю* за *тобой* *все* сообщения! *Кар-р!*",
        parse_mode="Markdown",
    )


@bot.message_handler(content_types=["text"])
def echo_text(message: Message):
    bot.send_message(
        message.chat.id, "_" + message.text.strip("_*") + "_", parse_mode="Markdown"
    )


@bot.message_handler(content_types=["sticker"])
def echo_sticker(message: Message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)


@bot.message_handler(content_types=["animation", "photo", "video", "video_note"])
def echo_video(message: Message):
    bot.send_message(message.chat.id, "*Выглядит кр-р-руто!*", parse_mode="Markdown")


@bot.message_handler(content_types=["audio", "voice"])
def echo_audio(message: Message):
    bot.send_message(message.chat.id, "*Звучит невер-р-роятно!*", parse_mode="Markdown")


@bot.message_handler(content_types=["pinned_message"])
def echo_pinned(message: Message):
    bot.send_message(message.chat.id, "*Закр-р-реплено!*", parse_mode="Markdown")


@bot.message_handler(content_types=["new_chat_members"])
def echo_new_chat_members(message: Message):
    reply_text = "*Пр-р-ривет"
    if len(message.new_chat_members) == 1:
        reply_text += f", _{message.new_chat_members[0].first_name}_!*"
    else:
        reply_text += " _всем_!*"
    bot.send_message(
        message.chat.id,
        reply_text,
        parse_mode="Markdown",
    )


@bot.message_handler(content_types=all_content_types)
def echo_all(message: Message):
    bot.send_message(message.chat.id, "*Кар-р-р!*", parse_mode="Markdown")


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
