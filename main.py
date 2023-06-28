from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_html_cintent(self):
        return """
        <!doctype html>
<!-- Корень документа -->
<html lang="en">
<!-- Информация для браузера -->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <!-- Заголовок страницы -->
    <title>Окошко</title>
</head>
<body>
<nav class="navbar navbar-light bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <div class="col-sm-12">
                <h2 class="text-white">Меню
                    <div class="btn-group" role="group" aria-label="Basic outlined example">
                        <button type="button" class="btn btn-outline-primary">Главная</button>
                        <button type="button" class="btn btn-outline-primary">Категории</button>
                        <button type="button" class="btn btn-outline-primary">Заказы</button>
                        <button type="button" class="btn btn-outline-primary">Контакты</button>
                    </div>
                </h2>
            </div>
        </a>
    </div>
</nav>
<div class="container-fluid">
    <h1 align="center">Контакты</h1>
    <div class="col-2 ml-auto mr-3 bg-white" style="height: 5px;"></div>

    <div class="col-2 ml-auto mr-3 bg-white" style="height: 25px;"></div>
    <div align="center" class="row mt-5">
        <div class="col-sm-6">
            <div class="card text-center" style="width: 30rem;">
                <div class="mb-3">
                    <label for="formGroupExampleInput" class="form-label">Сообщение</label>
                    <input type="text" class="form-control" id="formGroupExampleInput"
                           placeholder="Example input placeholder">
                </div>
                <form class="row gx-3 gy-2 align-items-center">
  <div class="col-sm-3">
    <label class="visually-hidden" for="specificSizeInputName">Name</label>
    <input type="text" class="form-control" id="specificSizeInputName" placeholder="Username">
  </div>
  <div class="col-sm-3">
    <label class="visually-hidden" for="specificSizeInputGroupUsername">Имя</label>
    <div class="input-group">
      <div class="input-group-text">@</div>
      <input type="text" class="form-control" id="specificSizeInputGroupUsername" placeholder="E-mail">
    </div>
  </div>


  <div class="col-auto">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="autoSizingCheck2">
      <label class="form-check-label" for="autoSizingCheck2">
        Remember me
      </label>
    </div>
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>
            </div>
        </div>
        <div class="col-6">
            <div class="card text-center" style="width: 30rem;">
                <div class="card-body">
                    <h3>Наши контакты</h3>
                    <div class="card-body mx-auto">

                        <p class="card-text">Здесь Вы можете оставить Ваши контакты. Мы обязательно с Вами свяжемся!:)
                        всего за 200%</p>

                    </div>
                </div>
            </div>
        </div>


    </div>
</div>

</body>
</html>
        """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_cintent()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
