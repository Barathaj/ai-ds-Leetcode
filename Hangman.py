import random
word_list = ["onakunallasavevarathuda","vaipuilladarajaa","donttriggerme","shootpanniduven"]
word = random.choice(word_list)
guess_word = "_" * len(word)
num_attempts = 6
guessed_letters = []
hang = [
    " _________\n|         |\n|         \n |\n|\n|\n|\n",
    " _________\n|         |\n|         O\n|\n|\n|\n|\n",
    " _________\n|         |\n|         O\n|         |\n|\n|\n|\n",
    " _________\n|         |\n|         O\n|        /|\n|\n|\n|\n",
    " _________\n|         |\n|         O\n|        /|\\\n|\n|\n|\n",
    " _________\n|         |\n|         O\n|        /|\\\n|        /\n|\n|\n",
    " _________\n|         |\n|         O\n|        /|\\\n|        / \\\n|\n|\n"
]
while num_attempts > 0 and guess_word != word:
    print("Answer:",guess_word,"\n")
    print("Attempts left:", num_attempts,"\n")
    print("Guessed letters:", guessed_letters,"\n")
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess. Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word = guess_word[:i] + guess + guess_word[i+1:]
    else:
   
        num_attempts -= 1
        print("Incorrect guess.")
        print(hang[6 - num_attempts])

if guess_word == word:
    print("Congratulations, nengal uyirudan irukalam. The word was", word)
else:
    print("Saavu Da (RIP)  ('_'). The word was", word)