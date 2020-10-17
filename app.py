from flask import Flask, request, jsonify
from Login import Usuario


usuarios = []
usuarios.append(Usuario(1, "Diego", "Robles", "Squartul", "123"))
usuarios.append(Usuario(2,"Angel", "Avila", "Rangolfa","123"))


app = Flask(__name__)

@app.route('/login', methods=['POST'])
#Método para hacer la autenticación del usuario
def login():
	if request.method == 'POST':

		response = {}

		nombre = request.form.get('nombre_usuario')
		password = request.form.get('password_usuario')

		#For que recorre el arreglo de los usuarios
		for user in usuarios:

			#Devuelve True si encontró uno
			if user.muestra(nombre,password) == True:

				response["id"] = user.id
				response["usuario"] = user.usuario

				return response

		#Devuelve False si no encontró un usuario
		return "False"


@app.route("/")
def index():
	return "<h1>Prueba de pagina en la nube</h1>"

if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)