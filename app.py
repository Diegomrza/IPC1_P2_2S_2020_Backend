from flask import Flask 
from Login import Usuario


usuarios = []
usuarios.append(Usuario(1, "Diego", "Robles", "Squartul", "123"))
usuarios.append(Usuario(2,"Angel", "Ávila", "Rangolfa","123"))


app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>" + "Hola amorrrr" + " Gays" + "</h1>"



if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)