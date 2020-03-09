from flask import *

app = Flask(__name__)


@app.route('/astronaut_selection')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
