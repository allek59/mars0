from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def root():
    return "<h2>Миссия Колонизация Марса</h2>"


@app.route('/index')
def index():
    return "<h2>И на Марсе будут яблони цвести!</h2>"


@app.route('/promotion')
def promotion():
    return """<h2>Человечество вырастает из детства.</h2>
    <h2>Человечеству мала одна планета.</h2>
    <h2>Мы сделаем обитаемыми безжизненные пока планеты.</h2>
    <h2>И начнем с Марса!</h2>
    <h2>Присоединяйся!</h2>"""


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='png/mars.jpg')}"
                    alt="здесь должна была быть картинка но вышли технические шоколадки">
                    <h2>На Марсе классно</h2>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>На Марсе классно!</title>
                      </head>
                      <body>
                        <h1>На Марсе классно!</h1>
                        <img src="{url_for('static', filename='png/mars2.jpg')}"
                    alt="здесь должна была быть картинка, но вышли технические шоколадки">
                        <div class="alert alert-success" role="alert">
                          На Марсе классно — красные пески, крутые горы и кратеры
                          Безумно красивые каналы рядом с экватором
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Ничто не сравнится с тамошними закатами
                          Правда, холодновато и давление, мягко говоря, низковатое
                        </div>
                        <div class="alert alert-dark" role="alert">
                          Зато две луны на небе и очень яркие звёзды
                          Это из-за низкой плотности воздуха, жаль, что так поздно
                          Земляне получили снимки с этой прекрасной планеты
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Тут было ещё прикольнее до местного конца света
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
