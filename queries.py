from actor import Actor
from base import Session
from movie import Movie
from QueryConverter import converter

from datetime import date

# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()
mv = converter()._convert_movie(movies)
import pdb;pdb.set_trace()

# u need to convert this data to schema type.
# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# 6 - movies that Dwayne Johnson participated
the_rock_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Dwayne Johnson') \
    .all()

print('### Dwayne Johnson movies:')
for movie in the_rock_movies:
    print(f'The Rock starred in {movie.title}')
print('')