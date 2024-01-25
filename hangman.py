import random as rand
life = 6
words = ["english", "fun", "run", "word", "games", "tryhard", "funny", "pain", "list", "coding", "math", "person", "table", "essay", "hangman", "writing", "firetruck"]
userguesses = []


word = rand.choice(words)
wordlist = list(word)
wordlen = len(word)

while life > 0:

    display = ''.join(i if i in userguesses else "_" for i in word)
    if display == word:
        print(f"You won! The word was {word}!")
        break
    print(display)

    guess = input("What letter do you guess? ").lower()

    if guess in userguesses:
        print("You already guessed this letter, try something else.")
    elif guess in wordlist:
        print (f"Yes, the letter {guess} is in the word!")
        userguesses.append(guess)
    elif guess not in wordlist:
        print (f"No, the letter {guess} is not in the word!")
        life = life - 1
        print (f"You have {life} live(s) left.")
        userguesses.append(guess)
        
    
if life == 0:
    print (f"The word was: {word}")