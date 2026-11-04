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
    return render_template("login8.html", data = data)

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


if __name__ == "__main__":
    app.run(debug = True)                           # Start the server