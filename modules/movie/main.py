from dataclasses import dataclass
import random
from modules.movie.search import Search
from modules.movie.watch import Watch
from modules.movie.data import Data

@dataclass
class Movie(Data, Search, Watch):
    watched_movies: list = None
    all_movies = list  = None

    # def load_data(self):
    #     print("loading data")
    def display_movies(self):
        # returns a return a list of 7 randomly selected movies
        movies = random.sample(self.all_movies, 7)
        print(*movies, sep="\n")

        # self.back_to_menu()
        self.want_to_watch()
