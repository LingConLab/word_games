from flask import Flask
from flask import request
from flask.templating import render_template
from games.Combiner import Combiner

app = Flask(__name__)

c = Combiner("russian_nouns.txt")
c.set_word(word="качели")


@app.route('/', methods=['post', 'get'])
@app.route('/home', methods=['post', 'get'])
def home():
    if request.method == "POST":
        input_word = request.form.get("guess")
        if c.guess(input_word):
            return render_template('base.html', word="качели", guessed=1)
        else:
            return render_template('base.html', word="качели", guessed=0)
    return render_template('base.html', word="качели")


if __name__ == "__main__":
    app.run(debug=True)
