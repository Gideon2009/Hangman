def hangman(word):
  # Explaining the rules
  print("Welcome to Hangman! You have guesses to figure out the correct word. Good luck!")
  lettersInWord = set()
  # Making the set of correct letters
  for letter in word:
    lettersInWord.add(letter)
  # The set of user's correct guesses
  correctGuesses = set()
  # Having the user make guesses
  for i in range(len(word) + 4, -1, -1):
    # Checking if the user has run out of guesses
    if i == 0:
      print("Sorry, you lose! The correct answer was " + str(word) + ".")
      break
    # Making a loop so that the number of guesses remaining only lowers if they get it wrong
    while True:
      # Saying how many guesses the user has remaining
      guess = input("Guess a letter! You have " + str(i) + " guesses remaining. ")
      # If the guess a word checking if it's right
      if guess == word:
        print("Congratulations! You win!")
        break
      # Checking if the letter is in the word
      elif guess in word:
        correctGuesses.add(guess)
      guesses = ""
      # Making the variable for word they have so far
      for x in word:
        if x in correctGuesses:
          guesses += x + " "
        else:
          guesses += "_ "
      # Printing out the word they have so far
      print(guesses + "\n")
      if guess not in word:
        break
      # Checking if the have won
      if len(correctGuesses) == len(lettersInWord):
        print("Congratulations! You win!")
        break
