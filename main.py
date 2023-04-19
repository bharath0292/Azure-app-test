"""
    API REST con Python 3 y SQLite 3
    By Parzibyte: 
    ** https://parzibyte.me/blog **
"""
from flask import Flask, jsonify, request
import game_controller
from flask_cors import CORS, cross_origin
import time
import threading

app = Flask(__name__)
CORS(app)

a = 0

def a_loop():
    global a
    while True:
        a += 1
        time.sleep(5)

t = threading.Thread(target=a_loop)
t.daemon = True
t.start()



@app.route('/null', methods=["GET"])
def null():
    global a
    return jsonify([a])

@app.route('/games', methods=["GET"])
def get_games():
    games = game_controller.get_games()
    return jsonify(games)


@app.route("/game", methods=["POST"])
def insert_game():
    game_details = request.get_json()
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.insert_game(name, price, rate)
    return jsonify(result)


@app.route("/game", methods=["PUT"])
def update_game():
    game_details = request.get_json()
    id = game_details["id"]
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.update_game(id, name, price, rate)
    return jsonify(result)


@app.route("/game/<id>", methods=["DELETE"])
def delete_game(id):
    result = game_controller.delete_game(id)
    return jsonify(result)


@app.route("/game/<id>", methods=["GET"])
def get_game_by_id(id):
    game = game_controller.get_by_id(id)
    return jsonify(game)


