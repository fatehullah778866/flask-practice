from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", name="Fateh ullah")


@app.route("/aboutt")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", email="fatehullah.dev@gmail.com")


if __name__ == "__main__":
    app.run(debug=True)