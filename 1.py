from flask import Flask

app = Flask(__name__)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <p><img src="static/images/mars.jpg" alt="картинка Марса :З"></p>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
