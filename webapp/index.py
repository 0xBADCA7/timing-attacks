from flask import Flask, request, make_response, render_template
from hashlib import sha1
from time import sleep
import http.client

app = Flask(__name__)
_secret = '458fae127cb7b290282c8a77c7542b0d4b5fa49b'


def check_admin(password):

    counter = 0
    for i in range(len(_secret)):
        if not password[i] == _secret[i]:
            return False
        #sleep(0.1)
        counter += 1


    return True


@app.route('/')
def index():
    password = request.args.get('password', None)
    username = request.args.get('user', 'stranger')
    err = None
    is_admin = False

    if password:
        is_admin = check_admin(password)

        if is_admin:
            username = "admin"
        else:
            err = True

    response = make_response(render_template('index.html', user=username, error=err))
    response.status_code = 500 if is_admin else 500

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
