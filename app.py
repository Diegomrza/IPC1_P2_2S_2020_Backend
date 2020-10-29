from flask import Flask, request, jsonify
from flask_cors import CORS
from Personas import Persona
from Juegos import Juegos

app = Flask(__name__)
CORS(app)

lista_juegos = []
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

#Método para recuperar la contraseña
@app.route('/recuperar/',methods=['POST'])
def recuperacion():
	global usuarios
	username = request.json["usuario"]

	for user in usuarios:
		if user.getUsuario() == username:
			return jsonify({
				"message": "Succesfully",
				"usuario": user.getUsuario(),
				"password": user.getPassword()
				})

	return jsonify({
		"message": "Failed",
		"usuario": "No encontrado"
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

	global lista_juegos
	global contador_juegos

	nombre = request.json["nombre"]
	anio = request.json["anio"]
	precio	= request.json['precio']
	categoria1 = request.json['categoria1']
	categoria2 = request.json['categoria2']
	categoria3 = request.json['categoria3']
	foto = request.json['foto']
	banner = request.json['banner']
	descripcion = request.json['descripcion']

	for juego in lista_juegos:
		if juego.getNombre() == nombre:
			return jsonify({"message": "Failed", "reason": "El juego ya existe"})

	nuevo_juego = Juegos(contador_juegos, nombre, anio, precio, categoria1,categoria2, categoria3, foto, banner, descripcion)
	contador_juegos = contador_juegos + 1
	lista_juegos.append(nuevo_juego)	
	mensaje = {"message": "Successfully","reason": "Juego creado"}
	return jsonify(mensaje)

	
@app.route('/')
def mensaje():
	return "Hola chiquibeibi"


if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)