import random
from collections import Counter
from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)


class Game:
    def __init__(self, dictionary_path: str) -> None:
        try:
            with open(dictionary_path, 'r', encoding="utf-8") as f:
                self.dictionary = set(f.read().split('\n'))
        except FileNotFoundError as e:
            print(
                f"File {dictionary_path} is not found! Check the path or filename.")
            return

        self.word = None
        self.solutions = None

    def start_game(self):
        pass

    def set_word(self, word="", rnd=False):
        if rnd:
            self.word = random.choice(list(self.dictionary))
        else:
            self.word = word

    def make_move(self, word):
        if word in self.solutions:
            self.solutions.remove(word)
            if len(self.solutions) == 0:
                self.end_game()
                return True
            return True
        else:
            return False

    def end_game(self):
        print("You won!")

    def flask_handler(self):
        pass


class Combiner(Game):
    def __init__(self, dictionary_path: str) -> None:
        super().__init__(dictionary_path)

    def start_game(self):
        super().start_game()
        super().set_word(word="TEST")
        print(f"Selected word is {self.word}")
        self.solutions = self.__find_solutions(self.word)

    def make_move(self, word: str):
        if super().make_move(word=word):
            return render_template('base.html', guessed_word=self.word, guessed=1)
        else:
            return render_template('base.html', guessed_word=self.word, guessed=0)


    def flask_handler(self):
        super().flask_handler()

    def __find_solutions(self, word='') -> list[str]:
        """
        Takes a word as an input and finds all the words that can be combined from the letters of the original word.
        Example: `"шинель" -> ["лень", "лен", "нил", "лишь"]`
        """

        if not word:
            word = self.word

        variants: list[str] = self.dictionary
        solutions = []
        orig_letters = dict(Counter(word))
        for w in variants:
            if w == self.word:
                continue
            # at this step we remove all words that either bigger or has letters that don't present in original word
            if len(w) > len(word) or len(set(w) - orig_letters.keys()) != 0:
                continue

            for letter in dict(Counter(w)):
                if orig_letters[letter] - dict(Counter(w))[letter] < 0:
                    break
            else:
                solutions.append(w)

        return solutions
