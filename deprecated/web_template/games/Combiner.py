from collections import Counter
import random


class Combiner:
    def __init__(self, path: str) -> None:
        with open(path, 'r', encoding="utf-8") as f:
            self.dictionary = set(f.read().split('\n'))
            self.word = "WORD"
            self.solutions = set()

    def find_solutions(self, word='') -> list[str]:
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

    def set_word(self, word="", rnd=False) -> None:
        if rnd:
            self.word = random.choice(list(self.dictionary))
        else:
            self.word = word
        print(f"Selected word is {self.word}")
        self.solutions = self.find_solutions()
        print(self.solutions)
        print(f"There are {len(self.solutions)} solutions")

    def guess(self, word):
        if word in self.solutions:
            self.solutions.remove(word)
            if len(self.solutions) == 0:
                print("You won!")
                return
            print(f"Yes! {len(self.solutions)} more")
            return True
        else:
            print(f"Lol there is no {word} in {self.word}")
        return False


if __name__ == "__main__":
    c = Combiner("russian_nouns.txt")
    c.set_word(word="патриот")
    while True:
        c.guess(input("Your word: "))
