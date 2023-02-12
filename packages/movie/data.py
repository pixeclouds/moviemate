from dataclasses import dataclass
import  json
from simple_colors import *


@dataclass
class Data:
    watched_movies: list = None
    all_movies = list  = None

    # Load movies data from database
    def load_data(self):
        self.get_movies_from_db()
        self.watched_movies = []

    # format printed movie info
    def formtter(self, movie):
        return blue(f"Title: {movie['title']} \nGenres: {movie['genres']} \nRuntime: {movie['runtime']}", "bold")

    def get_movies_from_db(self):
        f = open("database/movie_database.json")
        data = json.load(f)
        self.all_movies = data["all_movies"]

    def check_movie_in_db(self, title):
        for movie in self.all_movies:
            if movie["title"] in [ movie["title"] for movie in self.all_movies]:
                if movie["title"].lower() == title.lower():
                    return movie
                
        # Handle input error        
        print(red("Invalid Input/Not Found", "bold"))
        return False

