import requests as http
import pprint
from requests.exceptions import ConnectionError, JSONDecodeError

pp = pprint.PrettyPrinter(indent=4)

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

#ditto = http.get(f'{BASE_URL}/ditto')
#data = ditto.json()
#print(data["abilities"])


class Pokemon:
    #se le llama a esto variable de clase
    #BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def __init__(self, name):
        self.name = name
        self.url = "https://pokeapi.co/api/v2/pokemn"

    def __str__(self):
        return self.name

    def show_abilities(self):
        #pokemon_json = http.get(f'{BASE_URL}/{self.name}')
        try:
            pokemon_json = http.get(f'{self.url}/{self.name}')
            pokemon = pokemon_json.json()
            return pokemon["abilities"]
        except (ConnectionError, JSONDecodeError) as error:
            print(error)
            return "Try again later"

    #puedes crear metodos para saber su ataque, su defensa, etc y asi poder hacer batallas pokemon

    
"""puedes crear una clase de batle_pokemon y poder instanciar la clase pokemos v
arias veces y luchar con diferente pokemons, asi tambien puedo tener diferentes batallas"""


class BatllePokemon:
    def __int__(self, pokemon1, pokemon2):
        self.poke1 = Pokemon("squirtle")
        self.poke2 = Pokemon("ditto")
        #el pokemon1 puedes reemplazar por la clase Pokemon("squirtle")

    def init_batle(self):
        print(self.poke1.show_abilities())
        print(self.poke2.show_abilities())


squirtle = Pokemon(name="squirtle")
data = squirtle.show_abilities()
pp.pprint(data)
