from flask import Flask, render_template, requests

app = Flask(__name__, template_folder='template')

@app.route("/", methods = ['POST','GET'])

def index():
    if requests.method == 'POST':
        pass
    else:   
        return render_template('')

if __name__ == "__main__":
    app.run(debug=True)