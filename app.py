import os
from flask import Flask,render_template, request, json



app = Flask(__name__)


@app.route('/')
def signUp():
    return render_template('index.html')


@app.route('/process',methods= ['POST'])
def process():
    firstName = request.form.get("firstName")
    lastName = request.form.get("lastName")
    return json.dumps({"firstName":firstName,"lastName":lastName})


if __name__=="__main__":
    app.run(debug=True)
