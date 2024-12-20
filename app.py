from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# create a list the 8 image file names (sch logo, 4 house mascots, stem cca, guitar ensemble, taekwondo)
# will refer to the colours flask app from old computing task to style the table
answer_table = [] # table of the names of image files
game_table = [] # table with 4 rows 4 cols of None data; to be processed by jinja during game

@app.route("/")
def lobby():
  return render_template("lobby.html")

@app.route("/prep_game")
def prep_game():
  # extend image names list by itself and shuffle
  # fill the list contents into 2d array for table display later
  return render_template("game.html")

if __name__ == "__main__":
  app.run(debug=True, port=7777)
