from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/calculate", methods =['POST'])
def calculate():
    # get values from the form
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    operation = request.form["operation"]
    
    #Perform calculation
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result == num1/num2
    else:
        result = "invalid operation!"
        
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
