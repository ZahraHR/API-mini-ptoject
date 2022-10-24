from flask import Flask, jsonify, request
import json

from base import Session

from movie import Movie
from actor import Actor

from QueryConverter import converter


app = Flask(__name__)

session = Session()


# 3 - extract all movies

@app.route('/')
def get_all_movies():
    movies = session.query(Movie).all()
    return jsonify(converter()._convert_movie(movies))


if __name__ == "__main__":
    app.run()