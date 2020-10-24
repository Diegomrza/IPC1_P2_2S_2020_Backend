from flask import Flask, request, jsonify
from Login import Usuario
from flask_cors import CORS

usuarios = []
usuarios.append(Usuario(0, "Usuario", "Maestro", "admin", "admin", 'Administrador'))
usuarios.append(Usuario(1,'Diego','Robles','Squery','Marihuana7291384650','cliente'))

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
#Método para hacer la autenticación del usuario
def login():
	if request.method == 'POST':

		usuario = request.form.get('nombre_usuario')
		password = request.form.get('password_usuario')

		#For que recorre el arreglo de los usuarios
		for user in usuarios:
			#Devuelve los datos del usuario si lo encontró
			if user.verificacion(usuario,password) == True:
				return user.dump()
		#Devuelve un mensaje si no encontró un usuario
		return "No se encontró el usuario"


@app.route("/registro")
def index():
	return "<h1>Texas</h1>"

if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)