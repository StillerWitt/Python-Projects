word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
play_hangman(chosen_word)

import random

def create_display(word):
    return ["_" for _ in range(len(word))]

def update_display(guess, display, word):
    for i in range(len(word)):
        if guess == word[i]:
            display[i] = guess
    return display

def play_hangman(word):
    lives = 6
    display = create_display(word)
    stages = {
        0: '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''',
        1: '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''',
        2: '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''',
        3: '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''',
        4: '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''',
        5: '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''',
        6: '''
          +---+
          |   |
              |
              |
              |
              |
        ========='''
    }

    while True:
        print(stages[lives])
        print(f"{' '.join(display)}")
        guess = input("Guess a letter: ").lower()
        display = update_display(guess, display, word)
        if guess not in word:
            lives -= 1
            if lives == 0:
                print("You lose.")
                break
        if "_" not in display:
            print("You win.")
            break


