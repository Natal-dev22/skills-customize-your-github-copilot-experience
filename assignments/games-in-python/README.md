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
- Track the letters the player has guessed and set a maximum number of incorrect guesses.
- Show the hidden word as underscores, revealing any letters the player has guessed correctly.


### 🛠️ Implement the Guessing Game

#### Description
Let the player guess letters, update the displayed word and remaining attempts, and end the game with the appropriate result.

#### Requirements
Completed program should:

- Prompt the player to enter a letter and check whether it appears in the hidden word.
- Update and display the word's progress after each guess, along with the number of incorrect guesses remaining.
- End when the player guesses the word or reaches the incorrect-guess limit, then display a win or loss message. If the player loses, reveal the hidden word.
