from flask import Flask, request, jsonify
from flask_cors import CORS
from Personas import Persona
from Juegos import Juegos
from Comentarios import Comentarios
from datetime import datetime

app = Flask(__name__)
CORS(app)

lista_juegos = []
usuarios = []
juegos_comprados = []
comentarios = []

contador_usuarios = 1
contador_juegos = 5

#Lista de personas
usuarios.append(Persona(0,'Usuario','Maestro','admin','admin',"administrador"))

#Lista de juegos
lista_juegos.append(Juegos(0, 'Tetris', 1984, 100, 'Puzzle', 'Estrategia', 'Construccion', 'https://www.elotrolado.net/w/images/6/6f/Tetris_%28Caratula_NES%29.jpg', 'https://i.pinimg.com/originals/78/fe/e8/78fee894936f57360a88dd1089aac6ca.png', 'Tetris es un videojuego de lógica originalmente diseñado y programado por Alekséi Pázhitnov en la Unión Soviética. Fue lanzado el 6 de junio de 1984.'))
lista_juegos.append(Juegos(1, 'God of War', 2005, 200, 'Aventura', 'Estrategia', 'Peleas', 'https://upload.wikimedia.org/wikipedia/en/0/0c/Gowbox.jpg', 'https://www.moodvisuals.com/wp-content/uploads/2019/02/GoW-Header-01.jpg', 'God of War es un videojuego de acción-aventura desarrollado por SCE Santa Monica Studio y distribuido por Sony Computer Entertainment en 2005 para PlayStation 2. '))
lista_juegos.append(Juegos(2, 'The Legend of Zelda', 1986, 300, 'Aventura', 'Estrategia', 'Accion', 'https://newesc.com/wp-content/uploads/legend-of-zelda-bow-us.jpg','https://thenintendoswitchgames.com/appData/the-legend-of-zelda-breath-of-the-wild/banner.jpg', 'The Legend of Zelda es una serie de videojuegos de acción-aventura creada por los diseñadores japoneses Shigeru Miyamoto y takashi tezuka y desarrollada por Nintendo empresa que también se encarga de su distribución internacional.'))
lista_juegos.append(Juegos(3, 'Mario', 1983, 400, 'Aventura', 'Estrategia', 'Plataforma', 'https://nintendolatino.com/wp-content/uploads/2013/11/nes-super-mario-bros-1-cover-artwork-for-box.jpg','https://s.libertaddigital.com/2017/11/15/640/320/312x161/super-mario-bros.jpg?390d7ac9-1a2d-4679-8e0d-2a964677b81b', 'Super Mario Bros. o Super Mario Brothers es un videojuego de plataformas diseñado por Shigeru Miyamoto lanzado el 13 de septiembre de 1985 y producido por la compañía Nintendo para la consola Nintendo Entertainment System.'))
lista_juegos.append(Juegos(4, 'Need for Speed: Most Wanted', 2012, 500, 'Carreras', 'Accion', '', 'https://vignette.wikia.nocookie.net/nfs/images/7/76/NFSMW_Boxart.jpg/revision/latest/top-crop/width/360/height/450?cb=20200127230308&path-prefix=es','https://steam.cryotank.net/wp-content/gallery/needforspeedmostwanted2012/Need-For-Speed-Most-Wanted-2012-06-HD.png','Need for Speed: Most Wanted es un videojuego de carreras de la saga Need for Speed desarrollado por Electronic Arts y Criterion Games para Xbox 360'))


#Login
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


#Recuperar contraseña
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



#Registro 
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



#Registro como administrador
@app.route('/registroAdmin/', methods=['POST'])
def registro_admin():

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
		nuevo = Persona(contador_usuarios, nombre, apellido, usuario, password,'administrador')
		contador_usuarios = contador_usuarios + 1
		usuarios.append(nuevo)	
		mensaje = {"message": "Successfully","reason": "Usuario creado"}
		return jsonify(mensaje)

	mensaje = {"message": "Failed","reason": "Las passwords no coinciden"}
	return jsonify(mensaje)	


#Mostrar un usuario
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


#Mostrar todos los usuarios
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


#Modificar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
	global usuarios

	usuario = request.json["usuario"]

	if	usuario == "":
		for i in range(len(usuarios)):
			if id == usuarios[i].id:
				usuarios[i].setNombre(request.json["nombre"])
				usuarios[i].setApellido(request.json["apellido"])
				usuarios[i].setPassword(request.json["password"])
				break
	else:
		for i in range(len(usuarios)):
			if id == usuarios[i].id:
				usuarios[i].setNombre(request.json["nombre"])
				usuarios[i].setApellido(request.json["apellido"])
				usuarios[i].setUsuario(request.json["usuario"])
				usuarios[i].setPassword(request.json["password"])
				break
	
				
	return jsonify({"message": "Se actualizaron los datos correctamente"})	


#Eliminar un usuario
@app.route('/usuarios/<string:user>', methods=['DELETE'])
def borrar_usuario(user):
	global usuarios
	for i in range(len(usuarios)):
		if user == usuarios[i].usuario:
			del usuarios[i]
			break
	return jsonify({"message": "Se eliminaron los datos correctamente"})	



#Crear juegos
@app.route('/juegos/', methods=['POST'])
def crear_juego():
	global lista_juegos
	global contador_juegos
	flag = True
	nombre = request.json['nombre']
	anio = request.json['anio']
	precio = request.json['precio']
	categoria1 = request.json['categoria1']
	categoria2 = request.json['categoria2']
	categoria3 = request.json['categoria3']
	foto = request.json['foto']
	banner = request.json['banner']
	descripcion = request.json['descripcion']

	if nombre == "":
		flag = False
	else:
		nuevo_juego = Juegos(contador_juegos,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)
		contador_juegos = contador_juegos + 1
		lista_juegos.append(nuevo_juego)
		
	if	flag == True:
		mensaje = {"message": "Successfully","reason": "Juego creado"}
	else:
		mensaje = {"message": "Failed" }

	return jsonify(mensaje)


#Ver juego
@app.route('/usuarios/<int:id>', methods=['GET'])
def ver_juego(id):
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

#Modificar juego
@app.route('/modJuegos/<int:id>', methods=['PUT'])
def modificar_juego(id):
	global lista_juegos

	for i in range(len(lista_juegos)):
			if id == lista_juegos[i].id:
				lista_juegos[i].setNombre(request.json["nombre"])
				lista_juegos[i].setAnio(request.json["anio"])
				lista_juegos[i].setPrecio(request.json["precio"])
				lista_juegos[i].setCategoria1(request.json["categoria1"])
				lista_juegos[i].setCategoria2(request.json["categoria2"])
				lista_juegos[i].setCategoria3(request.json["categoria3"])
				lista_juegos[i].setFoto(request.json["foto"])
				lista_juegos[i].setBanner(request.json["banner"])
				lista_juegos[i].setDescripcion(request.json["descripcion"])
				break
	
	return jsonify({"message": "Se actualizaron los datos correctamente"})	


#Eliminar juego
@app.route('/juegosEliminar/<int:id>', methods=['DELETE'])
def eliminar_juego(id):
	global lista_juegos
	for i in range(len(lista_juegos)):
		if id == lista_juegos[i].id:
			del lista_juegos[i]
			break
	return jsonify({"message": "Se eliminaron el juego correctamente"})


#Obtener todos los juegos
@app.route('/obtenerJuegos')
def obtener_juegos():
	global lista_juegos
	Datos = []
	for juego in lista_juegos:
		Dato = {
				'id': juego.getId(),
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


#Obtener juegos por su genero
@app.route('/juegos/<string:categoria>', methods=['GET'])
def obtener_un_juego_categoria(categoria):
	global lista_juegos
	datos = []
	for juego in lista_juegos:
		if categoria == juego.categoria1 or categoria == juego.categoria2 or categoria == juego.categoria3:
			dato = {
					'id': juego.getId(),
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
			datos.append(dato)
	print(len(datos))

	if len(datos) == 0:
		respuesta = jsonify({"message":"sinResultados"})
	else:
		respuesta = jsonify(datos)	

	return respuesta


#Obtener juegos por su id
@app.route('/juego/<int:id>', methods=['GET'])
def obtener_un_juego(id):
	global lista_juegos

	for juego in lista_juegos:
		if id == juego.getId():
			dato = {
					'id': juego.getId(),
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
			break
	respuesta = jsonify(dato)	
	return respuesta


#Comprar Juegos  
@app.route('/adquirirJuego/<int:id>', methods=['POST'])
def adquirir_un_juego(id):
	global lista_juegos
	global juegos_comprados

	id_usuario = request.json['id']
	id_unido = str(id)+","+id_usuario
	
	for juego in lista_juegos:
		if id == juego.getId():
			nombre = juego.nombre
			anio = juego.anio
			precio = juego.precio
			categoria1 = juego.categoria1
			categoria2 = juego.categoria2
			categoria3 = juego.categoria3
			foto = juego.foto
			banner = juego.banner
			descripcion = juego.descripcion

			#Creacion del juego nuevo asociandolo con el id del usuario
			nuevo_juego = Juegos(id_unido,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)		
			juegos_comprados.append(nuevo_juego)		
			break
	respuesta = jsonify({'message':'Succesfully'})	
	return respuesta	


#Mostrar juegos comprados por un usuario
@app.route('/compras/<int:id>', methods=['GET'])
def obtener_juegos_comprados(id):
	global juegos_comprados

	x = []
	idu = str(id)
	datos = []

	for juego in juegos_comprados:
		x = juego.id.split(',')
		if idu == x[1]:
			dato = {
				'id': juego.getId(),
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
			datos.append(dato)
	respuesta = jsonify(datos)	
	return respuesta


#Obtener todas las compras
@app.route('/obtenerCompras')
def compras_totales():
	global juegos_comprados
	Datos = []
	for juego in juegos_comprados:
		Dato = {
				'id': juego.getId(),
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


#Crear comentarios
@app.route('/comentarios/<int:id>', methods=['POST'])
def crear_comentario(id):
	global comentarios

	id_usuario = request.json['id']
	comentario = request.json['comentario']
	nombre = request.json['usuario']
	fecha = datetime.now()

	print(fecha)

	comentarios.append(Comentarios(id_usuario, id, comentario, nombre, fecha))

	respuesta = jsonify({'message':'Succesfully'})	
	return respuesta


#Obtener todos los comentarios
@app.route('/comentarios', methods=['GET'])
def ver_comentarios():
	global comentarios
	coments = []

	for comentario in comentarios:
		comenta = {
			'idUsuario': comentario.id_usuario,
			'idJuego': comentario.id_juego,
			'comentario': comentario.texto,
			'usuario': comentario.nombre,
			'fecha': comentario.fecha
		}
		coments.append(comenta)

	respuesta = jsonify(coments)	
	return respuesta


#Obtener solo los comentarios de un juego
@app.route('/comentarios/<int:id>', methods=['GET'])
def ver_comentarios_de_juego(id):

	global comentarios
	coments = []

	for comentario in comentarios:
		if id == comentario.id_juego:
			
			print(comentario.fecha)
			
			comenta = {
				'idUsuario': comentario.id_usuario,
				'idJuego': comentario.id_juego,
				'comentario': comentario.texto,
				'usuario': comentario.nombre,
				'fecha':comentario.fecha
			}
			coments.append(comenta)

	respuesta = jsonify(coments)	
	return respuesta	


#Ruta Principal que no tiene nada
@app.route('/')
def mensaje():
	return "Online!"

if __name__ == "__main__":
	app.run(threaded = True,port = 5000, debug = True)