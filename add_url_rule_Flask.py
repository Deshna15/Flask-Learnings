from flask import Flask

app = Flask(__name__)


def helloworld():
    return "Hello World"


if __name__ == '__main__':
    app.add_url_rule('/', 'hello', helloworld)
    # Default 127.0.0.1:5000
    app.run()
