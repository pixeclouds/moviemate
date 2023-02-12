from dataclasses import dataclass
import re
from simple_colors import *
# from main import Movie


@dataclass
class Search:
    
    def search_for_movie(self):
        query = input(yellow("Search: ", "bold")).strip()
        result = self.run_search(query)
        print(*result, sep="\n")
        # self.back_to_menu()
        self.want_to_watch()

    def run_search(self, query):
        movies = [ movie["title"] for movie in self.all_movies]
        # Remove common words from the query
        common_words = ["on", "of", "the", "in", "and", "a"]
        query = " ".join([word for word in query.split() if word.lower() not in common_words])

        #  Create a pattern to match any of the words in the query
        pattern = re.compile("|".join( word for word in query.split()), re.IGNORECASE)

        return [movie for movie in movies if pattern.search(movie)]

