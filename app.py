from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

# create a list the 8 image file names (sch logo, 4 house mascots, stem cca, guitar ensemble, taekwondo)
image_names = ["ASR ARTEMIS LOGO.jpg", 
               "ASR ATHENA LOGO.jpg",
               "ASR GUITAR ENSEMBLE LOGO.jpg",
               "ASR HELIOS LOGO.jpg",
               "ASR OPEN HOUSE LOGO.png",
               "ASR POSEIDON LOGO.jpg",
               "ASR STEM LOGO.jpg",
               "ASR TAEKWONDO LOGO.jpg"]

# will use them like <img src="{{ image_name }}"> to show the images
# will refer to the colours flask app from old computing task to style the table

answer_table = [] # table of the names of image files, like the "answer key" that wouldn't get passed to frontend
game_table = [] # table with 4 rows 4 cols of None data; to be processed by jinja during game
tries = 0 # number of attempts at guessing
row_col = [] # list storing row-col pairs of each box

@app.route("/")
def lobby():
    return render_template("lobby.html")

@app.route("/game")
def game():
    global game_table
    global row_col
    return render_template("game.html", game_table=game_table, row_col=row_col)

@app.route("/prep_game")
def prep_game():
    # extend image names list by itself and shuffle (2 of each image names in the list)
    # fill the list contents into answer_table (2d array)
    global answer_table
    global game_table

    answer_list = image_names.copy() + image_names.copy()
    random.shuffle(answer_list)

    # fill into answer_table
    for i in range(4):
        answer_table.append(answer_list[i*4:(i + 1)*4])

    # fill None into game_table
    game_table = [[None for i in range(4)] for j in range(4)]
    
    return redirect("/game")

@app.route("/process_game")
def process_game():
    # check for duplicate guesses
    # check if both guesses are the same image names from answer_table
    # update game_table with the image names if guessed correctly (add image names from answer_table)
    # update rol_col (remove row_col pairs that have been guessed already)
    # check if any more None in game_table (to see if all images have been guessed correctly)
        # if so, redirect to /end_game
    return redirect("/game")

@app.route("/end_game")
def end_game():
    global answer_table

    return render_template("endgame.html", answer_table=answer_table)
    
if __name__ == "__main__":
    app.run(debug=True, port=7777)
