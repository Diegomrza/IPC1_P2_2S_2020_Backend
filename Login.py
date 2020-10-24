class Usuario:

    def __init__(self, id, nombre, apellido, user, password, tipo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.password = password
        self.tipo =	tipo

    def verificacion(self, user, password):

        if self.user == user and self.password == password:
            print('La autenticacion fue correcta')
            return True
        else:
	        return False
    	

    def dump(self):
    
    	return {
    	    'id':self.id,
    	    'nombre':self.nombre,
            'apellido':self.apellido,
            'user':self.user,
            'contraseña':self.password,
            'tipo':self.tipo
    	}		

