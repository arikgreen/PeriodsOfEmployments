import json
import datetime
from flask import Flask, render_template, request, json

app = Flask(__name__)

#------------------------------------------------------------------------------
# Teraz określ katalog główny / i odpowiadającą mu funkcję obsługi żądań (request handler): 
@app.route("/")
def main():
	return render_template('index.html')

#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------

@app.route('/countPeriods',methods=['POST'])
def countPeriods():
	if request.form:
		dateRange = json.loads(request.form['data'])
		newDateRange = []
		
		# dateRange.append([datetime.date(2014,5,3), datetime.date(2020,12,31)])
		# dateRange.append([datetime.date(1999,8,2), datetime.date(2019,12,31)])
		# dateRange.append([datetime.date(2000,3,8), datetime.date(2014,9,8)])
		# dateRange.append([datetime.date(2021,2,1), datetime.date(2021,12,31)])
		# dateRange.append([datetime.date(1996,1,2), datetime.date(1999,12,31)])

		# print(dateRange[0][0],dateRange[0][1])

		#print("Oryginal list")
		#print(dateRange)

		dateRange.sort(key=lambda t:t[0])

		#print("Sorted list")
		#print(dateRange)

		# min_start=min(dateRange, key=lambda t:t[0])[0]
		# max_end=max(dateRange, key=lambda t:t[1])[1]

		#print("Min:", min_start)
		#print("Max:", max_end)

		newDateRange.append(dateRange[0])

		for period in dateRange:
				if period[0] > newDateRange[0][1]:
						newDateRange.append(period)
				elif period[1] > newDateRange[0][1]:
						newDateRange[0][1] = period[1]

		# print("Result list")
		# print(newDateRange)
		return json.dumps({'html':newDateRange})
	else:
		return json.dumps({'error':'<span>NO periods</span>'})

#------------------------------------------------------------------------------
if __name__ == "__main__":
	# app.run()
	app.run(debug=True, use_debugger=False, use_reloader=False)