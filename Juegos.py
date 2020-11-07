class Juegos:

    def __init__(self, id, nombre, anio, precio, categoria1, categoria2, categoria3, foto, banner, descripcion):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.precio = precio
        self.categoria1 = categoria1
        self.categoria2 = categoria2
        self.categoria3 = categoria3
        self.foto = foto
        self.banner = banner
        self.descripcion = descripcion
    
    #Getters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAnio(self):
        return self.anio

    def getPrecio(self):
        return self.precio

    def getCategoria1(self):
        return self.categoria1

    def getCategoria2(self):
        return self.categoria2

    def getCategoria3(self):
        return self.categoria3

    def getFoto(self):
        return self.foto

    def getBanner(self):
        return self.banner

    def getDescripcion(self):
        return self.descripcion                

    #Setters
    def setId(self, id):
        self.id =id

    def setNombre(self, nombre):
        self.nombre = nombre  

    def setAnio(self, anio):
        self.anio = anio

    def setPrecio(self, precio):
        self.precio = precio

    def setCategoria1(self, categoria1):
        self.categoria1 = categoria1

    def setCategoria2(self, categoria2):
        self.categoria2 = categoria2

    def setCategoria3(self, categoria3):
        self.categoria3 = categoria3

    def setFoto(self, foto):
        self.foto = foto

    def setBanner(self, banner):
        self.banner = banner

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion    
