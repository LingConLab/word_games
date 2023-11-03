def wordle(dictionary: str, alphabet: str, size: int, tries: int, direction: str,
           nothing_to_delete_error: str, no_word_in_dictionary_error: str,
           word_is_too_short_error: str, word_is_too_long_error: str,
           victory_outcome: str, lose_outcome: str):
    """
    Wordle is a word puzzle game that challenges players to guess a hidden word within a limited number of attempts. When player starts a new game, they are presented with a blank space where they can input your guesses. Player can type in a word of the same length as hidden word as their guess, and the game provides feedback on each letter's position in the hidden word.

    Wordle requires a bunch of arguments:

    :dictionary:, an argument of string type whose value is a path to csv file containing words and organised in the next way:
        word_1, word_2, etc.
    :keyboard:, an argument of string type whose value is a path to csv file containing lines of symbols to build a keyboard with them and organised in the next way:
        qwertyuiop, asdfghjkl, etc.
    :size:, an argument of integer type whose value will define the lengрt of hidden words and, therefore, of all words that can be entered

    :number of tries:, an argument of integer type whose value will define the number of attempts player will have unless game will conclude win or lose

    :direction:, an argument of string type whose value can be either "left_to_right" or "right_to_left". It defines the direction of writing system

    :nothing_to_delete_error:, an argument of string type whose value will be shown as alert on the player's screen, if they press backspace on empty word field

    :no_word_in_dictionary_error:, an argument of string type whose value will be shown as alert on the player's screen, if they try to enter a word not presented in dictionary

    :word_is_too_short_error:, an argument of string type whose value will be shown as alert on the player's screen, if they try to enter a word containing less letters then number in the size variable

    :word_is_too_long_error:, an argument of string type whose value will be shown as alert on the player's screen, if they press a keyboard letter button, when there are no empty cells in the word field

    :victory_outcome:, an argument of string type whose value will be shown as alert on the player's screen, if they manage to guess the hidden word in a number of attempts not exceeding the number in the tries variable

    :lose_outcome:, an argument of string type whose value will be shown as alert on the player's screen, if they don't manage to guess the hidden word in a number of attempts not exceeding the number in the tries variable
    """
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('src/word_games/templates'))
    template = env.get_template('wordle_template.html')
    rendered_template = template.render(dictionary=dictionary, alphabet=alphabet,
                                                  size=size, tries=tries, direction=direction,
                                                  nothing_to_delete_error=nothing_to_delete_error,
                                                  no_word_in_dictionary_error=no_word_in_dictionary_error,
                                                  word_is_too_short_error=word_is_too_short_error,
                                                  word_is_too_long_error=word_is_too_long_error,
                                                  victory_outcome=victory_outcome, lose_outcome=lose_outcome)

    with open("wordle.html", "w", encoding="utf-8") as file:
        print(rendered_template, file=file)


def combiner(dictionary: str, random_word: bool = True):
    """
    Combiner is a game whose essence is to find all the words that can be made up of the letters of the original word.

    Combiner requires two arguments:

    :dictionary: an argument of string type whose value is a path to csv file containing words and organised in the next way:
        word_1, word_2, etc.
    :random_word: an argument of boolean type. If it is set to True, source word will be chosen randomly on the start of game, otherwise it must be entered manually.
    """
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('src/word_games/templates'))
    template = env.get_template('combiner_template.html')
    rendered_template = template.render(dictionary=dictionary, random_word=random_word)

    with open("combiner.html", "w", encoding="utf-8") as file:
        print(rendered_template, file=file)
