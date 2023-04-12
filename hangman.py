import random
with open ("e:\Projects\py\hangman\words.txt", "r") as myfile:
    lines = myfile.read().splitlines()
print()
print("Ready to play hang-man.")
print("you have 7 guesses from the start. start guessing.")
print()
life=7
firstflag=True
usedLetter=["",]
randomWord =random.choice(lines) # pick up a random item in this list
done=len(randomWord)
word_as_list=list(randomWord)
while True:
    
    if (firstflag==False):
        print(f"Used letter(s): {usedLetter}")
        guess=input(f"You have {life} guesses left. Guess a word to fill the blanks: ")
        if (guess not in usedLetter):
            usedLetter.append(guess)
            if (guess not in word_as_list):
                life-=1
        else:
            print("Dont guess something you already guessed.")

    firstflag=False

    for i in range(len(randomWord)):
        if(randomWord[i] in usedLetter):
            print(randomWord[i], end="")
        else:
            print("_", end="")
    print()
    print()
    if set(word_as_list).intersection(set(usedLetter))==set(word_as_list):
        print(f"Congratualtions! You have won the game. The word was {randomWord}")
        exit()
    if (life==0):
        print(f"Sorry, you ran out of the guesses. the word was {randomWord}")
        exit()