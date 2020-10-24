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
    
    def crear_juego(self, id, nombre, anio, precio, categoria1, categoria2, categoria3, foto, banner, descripcion):
        print('Hola, se creó un nuevo juego :D')

    def ver_juego(self,id):
        print()