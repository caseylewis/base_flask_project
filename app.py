from flask import Flask, render_template, request, jsonify  # , redirect, url_for

# FLASK APP
app = Flask(__name__)

user_list_data = [
    {
        'name': 'Casey',
        'phone_number': '817-253-8694',
    },
    {
        'name': 'Natalie',
        'phone_number': '111-222-3333',
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/javascript_example')
def javascript_example():
    return render_template('javascript_example.html')


@app.route('/ajax_input_example', methods=['GET', 'POST'])
def ajax_input_example():
    return render_template('ajax_input_example.html', user_list=user_list_data)


@app.route('/add_user', methods=['POST'])
def add_user():
    # CREATE NEW USER
    user = {}
    # COPY USER FROM FORM VALUES
    for key, value in request.form.items():
        user[key] = value

    user_list_data.append(user)
    return jsonify(user_list_data)


if __name__ == '__main__':
    # HOST OPTIONS
    localhost = '0.0.0.0'

    host = localhost
    app.run(host=host, debug=True)
    # app.run(debug=True)
