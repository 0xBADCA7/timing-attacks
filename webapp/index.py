from flask import Flask, request, make_response, render_template
import sqlite3

from hashlib import sha1
from time import sleep

app = Flask(__name__)
_secret = 'fad08d06495532c3ae5db5209834956b0114da77'


def type1_check(password):
    """
    Type 1 vulnerable code.
    Check password string byte-by-byte against a predefined value
    :param password: User-supplied user name
    :return: True if matched all bytes correctly, False otherwise
    """
    counter = 0
    for i in range(len(_secret)):
        if not password[i] == _secret[i]:
            return False
        # Introduce sleep(0.1) here to run the most basic test (easily seen)
        #sleep(0.1)
        counter += 1

    return True


def get_hash_from_db(username):
    """
    Get a hash of password from the DB by user name
    :param username: User-supplied user name
    :return: Hash of the password if user name found or None otherwise
    """
    candidate = None

    try:
        conn = sqlite3.connect('/tmp/sample.db')
        c = conn.cursor()
        c.execute('''SELECT password FROM users WHERE username = ? ''', (username,))
        candidate = c.fetchone()[0]
        conn.close()
    except Exception as e:
        print("Couldn't fetch data from the SQLite database file")
        print(e)

    return candidate


def type2_check(username, password):
    """
    Type 2 vulnerable code.
    Uses database connectivity for additional natural latency.
    :param username: User-supplied user name
    :param password: User-supplied password
    :return: True if password is correct and user exists otherwise False
    """
    hash_from_db = get_hash_from_db(username)

    if hash_from_db:
        test_hash = sha1(password.encode('utf8')).hexdigest()
        if test_hash == hash_from_db:
            print("Correct password")
            return True

    return False


@app.route('/')
def index():
    password = request.args.get('password', None)
    username = request.args.get('user', 'stranger')
    err = None
    is_admin = False

    if password:
        # Replace type1_check with other types to
        # play with various workloads
        is_admin = type2_check(username, password)

        if is_admin:
            username = 'admin'
        else:
            username = 'stranger'
            err = True

    response = make_response(render_template('index.html', user=username, error=err))
    response.status_code = 500 if is_admin else 500

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
