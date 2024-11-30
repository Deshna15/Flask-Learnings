from flask import Flask,  render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def index(name):
    return render_template("jinja.html", name=name)


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()



# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements