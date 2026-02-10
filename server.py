

import http.server
import socketserver
import os

# Указываем путь к вашей папке
DIRECTORY = "/storage/emulated/0/Documents/05._Python_server./"
PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Устанавливаем рабочую директорию для сервера
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
        print(f"Папка {DIRECTORY} была создана.")

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Сервер запущен! Папка: {DIRECTORY}")
        print(f"Локальный адрес: http://localhost:{PORT}")
        print("Теперь запустите ngrok, чтобы открыть доступ из интернета.")
        httpd.serve_forever()

# Реализация вашей команды "сайт"
command = input("Введите команду: ").strip().lower()
if command == "сайт":
    start_server()
else:
    print("Неверная команда. Введите 'сайт'.")





