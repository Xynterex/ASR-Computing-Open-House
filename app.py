from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def lobby():
  return render_template("lobby.html")

if __name__ == "__main__":
  app.run(debug=True, port=7777)
