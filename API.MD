# Combiner

Combiner is a game whose essence is to find all the words that can be made up of the letters of the original word.

Combiner requires two arguments:

1. dictionary, an argument of string type whose value is a path to csv file containing words and organised in the next way:

```
word_1, word_2, etc.
```

2. random_word, an argument of boolean type. If it is set to True, source word will be chosen randomly on the start of game, otherwise it must be entered manually.

# Wordle

Wordle is a word puzzle game that challenges players to guess a hidden word within a limited number of attempts. When player starts a new game, they are presented with a blank space where they can input your guesses. Player can type in a word of the same length as hidden word as their guess, and the game provides feedback on each letter's position in the hidden word.

Wordle requires a bunch of arguments:

1. dictionary, an argument of string type whose value is a path to csv file containing words and organised in the next way:

```
word_1, word_2, etc.
```

2. keyboard, an argument of string type whose value is a path to csv file containing lines of symbols to build a keyboard with them and organised in the next way:

```
qwertyuiop, asdfghjkl, etc.
```

3. size, an argument of integer type whose value will define the lengрt of hidden words and, therefore, of all words that can be entered

4. number of tries, an argument of integer type whose value will define the number of attempts player will have unless game will conclude win or lose

5. direction, an argument of string type whose value can be either "left_to_right" or "right_to_left". It defines the direction of writing system

6. nothing_to_delete_error, an argument of string type whose value will be shown as alert on the player's screen, if they press backspace on empty word field

7. no_word_in_dictionary_error, an argument of string type whose value will be shown as alert on the player's screen, if they try to enter a word not presented in dictionary

8. word_is_too_short_error, an argument of string type whose value will be shown as alert on the player's screen, if they try to enter a word containing less letters then number in the size variable

9. word_is_too_long_error, an argument of string type whose value will be shown as alert on the player's screen, if they press a keyboard letter button, when there are no empty cells in the word field

10. victory_outcome, an argument of string type whose value will be shown as alert on the player's screen, if they manage to guess the hidden word in a number of attempts not exceeding the number in the tries variable

11. lose_outcome, an argument of string type whose value will be shown as alert on the player's screen, if they don't manage to guess the hidden word in a number of attempts not exceeding the number in the tries variable
