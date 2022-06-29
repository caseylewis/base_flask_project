from flask import Flask, render_template, request, jsonify  # , redirect, url_for

from Libs.DataLib.json_helper import *
from Libs.OSLib.os_helper import *

# FLASK APP
app = Flask(__name__)

# APP DATA - TAKEN FROM YAML FILE
app_config = get_yaml_config(os.path.join(os.getcwd(), "docker-compose.yml"))

# NAME CONSTANTS
BASE_TITLE = app_config['app_title']
APP_NAME = app_config['app_name']

app_data = StandardAppDirStruct(os.getcwd(), APP_NAME)
# JSON
users_json = JsonManager(os.path.join(app_data.data_dir, 'users.json'))
user_list_data = users_json.import_data()

# user_list_data = [
#     {
#         'name': 'Casey',
#         'phone_number': '817-253-8694',
#     },
#     {
#         'name': 'Natalie',
#         'phone_number': '111-222-3333',
#     }
# ]


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title=f"{BASE_TITLE} - Home")


@app.route('/javascript_example')
def javascript_example():
    return render_template('javascript_example.html', title=f"{BASE_TITLE} - Javascript")


@app.route('/ajax_input_example', methods=['GET', 'POST'])
def ajax_input_example():
    load_user_list_data()
    return render_template('ajax_input_example.html', title=f"{BASE_TITLE} - Ajax", user_list=user_list_data)


@app.route('/add_user', methods=['POST'])
def add_user():
    # CREATE NEW USER
    user = {}
    # COPY USER FROM FORM VALUES
    for key, value in request.form.items():
        user[key] = value

    user_list_data.append(user)
    save_user_list_data()
    return jsonify(user_list_data)


def save_user_list_data():
    users_json.export_data(user_list_data)


def load_user_list_data():
    global user_list_data
    user_list_data = users_json.import_data()


if __name__ == '__main__':
    # HOST OPTIONS
    localhost = '0.0.0.0'

    host = localhost
    app.run(host=host, debug=True)
    # app.run(debug=True)
