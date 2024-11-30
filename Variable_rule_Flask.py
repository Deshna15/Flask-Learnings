from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def helloworld(name):
    return "Hello {}".format(name)


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
