from dataclasses import dataclass
import time
from simple_colors import *

@dataclass
class Watch:

    # Display TV
    def load_tv(self):
            # print("---------------")
            print("***************")
            # print("*             *", "\n*             *", "\n*             *", "\n*             *")
            
            print("||           ||","\n||           ||","\n||           ||", )
            # print("------+--+-----")
            print("**************")

            # print("---------------")

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
                    # time.sleep(5)
                    stop = input(red("stop movie y/n :", "bold"))
                    if stop == "y":
                        movie["watchtime"] = i
                        break
                        
            self.watched_movies.append(movie)
        self.want_to_watch()

