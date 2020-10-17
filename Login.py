class Usuario:

    usuarios = []

    def __init__(self, id, nombre, apellido, usuario, password):
    	self.nombre = nombre
    	self.apellido = apellido
    	self.usuario = usuario
    	self.password = password

    def muestra(self, usuario, password):
    	if self.usuario == usuario and self.password == password:
    		print("Bienvenido")
    	else:
    		print("Error")


usuario1 = Usuario(1, "Diego","Robles","Squery",'123')

usuario1.muestra("Squery", "1234")