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
    global tries
    global game_table
    global row_col
    
    return render_template("game.html", game_table=game_table, row_col=row_col, tries=tries)

@app.route("/prep_game")
def prep_game():
    # extend image names list by itself and shuffle (2 of each image names in the list)
    # fill the list contents into answer_table (2d array)
    global answer_table
    global game_table
    global row_col
    global tries

    tries = 0 # reset tries
    answer_list = image_names.copy() + image_names.copy()
    random.shuffle(answer_list)

    # fill into answer_table
    for i in range(4):
        answer_table.append(answer_list[i*4:(i + 1)*4])

    # fill None into game_table
    game_table = [[None for i in range(4)] for j in range(4)]

    # row_col list
    row_col = ["A1", "A2", "A3", "A4",
               "B1", "B2", "B3", "B4",
               "C1", "C2", "C3", "C4",
               "D1", "D2", "D3", "D4"]
    
    return redirect("/game")

@app.route("/process_game", methods=["POST"])
def process_game():
    global game_table
    global answer_table
    global row_col
    global tries

    tries += 1
    
    guess1 = request.form.get("guess1")
    guess2 = request.form.get("guess2")

    # check for duplicate guesses
    if guess1 == guess2:
        return redirect("/game")

    # check if both guesses are the same image names from answer_table
    # obtain indexes of row and col
    col1, row1= "ABCD".index(guess1[0]), int(guess1[1]) - 1
    col2, row2= "ABCD".index(guess2[0]), int(guess2[1]) - 1

    # check if both guesses are the same image names from answer_table
    if answer_table[row1][col1] == answer_table[row2][col2]: # guesses are the same
        # update game_table with the image names if guessed correctly (add image names from answer_table)
        game_table[row1][col1] = answer_table[row1][col1]
        game_table[row2][col2] = answer_table[row2][col2]
        
        # update rol_col (remove row_col pairs that have been guessed already)
        row_col.remove(guess1)
        row_col.remove(guess2)
        # check if any more data in row_col
        if len(row_col) == 0:
            # if so, redirect to /end_game
            return redirect("/end_game")
        else:
            return redirect("/game")

    # expose the cards if wrongly guessed
    return redirect(url_for("expose", row1=row1, col1=col1, row2=row2, col2=col2))

@app.route("/expose")
def expose():
    global answer_table
    row1 = int(request.args.get("row1"))
    col1 = int(request.args.get("col1"))
    row2 = int(request.args.get("row2"))
    col2 = int(request.args.get("col2"))
    
    expose_table = [[None for i in range(4)] for j in range(4)]
    
    expose_table[row1][col1] = answer_table[row1][col1]
    expose_table[row2][col2] = answer_table[row2][col2]

    return render_template("expose.html", expose_table = expose_table)

@app.route("/end_game")
def end_game():
    global answer_table
    global tries

    return render_template("endgame.html", answer_table=answer_table, tries=tries)
    
if __name__ == "__main__":
    app.run(debug=True, port=7777)
