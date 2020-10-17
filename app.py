from flask import Flask 
from Login import Usuario


app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Que onda que pets</h1>"


if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)