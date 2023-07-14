from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pokemons')
def get_pokemons():
    response = requests.get('https://pokeapi.co/api/v2/pokemon')
    data = response.json()
    pokemons = []
    for pokemon in data['results']:
        pokemons.append(pokemon['name'])
    return jsonify(pokemons)

if __name__ == '__main__':
    app.run()