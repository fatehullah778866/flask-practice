from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    name = "Fateh ullah"
    age = 21
    return f"my name is {name} and my age is {age}!"


@app.route("/hello/<username>")
def hello(username):
    return f"Hi {username} welcome to Flask!"


@app.route("/square/<int:number>")
def square(number):
    result = number * number
    return f"square of {number} is {result} "


if __name__ == "__main__":
    app.run(debug=True)

