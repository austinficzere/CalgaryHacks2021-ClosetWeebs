from flask import Flask, render_template, request, redirect, url_for
from person import Person
from database import Database

app = Flask(__name__)
data = Database()
mapToNum = {'sport':0,'game':1,'read':2,'code':3,'music':4, 'stock' : 5, 'movies' : 6}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        loginValidate(request.form)
    return render_template('login.html')

def loginValidate(form):
    if data.isUserPassValid(request.form['username'],request.form['pswd']):
        print("LOGINED")
    else:
        print("no")


@app.route("/createAccount", methods = ['POST','GET'])
def createAccount():
    if request.method == 'POST':
        newPerson = createPerson(request.form)
        addPerson(request.form,newPerson)
    return render_template('createAccount.html')

@app.route("/users/<name>")
def createProfile():
    render_template("profileTemplate.html",data.getPersons)


def addPerson(form,person):
    user = request.form['username']
    passw = request.form['pswd']
    data.addUser(user,passw)
    data.addPerson(user,person)
    data.closeData()


def createPerson(form):
    interest = []
    for key in mapToNum.keys():
        if key in form:
            if form[key] == 'on':
                interest.append(mapToNum[key])
    return Person(form['name'],int(form['year+']),form['major'],form['concen'],[],interest,form['descrip'],int(form['priority']))


if __name__ == "__main__":
    app.run(debug=True)