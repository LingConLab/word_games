from flask import Flask
from flask import request
from flask.templating import render_template
from games.Games import *


game = "GAME_MASK"

@app.route('/', methods=['post', 'get'])
@app.route('/home', methods=['post', 'get'])
def home():
    return render_template('base.html')


@app.route('/game', methods=['post', 'get'])
def play():
    if request.method == "POST":
        input_word = request.form.get("guess")
        return game.make_move(input_word)


if __name__ == "__main__":
    app.run(debug=True)
