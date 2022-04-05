from flask import Flask, render_template, request, json
app = Flask(__name__)

# Teraz określ katalog główny / i odpowiadającą mu funkcję obsługi żądań (request handler): 

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/addPeriod',methods=['POST'])
def addPeriod():
	# read the posted values from the UI
	dateBegin = request.form['dateBegin']
	dateEnd = request.form['dateEnd']

	# return json.dumps({'html':'request ok'})

	# validate the received values
	if dateBegin and dateEnd:
		return json.dumps({'html':dateBegin + ' - ' + dateEnd})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
	app.run()