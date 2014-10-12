from flask import Flask, render_template, request
import json
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def readFile():
	json_data=open('nutrition.json')
	data = json.load(json_data)
	json_data.close()
	return render_template('template.html', data=data)

@app.route("/submit", methods=["POST"])
def calculate():
	total = 0
	req = request.form
	for calories in req.keys():
		for quantity in req.getlist(calories):
			total += int(calories)*int(quantity)

	return str(total)
	
if __name__ == '__main__':
	app.debug = True
	app.run()