from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# create a list the 8 image files (sch logo, 4 house mascots, stem cca, guitar ensemble, taekwondo)
# extend list by itself and shuffle
# fill the list contents into 2d array for table display later
# will refer to the colours flask app from old computing task to style the table

@app.route("/")
def lobby():
  return render_template("lobby.html")

if __name__ == "__main__":
  app.run(debug=True, port=7777)
