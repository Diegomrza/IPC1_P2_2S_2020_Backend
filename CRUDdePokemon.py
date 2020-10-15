from pokemon import Pokemon

class CRUDdePokemon:

 	def __init__(self):

 		#Lista
 		self.pokemon = []
 		self.contador = 0

 		#Metodo para crear pokemon
 	def crear(self, nombre, especie, tipo, foto, passw):
 		
 		for poke in self.pokemon:

 			if poke.nombre == nombre:
 				print('el nombre de usuario ya está en uso')
 				return False

 		nuevo = Pokemon(self.contador, nombre, especie, tipo, foto, passw)		
 		self.pokemon.append(nuevo)
 		self.contador += 1
 		return True

 	def listar(self):

 		print('id:\tTipo:\t\tNombre de Usuario:')

 		for poke in self.pokemon:

 			print(str(poke.id) + '\t' + poke.especie + '\t\t' + poke.nombre)

'''
#variable pokemon
pikachu = Pokemon(1,'pika','pikachu','electrico','https://assets.pokemon.com/assets/cms2/img/pokedex/full/758.png','pass123')
pikachu.imprimir_tipo() 

charizard = Pokemon(2,'chari','charizard','fuego','https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png','pass123')
charizard.imprimir_tipo()

pikachu.autenticar('pika', 'pass123')'''
var_crud = CRUDdePokemon()
var_crud.crear('pika', 'Pikachu', 'Electrico', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/758.png', 'pass123')
var_crud.crear('chari', 'Charizard', 'Fuego', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/758.png', 'pass123')
var_crud.crear('Squery', 'Diego', 'persona', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/758.png', 'pass123')


var_crud.listar()