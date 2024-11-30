from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def helloworld():
#     return "Hello World"

@app.route('/hello')
def helloworld():
    return "Hello World"


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
    # app.run(host="0.0.0.0", port=60000, debug=True)
