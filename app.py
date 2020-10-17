from flask import Flask 
from Login import Usuario


app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Prueba numero 2 de heroku</h1>"


if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)