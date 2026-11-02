# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic word-guessing game in Python to practice strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Use the provided starter code to choose a hidden word and prepare the game state before asking the player to guess.

#### Requirements
Completed program should:

- Randomly select a word from the provided `words` list.
- Initialize an empty collection of guessed letters and set the incorrect-guess limit to 6.
- Display one underscore for each letter in the hidden word, revealing correctly guessed letters.


### 🛠️ Implement the Guessing Game

#### Description
Let the player guess letters, update the displayed word and remaining attempts, and end the game with the appropriate result.

#### Requirements
Completed program should:

- Prompt the player to enter a letter and check whether it appears in the hidden word.
- Record each guess, count incorrect guesses toward the six-guess limit, and do not count a repeated guess more than once.
- After each guess, display the word's progress and the number of incorrect guesses remaining.
- End when the player guesses every letter or reaches six incorrect guesses. Display a win or loss message and reveal the hidden word if the player loses.
