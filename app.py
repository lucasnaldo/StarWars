from flask import Flask
from swapi import StarWars

app = Flask(__name__)
app.register_blueprint(StarWars)   

try:
    app.run(debug=True)
except Exception as ex:
    print(f'''Erro ao levantar a aplicação.
Exception: {str(ex)}''')

