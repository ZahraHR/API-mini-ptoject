from typing import List
import json

from movie import Movie
from actor import Actor

class converter:

    @staticmethod
    def _convert_actor(actor):
        return {'id': actor.id,
                'name': actor.name,
                'birthday': actor.birthday}

    def _convert_movie(self,movies):
        self.movies=movies
        return [{'id':movie.id,
                'title':movie.title,
                'release_date':movie.release_date,
                'actors':[self._convert_actor(actor) for actor in movie.actors]} for movie in movies]
