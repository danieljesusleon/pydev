from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://backend-service/pokemons')
    pokemons = response.json()
    return render_template('index.html', pokemons=pokemons)

if __name__ == '__main__':
    app.run()
