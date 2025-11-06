
def do_GET(self):
    """ Метод для обработки входящих GET-запросов """

    self.send_response(200)  # Отправка кода ответа
    self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
    self.end_headers()  # Завершение формирования заголовков ответа
    with open('contacts_page.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    self.wfile.write(bytes(html_content, 'utf-8'))