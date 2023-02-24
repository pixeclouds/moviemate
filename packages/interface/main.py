
from dataclasses import dataclass
from packages.movie.main import Movie
from packages.engine.main import Engine
from simple_colors import *


'''
This is the main class thet runs the program. It handles menu selection.
It also inherits Engine and Movies class thus allowing the program to run
seamlessly on a single instantiation
'''
@dataclass
class Interface(Engine, Movie):

    def welcome(self):
        # load_data() attribute is declared in Data class, a parent class to Movie
        self.load_data()
        print(magenta("Welcome to Moviemate, Enter the corresponding command to enter menu mode","bold")) 
        print(blue("\nWatch Movie -> w, \nSearch for Movie -> s \nGo to Home page -> h \nRecommend movies -> r", "italic"))
        self.show_menu()

    # Prompt user to enter desired menu mode
    def show_menu(self):
        menu = input(green("\nChoose Menu [s/h/w/r]: ", "bold")).strip()
        self.choose_menu(menu)

    def choose_menu(self, menu):
        if  menu == "h":
            self.display_movies()
        elif menu == "w":
            self.which_movie()
        elif  menu == "s":
            self.search_for_movie()
        elif menu == "r":
            self.get_recommendation()
        else:
            print(red("Invalid command...try again", "bold"))
            self.show_menu()
    # Returns user back to the main menu
    def back_to_menu(self):
        res = input(blue("Do you want to go back to the menu [y/n]: ", "bold")).strip()

        if res == "y":
            self.show_menu()
        elif res == "n":
            pass
            res = input(red("Do you want to exit MovieMate [y/n]: ", "bold"))
            if res  == "y":
                print(green("\nGoodbye...See you soon", ["bold", "italic"]))
            else:
                self.back_to_menu()
        else:
            print(red("Invalid command. Try again", "bold"))
            self.back_to_menu()

    def want_to_watch(self):
        res = input(magenta("\nDo you want to watch movie [y/n]: ", "bold")).strip()
        if res == "y":
            self.which_movie()
        elif res == "n":
            self.back_to_menu()
        else:
            print(red("Invalid command. Try again", "bold"))
            self.want_to_watch()



