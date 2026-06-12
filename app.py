from services.pokemon_api import PokemonAPI
from services.weather_api import WeatherApi
from flask import Flask, render_template
from models.cpu_player import CPUPlayer
from models.pokemon import Pokemon
from models.battle import Battle
from models.player import Player
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def battle_loop(first_trainer, second_trainer, battle):
    first_pokemon = first_trainer.pokemon
    second_pokemon = second_trainer.pokemon
    while battle.check_battle_status(first_pokemon, second_pokemon) == "continue":
        print("\n------------------")
        print(f"Turn: {battle.count_turn}")
        print(f"{first_pokemon.name}: {first_pokemon.health} HP")
        print(f"{second_pokemon.name}: {second_pokemon.health} HP")
        print("------------------")

        battle.handle_turn(
            first_pokemon,
            second_pokemon
        )

        current_attacker = battle.order_to_play[0]
        current_defender = battle.order_to_play[1]

        if current_attacker == first_trainer.pokemon:
            current_trainer = first_trainer
        else:
            current_trainer = second_trainer

        print(f"{current_attacker.name}'s turn")
        
        battle.print_moves(current_attacker.moves)
        
        if isinstance(current_trainer, CPUPlayer):
            print("CPU is thinking...")

            time.sleep(2)

            action = current_trainer.choose_action()

            print(
                f"CPU selected: "
                f"{action if action == 'heal' else action.name}"
            )
            time.sleep(1.5)

        else:
            action = verify_move(
                current_attacker
            )

        battle.decide_action(current_attacker, current_defender, action)

        time.sleep(1.5)
    
    winner = battle.check_battle_status(first_pokemon, second_pokemon)

    print(f"\n🏆 Winner: " f"{winner.name}")


def start_game():
    print_title()
    pokemon1 = verify_pokemon("Choose Pokemon 1 (Player): ")
    pokemon2 = verify_pokemon("Choose Pokemon 2 (CPU): ")

    player = Player(pokemon1)
    cpu = CPUPlayer(pokemon2)

    first_pokemon, second_pokemon = which_starts_first(
        pokemon1,
        pokemon2
    )

    if first_pokemon == player.pokemon:
        first_trainer = player
        second_trainer = cpu
    else:
        first_trainer = cpu
        second_trainer = player

    city = verify_city()

    battle = Battle(city)

    return first_trainer, second_trainer, battle

def verify_pokemon(message):
    while True:
        try:
            pokemon_name = input(message)

            pokemon1 = create_pokemon(pokemon_name)

            return pokemon1

        except Exception as e:
            print(f"ERROR: {e}")

def verify_city():
    while True:
        try:
            city_name = input(
                "Choose a city to start the fight: "
            )

            weather = (
                WeatherApi()
                .get_current_weather(
                    city_name
                )
            )

            print(
                f"Weather detected: "
                f"{weather.capitalize()}"
            )

            return city_name

        except Exception:
            print(
                "City not found!"
            )

def verify_move(current_attacker):
    while True:
        try:
            move_id = int(
                input("Choose a move: ")
            )

            if move_id == 0:
                return "heal"

            move = current_attacker.choose_move(
                move_id
            )

            if move:
                return move

            print("Invalid move!")

        except ValueError:
            print("Please enter a valid number!")

def create_pokemon(pokemon_name):
    response = PokemonAPI(pokemon_name.lower()).get_pokemon()
    
    pokemon = Pokemon(response["name"], response["type"], response["level"] ,response["weight"], response["height"], response["base_health"], response["base_attack"], response["base_defense"], response["moves"], response["base_speed"])
    
    return pokemon

def which_starts_first(pokemon1, pokemon2):
    
    if pokemon1.speed > pokemon2.speed:
        return pokemon1, pokemon2

    if pokemon2.speed > pokemon1.speed:
        return pokemon2, pokemon1

    first = random.choice(
        [pokemon1, pokemon2]
    )

    second = (
        pokemon2
        if first == pokemon1
        else pokemon1
    )

    return first, second

def print_title():
    print(r"""
    =========================================================
    ██████╗  ██████╗ ██╗  ██╗███████╗██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗
    ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║█████╔╝ █████╗  ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
    ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝██║  ██╗███████╗╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

    ███████╗██╗ ██████╗ ██╗  ██╗████████╗
    ██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
    █████╗  ██║██║  ███╗███████║   ██║
    ██╔══╝  ██║██║   ██║██╔══██║   ██║
    ██║     ██║╚██████╔╝██║  ██║   ██║
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

            ⚡ Pokémon + Weather Battle ⚡
    =========================================================
    """)
if __name__ == "__main__":

    # app.run(debug=True)
    first_trainer, second_trainer, battle = (
        start_game()
    )

    battle_loop(
        first_trainer,
        second_trainer,
        battle
    )