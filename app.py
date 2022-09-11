from flask import Flask,redirect
import json
import urllib

app = Flask(__name__)

@app.route("/")
def index():
	return "Yooooooooooo"

@app.route("/rai1")
def rai1():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=2606803&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)


@app.route("/rai2")
def rai2():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=308718&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/rai3")
def rai3():
	with urllib.request.urlopen("https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=308709&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/rai4")
def rai4():
	with urllib.request.urlopen("https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746966&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/rai5")
def rai5():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=395276&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raimovie")
def raimovie():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=747002&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raipremium")
def raipremium():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746992&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raigulp")
def raigulp():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746953&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raiyoyo")
def raiyoyo():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746899&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/rainews")
def rainews():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=1&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raistoria")
def raistoria():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746990&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raiscuola")
def raiscuola():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=747011&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)

@app.route("/raisport")
def raisport():
	with urllib.request.urlopen("http://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=358025&output=62") as url:
		aa = json.load(url)
		aaa = str(aa["video"])
		myString = aaa.replace("['","")
		myString2 = myString.replace("']","")
		return redirect(myString2)


if __name__ == "__main__":
	app.run(debug=True)
