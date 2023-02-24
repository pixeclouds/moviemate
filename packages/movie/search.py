from dataclasses import dataclass
import re
from simple_colors import *


'''
This class handles search queries.
Other methods and properties such as back_to_movie() defined in other
classes can be accessed by this class due by inheritance.
back_to_menu() and want_to_watch() are defined in the Interface class 
all_movies property is defined in the Data class
'''
@dataclass
class Search:
    
    # Handles the search result
    def search_for_movie(self):
        query = input(yellow("Search: ", "bold")).strip()
        result = self.run_search(query)
        print(cyan("\nSearch result..", "bold"))
        if result == []:
            print(red("Movie not found", "bold"))
            self.back_to_menu()
        else:
            print(*result, sep="\n")
        # self.back_to_menu()
        self.want_to_watch()

    # Clean up search query and Perform the actual search 
    def run_search(self, query):
        movies = [ movie["title"] for movie in self.all_movies]
        # Remove common words from the query
        common_words = ["on", "of", "the", "in", "and", "a"]
        query = " ".join([word for word in query.split() if word.lower() not in common_words])

        #  Create a pattern to match any of the words in the query
        pattern = re.compile("|".join( word for word in query.split()), re.IGNORECASE)

        return [movie for movie in movies if pattern.search(movie)]

