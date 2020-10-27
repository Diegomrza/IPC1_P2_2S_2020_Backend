class Persona:
    def __init__(self, id, nombre, apellido, usuario, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password

    def autenticacion(self, usuario, password):
        if self.usuario == usuario:
            return True
        return False    

    def dump(self):
    
    	return {
    	    'id':self.id,
    	    'nombre':self.nombre,
            'apellido':self.apellido,
            'user':self.usuario,
            'contraseña':self.password,
    	}

    #setters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre    

    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password

    #Seters
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password

