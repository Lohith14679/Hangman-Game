import random

def choose_word():
    words = ['python', 'hangman', 'developer', 'programming', 'keyboard', 'laptop']
    return random.choice(words)

def display(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    guessed_word = False

    print("Welcome to Hangman!")

    while attempts > 0 and not guessed_word:
        print("\nWord:", display(word, guessed_letters))
        print(f"You have {attempts} attempts left.")
        guess = input("Enter a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")


hangman()
