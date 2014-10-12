from flask import Flask, render_template
import json
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def readFile():
	json_data=open('nutrition.json')
	data = json.load(json_data)
	json_data.close()
	return render_template('template.html', data=data)
	
if __name__ == '__main__':
	app.debug = True
	app.run()