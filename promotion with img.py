from flask import *

app = Flask(__name__)


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <p><img src="/static/img/mars.jpg" alt="картинка Марса :З"></p>
                    <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
                    <div class='alert alert-success' role='alert'>Человечеству мала одна планета.</div>
                    <div class='alert alert-secondary' role='alert'>
                      Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class='alert alert-warning' role='alert'>И начнем с Марса!</div>
                    <div class='alert alert-danger' role='alert'>Присоединяйся!</div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
