from dataclasses import dataclass
import random
from simple_colors import *


       
@dataclass
class Engine:
    
    def get_watch_time_ratio(self, movie):
        ratio = movie["watchtime"] / movie["runtime"]
        return ratio


    def get_movie_similarity(self, movie1, movie2):
        # Calculate similarity based on genre match
        genre_similarity = len(set(movie1["genres"]) & set(movie2["genres"])) 

        # Calculate similarity based on watch time/runtime ratio
        ratio_similarity = self.get_watch_time_ratio(movie2)

        # Combine the similarities into a single value
        similarity = genre_similarity + ratio_similarity
        return similarity


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

            # print("Movie: ", movie["title"], "|| Similarity score: ", score, "\n")
            similarity_scores.append((movie, score))

        # Sort movies by similarity
        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        # Return the top 5 movies
        return [movie for movie, _ in similarity_scores[:num_recommendations]]

    def get_recommendation(self):
        recommendation = self.recommend_movies()
        print(yellow("\nMovies you might like  to watch..", "bold"))
        print(*recommendation, sep="\n")
        self.want_to_watch()





