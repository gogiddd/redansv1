from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='26724138', api_hash='cff6dfd60637abb12cde975d934a16d8')


chat_id = "@datinganon_bot"  #тут свой чат в котором спамить

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if '/stop - завершить диалог' in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Привет! Думаю ты уже слышал про Редан. ")
        sleep(2)
        await app.send_message(chat_id, """Нравится их стиль или направление? Заходи к нам в шоп и забирай свой халявный патч или футболку🖤🕷  ⬇️""")

        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEH9Jxj_3ucoq1Z3IMOAAECjOpVswABgvvmAALeKAACNbD5SzhyyqUQwyDwLgQ")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.5 )
                 await app.send_message(chat_id, "Найти собеседника 🔎")


app.run()