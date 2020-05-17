from flask import Flask, render_template
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
#app.debug = True

#app.config["SECRET_KEY"] = "super_secret_key"
#toolbar = DebugToolbarExtension(app)

@app.route("/")
def first():
	return render_template("index.html")

@app.route("/departures/<departure>")
def route_departures(departure):
	return render_template("departure.html")

@app.route("/tours/<id>")
def route_tours(id):
	return render_template("tour.html")

if __name__ == "__main__":
	app.run(host = "185.162.131.72", port=80)
