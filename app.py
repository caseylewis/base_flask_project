from flask import Flask, render_template, request  # , redirect, url_for, jsonify

# FLASK APP
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/first_page')
def first_page():
    return render_template('first_page.html')


@app.route('/second_page')
def second_page():
    return render_template('second_page.html')


if __name__ == '__main__':
    # HOST OPTIONS
    localhost = '0.0.0.0'

    host = localhost
    app.run(host=host, debug=True)
    # app.run(debug=True)
