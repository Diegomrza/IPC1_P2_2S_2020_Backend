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

#Lista de personas
usuarios.append(Persona(0,'Usuario','Maestro','admin','admin',"administrador"))
usuarios.append(Persona(1,'diego','robles',"squery",'Marihuana',"cliente"))
usuarios.append(Persona(1,'kelly','herrea',"killy",'Arielito',"cliente"))
usuarios.append(Persona(1,'susan','herrera',"susy",'555',"cliente"))
usuarios.append(Persona(1,'usuario','generico',"user",'123',"cliente"))

#Lista de juegos
lista_juegos.append(Juegos(0, 'Halo', 2020, 300, 'Disparos', 'Estrategia', 'Suspenso', 'https://www.somosxbox.com/wp-content/uploads/2020/07/portada-oficial-de-Halo-Infinite.jpg', '', 'Hola'))
lista_juegos.append(Juegos(1, 'God of War', 2015, 300, 'Cocina', 'Estrategia', 'Miedo', 'https://images-na.ssl-images-amazon.com/images/I/51HGPUarUJL._AC_.jpg', '', 'Adios'))
lista_juegos.append(Juegos(2, 'Zelda', 2018, 300, 'Shooter', 'Estrategia', 'Puzzles', 'https://media.vandal.net/t200/43030/the-legend-of-zelda-breath-of-the-wild-201732131429_1.jpg','', 'Nel'))
lista_juegos.append(Juegos(3, 'Mario', 2000, 300, 'aventura', 'Estrategia', 'plataformas', 'https://img.elcomercio.pe/files/listing_ec_flujo_xx/uploads/2019/09/10/5d782abdf1f30.jpeg','', 'No hay'))
lista_juegos.append(Juegos(4, 'Need for Speed', 1995, 300, 'Disparos', 'Estrategia', 'Aventura', 'https://1.bp.blogspot.com/-vRye3bO-Ghk/Xc4mVG7azII/AAAAAAAAFTM/w7LqEKFmH5Av1XtAXAO2yyI-rvO292mCgCPcBGAYYCw/s640/1539.jpg','','sindesc'))
lista_juegos.append(Juegos(5, 'Minecraft', 2013, 300, 'Disparos', 'Estrategia', 'Thriller', 'https://vignette.wikia.nocookie.net/c-s/images/8/88/2127186-box_minecraft_large.png/revision/latest?cb=20121218031643','', 'Si hay'))


#Método para loguearse -----------------------------------------------------------------------
@app.route('/login/', methods=['POST'])
def login():

	global usuarios
	username = request.json["usuario"]
	password = request.json["password"]
	
	for user in usuarios:
		if user.usuario == username and user.password == password:
			return jsonify({
				"message": "Succesfully",
				"nombre": user.nombre,
				"apellido": user.apellido,
				"usuario": user.usuario,
				"password": user.password,
				"tipo": user.tipo,
				"id": user.id
				})

	return jsonify({
		"message": "Failed",
		"usuario": ""
	})

#Método para recuperar la contraseña -------------------------------------------------------
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

#Método para registrarse ---------------------------------------------------------------------
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


#Método para mostrar un usuario ---------------------------------------------------------------
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_persona(id):
	global usuarios

	for usuario in usuarios:
		if id == usuario.getId():
			dato = {
					'id': usuario.getId(),
			    	'nombre': usuario.getNombre(),
				    'apellido': usuario.getApellido(),
				    'usuario': usuario.getUsuario(),
				    'password': usuario.getPassword(),
					'tipo': usuario.getTipo()
                    }
			break

	respuesta = jsonify(dato)	
	return respuesta

#Método para mostrar todos los usuarios -------------------------------------------------------
@app.route('/usuarios/', methods=['GET'])
def mostrar_personas():
	global usuarios
	datos = []
	for usuario in usuarios:
		dato = {
				'id': usuario.getId(),
				'nombre': usuario.getNombre(),
				'apellido': usuario.getApellido(),
				'usuario': usuario.getUsuario(),
				'password': usuario.getPassword(),
				'tipo': usuario.getTipo()
				}
		datos.append(dato)
	respuesta = jsonify(datos)	
	return (respuesta)

#Método para modificar un usuario -------------------------------------------------------------
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
	global usuarios

	for i in range(len(usuarios)):
		if id == usuarios[i].id:
			usuarios[i].setNombre(request.json["nombre"])
			usuarios[i].setApellido(request.json["apellido"])
			usuarios[i].setUsuario(request.json["usuario"])
			usuarios[i].setPassword(request.json["password"])
			break
				
	return jsonify({"message": "Se actualizaron los datos correctamente"})	

#Método para eliminar un usuario --------------------------------------------------------------
@app.route('/usuarios/<string:user>', methods=['DELETE'])
def borrar_usuario(user):
	global usuarios
	for i in range(len(usuarios)):
		if user == usuarios[i].usuario:
			del usuarios[i]
			break
	return jsonify({"message": "Se eliminaron los datos correctamente"})	


#Métodos para los juegos

#Método para crear juegos ---------------------------------------------------------------------
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

#Método para obtener todos los juegos ---------------------------------------------------------
@app.route('/obtenerJuegos')
def obtener_juegos():
	global lista_juegos
	Datos = []
	for juego in lista_juegos:
		Dato = {'id': juego.getId(),
				'nombre': juego.getNombre(),
				'anio': juego.getAnio(),
				'precio': juego.getPrecio(),
				'categoria1': juego.getCategoria1(),
				'categoria2': juego.getCategoria2(),
				'categoria3': juego.getCategoria3(),
				'foto': juego.getFoto(),
				'banner': juego.getBanner(),
				'descripcion': juego.getDescripcion()
				}
		Datos.append(Dato)
	respuesta = jsonify(Datos)	
	return respuesta

#Ruta Principal que no tiene nada
@app.route('/')
def mensaje():
	return "Hola chiquibeibi"


if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)