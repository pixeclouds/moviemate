from dataclasses import dataclass
import random
from packages.movie.search import Search
from packages.movie.watch import Watch
from packages.movie.data import Data
from simple_colors import *


'''
This class inherits the Data, Search and Watch classes. 
methods and properties can thus be accessed across the three classes.
....
Attributes declared in other classes:
- want_to_watch() attribute is defined in the Interface Class.
- Formatter() is defined in the Data class
'''
@dataclass
class Movie(Data, Search, Watch):
   
    # This attribute returns and print a list of randomly selected movies from the database
    def display_movies(self):
        movies = random.sample(self.all_movies, 7)
        # Formatter attribute is inherited from the Data class
        movies = [ self.formatter(movie) for movie in movies]
        print(yellow("\nMovies you might like to watch...", "bold"))

        print(*movies, sep="\n\n")

        self.want_to_watch()
