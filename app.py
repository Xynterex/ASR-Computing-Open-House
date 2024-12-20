from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# create a list the 8 image file names (sch logo, 4 house mascots, stem cca, guitar ensemble, taekwondo)
# will refer to the colours flask app from old computing task to style the table

answer_table = [] # table of the names of image files
game_table = [] # table with 4 rows 4 cols of None data; to be processed by jinja during game
tries = 0 # number of attempts at guessing
row_col = [] # list storing

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
    # extend image names list by itself and shuffle
    # fill the list contents into 2d array for table display later
    return redirect("/game")

@app.route("/process_game")
def process_game():
    # check for duplicate guesses
    # check if both guesses are the same image names from answer_table
    # update game_table with the image names if guessed correctly (add image names from answer_table)
    # update rol_col (remove row_col pairs that have been guessed already)
    # check if any more None in game_table (to see if all images have been guessed correctly)
    return redirect("/game")

if __name__ == "__main__":
    app.run(debug=True, port=7777)
