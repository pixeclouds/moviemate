from dataclasses import dataclass
import time
from simple_colors import *


'''
This class handles movie watching.
Other methods and properties defined in other
classes can be accessed in this class by inheritance.
......
- want_to_watch() property is defined in the Interface class.
- watched_movies property is defined in the Data class. 
- check_movie_in_db() attribute is defined in the Data class
'''
@dataclass
class Watch:

    # Display a TV representation
    def load_tv(self):
            print("---------------") 
            print("||           ||","\n||           ||","\n||           ||", )
            print("------+--+-----")
            print("---------------")

    # Prompts user to enter movie name he intends to watch
    def which_movie(self):
        title = input(yellow("Movie title: ", "bold")).strip()
        self.watch_movie(title)

    # Simulate movie watching
    def watch_movie(self, title):
        movie = self.check_movie_in_db(title)
        if movie:
            title = movie["title"]
            self.load_tv()
            print(magenta(f"Watching movie....{title}", "bold"))
            
            # Run and track watch time
            for i in range(1, movie["runtime"]):
                # Simulate transition 
                time.sleep(0.5)
                
                movie["watchtime"] = i
                print(cyan(f"watching...: {i} mins", "italic"))
                if i % 10 == 0:
                    print(f"{i} minufes passed")
                    # Should uer lose interest in the movie being streamed, 
                    # prompt comes up to terminate the movie
                    stop = input(red("stop movie y/n :", "bold"))
                    if stop == "y":
                        movie["watchtime"] = i
                        break
            # Add the just watched movie to watch history 
            self.watched_movies.append(movie)
        self.want_to_watch()

