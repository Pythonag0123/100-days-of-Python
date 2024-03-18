import random

words = ["Max", "Charles", "Carlos", "Hamilton", "Toto", "Perez", "Sooki", "Pierre", "Daniel", "Bottas", "Iceman", "Alonso", "Seb", "Michael"]
WORD = random.choice(words)
a = '_' * len(WORD)
print(a)
WORD = WORD.lower()
incorrect_guesses = 0

while '_' in a:
    n = input("Guess a letter: ").lower()
    if n in WORD:
        for i in range(len(WORD)):
            if WORD[i] == n:
                a = a[:i] + n + a[i+1:]
        print(a)
    else:
        incorrect_guesses += 1
        print("Incorrect guess. Try again.")
        if incorrect_guesses >= 6:
            print("Sorry, you lost. The word was:", WORD)
            break

if '_' not in a:
    print("Congratulations! You guessed the word correctly:", WORD)
