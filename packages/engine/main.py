from dataclasses import dataclass
import random
from simple_colors import *


'''
This class runs the recommendation engine of the program. 
Due to multiple inheritance in the Interface class,
the Engine class can access the following methods and properties
as referenced below
- all_movies and watched_movies properties declared in the Data class of the movie package 
- Formatter() method defined in the Data class
- want_to_watch() method defined in the Interface class

'''
       
@dataclass
class Engine:
    
    # Calculate the watch/runtime ratio for the wachted movies. 
    # This ratio is an important parameter for the recommendation algorithm 
    def get_watch_time_ratio(self, movie):
        ratio = movie["watchtime"] / movie["runtime"]
        return ratio

    # Calculate similarity score for each yet to be watched movie as 
    # compared against all movies in the user watch history
    def get_movie_similarity(self, movie1, movie2):
        # Calculate similarity based on genre match
        genre_similarity = len(set(movie1["genres"]) & set(movie2["genres"])) 

        # Calculate similarity based on watch time/runtime ratio
        ratio_similarity = self.get_watch_time_ratio(movie2)

        # Combine the similarities into a single value
        similarity = genre_similarity + ratio_similarity
        return similarity

    # Recommends the top 5 movies with the highest similarity score
    def recommend_movies(self):
        num_recommendations = 5
        all_movies = self.all_movies
        watched_movies = self.watched_movies

        # Calculate similarity between each movie and the previously watched movies
        similarity_scores = []
        for movie in all_movies:
            # skip movies already watched
            if movie["title"] in [movie["title"] for movie in watched_movies ]:
                continue
            score = sum([self.get_movie_similarity(movie, watched) for watched in watched_movies])

            # uncomment the line below to examine the calculated similarity scores
            # print("Movie: ", movie["title"], "|| Similarity score: ", score, "\n")
            similarity_scores.append((movie, score))

        # Sort movies by similarity
        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        # Return the top 5 movies
        return [movie for movie, _ in similarity_scores[:num_recommendations]]

    def get_recommendation(self):
        recommendation = self.recommend_movies()
        recommendation = [self.formatter(movie) for movie in recommendation]
        print(yellow("\nMovie Recommendations...", "bold"))
        print(*recommendation, sep="\n\n")
        self.want_to_watch()





