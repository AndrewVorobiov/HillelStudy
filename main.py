from flask import Flask, request

from utils import generate_password

app = Flask('MyFirstApp')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test/')
def test():
    return 'TEST FUNC'


# validators.py
# def validate_integer(value, min_length=10, max_length=100) -> bool:
#     return True or False


@app.route('/gen-pass/')
def gen_pass():  # length = 20
    query_params = request.args

    # length: str = query_params.get('length', '') or '10'
    length = query_params.get('length') or ''
    default_password_length = 10
    minimum_password_length = 10
    maximum_password_length = 200

    if length.isdigit():
        length = int(length)
        if length > maximum_password_length or length < minimum_password_length:
            length = default_password_length

    else:
        length = default_password_length

    return generate_password(length)


if __name__ == '__main__':
    app.run(port='5000')

"""
http://127.0.0.1:5000/gen-pass/?length=20&name=Dima
http://  127.0.0.1  :5000  /  ?key=value
1           2          3   4  5
1 - protocol (http, https, ftp, smtp)
2 - server identify, IPv4 (23.48.3.1), IPv6 (), socket file
    IPv4
    0-255.0-255.0-255.0-255
    correct
    3.5.127.48
    254.254.0.0

    wrong
    256.0.0.3
    1.4.127
    1.4.127.0.1

    special ipv4 address
    127.0.0.1 - localhost
3 - port
    0 - 65353  - 2 ** 16
    0 - root

    #
    80 - http
    443 - https
    5432 - postgres
    #
4 - path
    / - hello_world()
    /test/ - test()
5 - query parameters
   start with ?
   key - value pair

stop app in terminal - Ctrl + C
ыыыыыыыыы
"""
