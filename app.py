from flask import Flask, render_template, request, redirect, url_for,make_response
from person import Person
from database import Database
from match import Match

app = Flask(__name__)
data = Database()
mapToNum = {'sport':0,'game':1,'read':2,'code':3,'music':4, 'stock' : 5, 'movies' : 6}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        if loginValidate(request.form):
             resp = make_response(redirect('/MainPage'))
             resp.set_cookie('username', request.form['username'])
             return resp
    return render_template('login.html')

@app.route("/MainPage")
def mainPage():
    user = request.cookies.get('username')
    print(data.readUser(user).toString())
    return render_template("MatchPage.html")

def loginValidate(form):
    if data.isUserPassValid(request.form['username'],request.form['pswd']):
        return True
    else:
        return False

@app.route("/matches")
def matches():
    user = request.cookies.get('username')
    mm = Match(data.readUser(user),data.getPersons())
    topMatches = mm.match()
    return render_template("matches.html", matches = topMatches)


@app.route("/createAccount", methods = ['POST','GET'])
def createAccount():
    if request.method == 'POST':
        newPerson = createPerson(request.form)
        addPerson(request.form,newPerson)
        resp = make_response(redirect('/MainPage'))
        resp.set_cookie('username', request.form['username'])
        return resp
    return render_template('createAccount.html')

@app.route("/users/<user>")
def createProfile(user = None):
    print(user)
    print(data.readUser(user))
    return render_template("profileTemplate.html",user = data.readUser(user))

@app.route("/editProfile.html")
def editProfile(user = None):
    return render_template("editProfile.html", user = data.readUser(user))

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