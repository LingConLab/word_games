from flask import Flask
from flask import request
from flask.templating import render_template
from Games import *


game = "GAME_MASK"

game.start_game()

@app.route('/', methods=['post', 'get'])
@app.route('/home', methods=['post', 'get'])
def home():
    if request.method == "POST":
        input_word = request.form.get("guess")
        return game.make_move(input_word)
    return render_template('base.html', guessed_word=game.word)


@app.route('/game', methods=['post', 'get'])
def play():
    if request.method == "POST":
        input_word = request.form.get("guess")
        return game.make_move(input_word)


if __name__ == "__main__":
    app.run(debug=True)
