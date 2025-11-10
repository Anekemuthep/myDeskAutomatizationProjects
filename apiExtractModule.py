import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {response.status_code}")

def pokemon_info_of(pokemon_name,inforequested):
    pokemon_info = get_pokemon_info(pokemon_name)
    info_retrived = pokemon_info[f"{inforequested}"]
    print(f"{inforequested}: {info_retrived}")

def pokemon_printer(pokemonName):
    pokemon_info = get_pokemon_info(pokemonName)  
    if pokemon_info:
        pokemon_info_of(pokemonName, "name")
        pokemon_info_of(pokemonName, "id")
        pokemon_info_of(pokemonName,"height")
        pokemon_info_of(pokemonName,"weight")
    else:
        print(f"no data found for {pokemonName}")

pokemon_printer("pikachu")
pokemon_printer("typhlosion")
#pokemon_printer("electrifier")
pokemon_printer("charmander")