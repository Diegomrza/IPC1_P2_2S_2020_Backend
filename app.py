from flask import Flask, request, jsonify
from flask_cors import CORS
from Personas import Persona
from Juegos import Juegos

app = Flask(__name__)
CORS(app)

juegos = []
usuarios = []

contador_usuarios = 2
contador_juegos = 0

usuarios.append(Persona(0,'Usuario','Maestro','admin','admin','administrador'))
usuarios.append(Persona(1,'diego','robles',"squery",'123','cliente'))
usuarios.append(Persona(1,'kelly','herrea',"killy",'123','cliente'))
usuarios.append(Persona(1,'susan','herrera',"susy",'123','cliente'))
usuarios.append(Persona(1,'usuario','generico',"user",'123','cliente'))

#Método para ingresar
@app.route('/login/', methods=['POST'])
def login():

	global usuarios
	username = request.json["usuario"]
	password = request.json["password"]

	for user in usuarios:
		if user.getUsuario() == username and user.getPassword() == password:
			return jsonify({
				"message": "Succesfully",
				"usuario": user.getUsuario()
				})

	return jsonify({
		"message": "Failed",
		"usuario": ""
	})

#Método para registrar
@app.route('/registro/', methods=['POST'])
def registro():

	global usuarios
	global contador_usuarios
	nombre = request.json["nombre"]
	apellido = request.json["apellido"]
	usuario	= request.json['usuario']
	password = request.json['password']
	confirmPassword = request.json['confirmPassword']

	for user in usuarios:
		if user.getUsuario() == usuario:
			return jsonify({"message": "Failed", "reason": "El usuario ya existe"})

	if password == confirmPassword:
		nuevo = Persona(contador_usuarios, nombre, apellido, usuario, password,'cliente')
		contador_usuarios = contador_usuarios + 1
		usuarios.append(nuevo)	
		mensaje = {"message": "Successfully","reason": "Usuario creado"}
		return jsonify(mensaje)

	mensaje = {"message": "Failed","reason": "Las passwords no coinciden"}
	return jsonify(mensaje)	


#Mostrar solo un usuario recibiendo su usuario como parámetro
@app.route('/usuarios/<string:user>', methods=['GET'])
def obtener_persona(user):
	global usuarios
	Datos = []

	for usuario in usuarios:
		if user == usuario.getUsuario():
			Dato = {'id': usuario.getId(),
			    	'nombre': usuario.getNombre(),
				    'apellido': usuario.getApellido(),
				    'usuario': usuario.getUsuario(),
				    'password': usuario.getPassword(),
					'tipo': usuario.getTipo()
                    }
			Datos.append(Dato)
			break

	respuesta = jsonify(Datos)	
	return respuesta

#Mostrar todos los usuarios
@app.route('/usuarios/', methods=['GET'])
def mostrar_personas():
	global usuarios
	Datos = []
	for usuario in usuarios:
		Dato = {'id': usuario.getId(),
				'nombre': usuario.getNombre(),
				'apellido': usuario.getApellido(),
				'usuario': usuario.getUsuario(),
				'password': usuario.getPassword(),
				'tipo': usuario.getTipo()
				}
		Datos.append(Dato)
	respuesta = jsonify(Datos)	
	return (respuesta)
'''
#Crear un usuario e ingresarlo al arreglo
@app.route('/usuarios/', methods=['POST'])
def agregar_usuario():
	global usuarios
	global contador_usuarios

	usuario = request.json['usuario']
	password = request.json['password']

	for user in usuarios:
		if user.autenticacion(usuario, password) == True:
			return jsonify({"message": "Failed", "reason": "El usuario ya existe"})

	nuevo = Persona(contador_usuarios, request.json['nombre'], request.json['apellido'], request.json['usuario'], request.json['password'])
	contador_usuarios = contador_usuarios + 1
	usuarios.append(nuevo)	
	return jsonify({"message": "successfully", "reason": "Usuario creado"})'''

#Modificar un dato del arreglo de usuarios
@app.route('/usuarios/<string:user>', methods=['PUT'])
def editar_usuario(user):
	global usuarios
	for i in range(len(usuarios)):
		if user == usuarios[i].usuario:
			usuarios[i].setNombre(request.json["nombre"])
			usuarios[i].setApellido(request.json["apellido"])
			usuarios[i].setUsuario(request.json["usuario"])
			usuarios[i].setPassword(request.json["password"])
			break
	return jsonify({"message": "Se actualizaron los datos correctamente"})	

#Eliminar un usuario del arreglo de usuarios
@app.route('/usuarios/<string:user>', methods=['DELETE'])
def borrar_usuario(user):
	global usuarios
	for i in range(len(usuarios)):
		if user == usuarios[i].usuario:
			del usuarios[i]
			break
	return jsonify({"message": "Se eliminaron los datos correctamente"})	

#Métodos para los juegos

#Creacion de juegos
@app.route('/juegos/', methods=['POST'])
def crear_juego():

	
	return jsonify({'message': 'successfully', 'reason': 'juego creado'})
	


if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)