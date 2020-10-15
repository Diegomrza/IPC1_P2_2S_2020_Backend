#public class Usuario{}
class Pokemon:

	#public Pokemon(parametros){}
	def __init__(self, id, nombre, especie, tipo, foto, passw):
		#print("Este es el constructor")
		self.id = id
		self.nombre = nombre
		self.especie = especie
		self.tipo = tipo
		self.foto = foto
		self.passw = passw
		
	def imprimir_tipo(self):
		print(self.nombre + ' es de tipo: ' + self.tipo)

	def autenticar(self, nombre, passw):
		if self.nombre == nombre and self.passw == passw:
			print('La autenticacion es correcta')
			return True

		print('La autenticacion es incorrecta')
		return False

#variable pokemon
pikachu = Pokemon(1,'pika','pikachu','electrico','https://assets.pokemon.com/assets/cms2/img/pokedex/full/758.png','pass123')
pikachu.imprimir_tipo() 

charizard = Pokemon(2,'chari','charizard','fuego','https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png','pass123')
charizard.imprimir_tipo()

pikachu.autenticar('pika', 'pass123')