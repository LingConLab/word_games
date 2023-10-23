def wordle(dictionary: str, alphabet: str, size: int, tries: int, direction: str,
           nothing_to_delete_error: str, no_word_in_dictionary_error: str,
           word_is_too_short_error: str, word_is_too_long_error: str,
           victory_outcome: str, lose_outcome: str):
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('templates/wordle_template.html')
    rendered_template = template.render(dictionary=dictionary, alphabet=alphabet,
                                                  size=size, tries=tries, direction=direction,
                                                  nothing_to_delete_error=nothing_to_delete_error,
                                                  no_word_in_dictionary_error=no_word_in_dictionary_error,
                                                  word_is_too_short_error=word_is_too_short_error,
                                                  word_is_too_long_error=word_is_too_long_error,
                                                  victory_outcome=victory_outcome, lose_outcome=lose_outcome)

    with open("wordle.html", "w", encoding="utf-8") as file:
        print(rendered_template, file=file)


def combiner(dictionary: str, random_word: bool):
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('templates/combiner_template.html')
    rendered_template = template.render(dictionary=dictionary, random_word=random_word)

    with open("combiner.html", "w", encoding="utf-8") as file:
        print(rendered_template, file=file)
