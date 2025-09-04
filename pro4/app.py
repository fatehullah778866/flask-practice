from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",name="Fateh", age=21)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    email = "fatehullah.dev@gmail.com"
    return render_template("contact.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)
