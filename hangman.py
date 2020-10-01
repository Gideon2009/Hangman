def hangman(word):
  print("Welcome to Hangman! You have 15 guesses to figure out the correct word. Good luck!")
  lettersInWord = set()
  for letter in word:
    lettersInWord.add(letter)
  correctGuesses = set()
  for i in range(len(word) + 4, -1, -1):
    if i == 0:
      print("Sorry, you lose! The correct answer was " + str(word) + ".")
      break
    guess = input("Guess a letter! You have " + str(i) + " guesses remaining. ")
    if guess in word:
      correctGuesses.add(guess)
    guesses = ""
    for x in word:
      if x in correctGuesses:
        guesses += x + " "
      else:
        guesses += "_ "
    print(guesses + "\n")
    if len(correctGuesses) == len(lettersInWord):
      print("Congratulations! You win!")
      break
