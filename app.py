from flask import Flask, render_template
from services.pokemon_api import PokemonAPI
from services.weather_api import WeatherApi

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

pokemon_api = PokemonAPI('Pikachu')
weather_api = WeatherApi('current', 'Mexico')
print(pokemon_api.get_pokemon('pikachu'))
print(weather_api.get_current_weather('current', 'Mexico'))

if __name__ == "__main__":

    app.run(debug=True)