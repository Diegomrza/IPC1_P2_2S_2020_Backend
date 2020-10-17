class Usuario:

    def __init__(self, id, nombre, apellido, usuario, password):
    	self.id = id
    	self.nombre = nombre
    	self.apellido = apellido
    	self.usuario = usuario
    	self.password = password

    def muestra(self, usuario, password):


    	if self.usuario == usuario and self.password == password:
    		
    		return True
    	else:
    		return False

    def dump(self):
    
    	return {
    	'id' :self.id,
    	'nombre' :self.usuario
    	}		


usuario1 = Usuario(0, "Diego","Robles","Squery",'123')

#usuario1.muestra("Squery", "1234")

