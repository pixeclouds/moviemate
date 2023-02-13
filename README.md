# Moviemate

## Description
MovieMate is an interactive and immersive command-line text based video streaming platform. The platform has a custom-built adaptive and intuitive recommendation engine.

## User guide
Below is a short explainer on how the platform works.

- Upon running, the user is prompted with a list of commands to enter to change to the corrresponding menu mode.With **s** for enter search, **w** for watch , **r** for recommendation, **h** for homepage modes respectively.

- Entering **s** command takes the user to the search mode. Here the user is then prompted to enter the search query. Movies that match or are similar to the query are returned in the result.

- **h** takes the user to home. Here, a list of randomly selected movies is displayed. The can then switch to the watch console to watch any movie that picked his interest.

- Entering **w** command takes the user to the watch console. Here the user enter the name of the movie he wishes to watch. Note that the name of the movie should match the one on the database or as displayed. The name is NOT case sensitive.

- **r** runs the recommendation engine which returns a list of recommended movies. The recommendation is based on the genres and watch time of all watched movies. To give more context, a user watched a 50 minutes crime movie up till the 30 minutes mark and then watched a 50 romance movie only up till 22 minutes mark. The engine will recommend more of crime movies than romance. Pls note that the enigine is more complex than this simplified context.


## How to install and run
Fork this repo to run the program locally on your machine. You will need to activate a virtaul environment . To do this run following commands in your terminal.
```
python -m venv venv
venv/Scripts/activate
```

Install external libraries
```
pip install -r requirements.txt
```
Run the program
```
py main.py
```
