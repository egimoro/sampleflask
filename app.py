from flask import jsonify, request, render_template, Flask

app = Flask(__name__)

@app.route('/')
def interactive():
	return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
    firstName = request.form['firstName']

    lastName = request.form['lastName']

    output = firstName + " " + lastName

    if firstName and lastName:
        return jsonify({'output':'Full Name: ' + output})
    return jsonify({'error' : 'Missing data!'})


if __name__ == "__main__":
    app.run(debug=True)
    
