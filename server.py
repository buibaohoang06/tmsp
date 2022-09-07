from flask import Flask, render_template, request
import json

def gatherData(username):
	with open('example.json', 'r') as data:
		pfp = json.loads(data.read())["users"][username]["profile_pic"]
	return pfp

app = Flask(__name__)

@app.get("/")
def main_page():
	return render_template('home.html', username="admin")
@app.get("/account")
def account_page():
	pfp = gatherData("admin")
	return render_template('account.html', username="admin", pfp=pfp)
app.run(debug=True, host="0.0.0.0")