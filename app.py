from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    print(__name__)  # I add two more lines here
    print("ok")
    app.run(debug=True, host="0.0.0.0")
