# word_games

Python package for creating language games from your own data. It consists of a set of functions that via jinja2 render HTML files containing various games using existing templates and provided dictionaries. The games themselves function as brython code inside an html file.

# Quick start

Import the function responsible for generating the game you need:\
`from wordle import wordle`

Call it and pass all the required arguments:
```
wordle(dictionary="dictionary.json", size=5, tries=6, alphabet="alphabet.json", direction="left_to_right",
       nothing_to_delete_error="Кажется, Вам нечего удалять",
       no_word_in_dictionary_error="К сожалению, такого слова нет в словаре",
       word_is_too_short_error="Загаданое слово длиннее", word_is_too_long_error="Загаданое слово короче",
       victory_outcome="Вам удалось отгадать загаданное слово. Перезагрузите страницу, чтобы получить новое слово",
       lose_outcome="Вам не удалось отгадать загаданное слово. Перезагрузите страницу, чтобы попробовать снова", )
```

It will spawn a ready html file with game that now can be placed on server.
