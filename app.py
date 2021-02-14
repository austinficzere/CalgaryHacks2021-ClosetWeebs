from flask import Flask, render_template, request, redirect, url_for
from person import Person
from database import Database

app = Flask(__name__)
data = Database()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        loginValidate(request.form)
    return render_template('login.html')

def loginValidate(form):
    pass


@app.route("/createAccount", methods = ['POST','GET'])
def createAccount():
    if request.method == 'POST':
        newPerson = createPerson(request.form)
    return render_template('createAccount.html')


def addPerson(form):
    #check if person exists
    # add to database
    pass


def createPerson():
    # create the person
    pass

if __name__ == "__main__":
    app.run(debug=True)