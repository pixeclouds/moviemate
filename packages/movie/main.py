from dataclasses import dataclass
import random
from packages.movie.search import Search
from packages.movie.watch import Watch
from packages.movie.data import Data
from simple_colors import *

@dataclass
class Movie(Data, Search, Watch):
    watched_movies: list = None
    all_movies = list  = None

    def display_movies(self):
        # returns a return a list of 7 randomly selected movies
        movies = random.sample(self.all_movies, 7)
        movies = [ self.formtter(movie) for movie in movies]
        print(yellow("\nMovies you might like to watch...", "bold"))

        print(*movies, sep="\n\n")

        # self.back_to_menu()
        self.want_to_watch()
