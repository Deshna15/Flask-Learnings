from flask import Flask, redirect, url_for, request,abort

app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome_user(name):
    return "Welcome {}".format(name)


@app.route('/login', methods=["Post"])
def login():
    if request.method == "POST":
        if request.form["nm"] =="admin":
            name = request.form["nm"]
            return redirect(url_for("welcome_user", name=name))
        else:
            abort(401)



if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
