import requests
poke_url = "https://pokeapi.co/api/v2/type"
class TypePokemon:
    def get_type_effectiveness(self, attack_type, defender_type):
        response_attack = requests.get(f"{poke_url}/{attack_type}").json()
        response_defender = requests.get(f"{poke_url}/{defender_type}").json()
        
        return response_attack,response_defender
