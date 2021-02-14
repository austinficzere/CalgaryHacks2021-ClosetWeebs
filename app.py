from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route("/login", methods = ['POST','GET'])
def login():
    return render_template('login.html')

@app.route("/createAccount", methods = ['POST','GET'])
def createAccount():
    return render_template('createAccount.html')

if __name__ == "__main__":
    app.run(debug=True)