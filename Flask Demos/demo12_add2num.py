from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/displayNames")
def displayNames():
    firstname = "Amisha"
    secondname = "Daf"
    return render_template("login7.html", firstname = firstname, secondname = secondname)

@app.route("/displayList")
def displayList():
    data = ['Amisha', "Vedika", "Gauri", "Shruti", "Piyu"]
    return render_template("login9.html", data = data)

@app.route("/displayNestedList")
def displayNestedList():
    data = [[101, "Amisha", 90], [102, "Vedika", 90], [103, "Gauri", 85], [104, "Shruti", 87], [105, "Piyu", 95]]
    return render_template("login10.html", data = data)

@app.route("/displayDict")
def displayDict():
    data = {101:['Amisha', 90], 102:['Vedika', 91], 103:['Gauri', 92]}
    return render_template("login11.html", data = data)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login5_getpost.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        if uname == "Amisha" and pwd == "123":
            return "Login Successful"
        else: 
            return "Login Failed"

@app.route("/sum", methods = ["GET", "POST"])
def getSum():
    if request.method == "GET":
        return render_template("login12.html")
    else:
        num1 = int(request.form["num1"])
        num2 = int(request.form["num1"])
        result = num1 + num2
        return render_template()



if __name__ == "__main__":
    app.run(debug = True)                           # Start the server