from games import wordle


wordle(dictionary="dictionary.csv", size=5, tries=6, alphabet="alphabet.csv", direction="left_to_right",
       nothing_to_delete_error="Кажется, Вам нечего удалять",
       no_word_in_dictionary_error="К сожалению, такого слова нет в словаре",
       word_is_too_short_error="Загаданое слово длиннее", word_is_too_long_error="Загаданое слово короче",
       victory_outcome="Вам удалось отгадать загаданное слово. Перезагрузите страницу, чтобы получить новое слово",
       lose_outcome="Вам не удалось отгадать загаданное слово. Перезагрузите страницу, чтобы попробовать снова", )
