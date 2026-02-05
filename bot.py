import os
import http.server
import socketserver
import threading
import telebot

# 1. Запуск веб-сервера для Render (чтобы не выключал бот)
def run_dummy_server():
    handler = http.server.SimpleHTTPRequestHandler
    # Используем порт, который дает Render, или 8080 по умолчанию
    port = int(os.environ.get("PORT", 8080))
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# 2. Настройка бота
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    text = """Нужны деньги? Просто записывай видео-отзывы! 
Покупаем твои кружочки и интервью. Дорого. Постоянно. Стабильно.

Для старта сотрудничества нужно выполнить тестовое задание:

Запиши кружок на 5 сек: «Привет, хочу делать отзывы и получать деньги».

👉 Скидывай сюда: @movsienkoivhr"""
    
    bot.send_message(message.chat.id, text)

# 3. Запуск основного цикла
if __name__ == '__main__':
    print("Бот успешно запущен в облаке!")
    bot.infinity_polling()
