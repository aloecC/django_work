from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    """Сервер обработки запросов от клиента"""

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        with open('contacts_page.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content, 'utf-8'))


if __name__ == "__mainn__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))