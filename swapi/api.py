from flask import Blueprint, Response, request, jsonify
from .service import Process
import requests
import json


StarWars = Blueprint(
    "people", __name__, url_prefix="/v1/informacoes"
)

@StarWars.route("/personagem/<nome>", methods=["GET"])
def personagem(nome):
    a = Process.personagem(nome)
    b = json.dumps(a)   

    return b
