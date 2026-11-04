from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signin")
def login():
    return render_template("login3_get.html")

@app.route("/verify")
def verify():
    uname = request.args["uname"]
    pwd = request.args["pwd"]
    if uname == "Amisha" and pwd == "123":
        return "Login Successful"
    else: 
        return "Login Failed"


@app.route("/signup")
def register():
    return "I am register method"

if __name__ == "__main__":
    app.run(debug = True)                           # Start the server