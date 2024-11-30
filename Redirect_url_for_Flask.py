from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome_user(name):
    return "Welcome {}".format(name)


@app.route('/hello/<name>')
def helloworld(name):
    return redirect(url_for("welcome_user", name=name))


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
