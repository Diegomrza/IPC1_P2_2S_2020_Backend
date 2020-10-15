#Comentario de una linea

''' Comentario
multilinea '''
class ClaseLogin:

	def __init__(self, ID, usuario, nombre, contraseña):
		self.ID = ID
		self.usuario = usuario
		self.nombre = nombre
		self.contraseña = contraseña

	def login(self, usuario, contraseña, confirmarContraseña):
		if contraseña == confirmarContraseña:
			print("Bienvenido")
		else:
			print("Incorrecto")



usuario1 = ClaseLogin(1,"Squery","Diego", "1234")
usuario1.login(usuario1.usuario, usuario1.contraseña, "1234")
