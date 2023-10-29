# What is it?

Python package for creating language games from your own data. It consists of a set of functions that render HTML files containing various games using existing templates and provided dictionaries.

# Installation

Installer is available at the Python Package Index
```
pip install word_games
```

# Usage

Import the function responsible for generating the game you need:\
`from word_games import wordle`

Call it and pass all the required arguments. For instance, Wordle requires a dictionary and a keyboard files, size of hidden words and, therefore, of all words that can be entered, number of tries player will have in game, direction of writing system of the game's language and finally some alerts texts:
```
wordle(dictionary="dictionary.json", size=5, tries=6, alphabet="alphabet.json", direction="left_to_right",
       nothing_to_delete_error="Seems, you have nothing to delete",
       no_word_in_dictionary_error="There is no word to delete",
       word_is_too_short_error="Hidden word is longer", word_is_too_long_error="Hidden word is shorter",
       victory_outcome="You have successfully guessed the hidden word. Reload the page to try again",
       lose_outcome="You failed to guess the hidden word. Reload the page to try again", )
```

It will spawn a ready html file with game that now can be placed on server.

Some of the requirements can be altered for different games, other such as dictionary, alphabet and direction are necessary for all games. All the requiremets for the specific game can be seen through help function:
```
help(wordle)
```

# License

[LICENSE](https://github.com/LingConLab/word_games/blob/main/LICENSE)
