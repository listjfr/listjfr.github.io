#HANGMAN
"""Note: if same letter guessed twice, that turn is used up"""
print("Welcome to Hangman!")
repeat = "y"

while (repeat == "y"):
  
  #user prompt
  word = (input("Pick a word: ")).lower()
  max_guesses = int(input("Enter the maximum number of guesses: "))
  blank = ["_ "] * len(word)
  print (" ".join(blank))
  print (" ")
  wrong_letters = []
  correct_letters = []
  correct = 0
  guesses = 0
  wrong = 0
  
  #guess
  for x in range(max_guesses):
    guesses += 1
    letter = input("Guess # " + str(guesses) + ". Guess a letter: ")
    
    #check if letter already used
    if letter in (correct_letters or wrong_letters):
      print ("You already used that letter!\n")
    else:
      #check if letter in word
      for i in range(len(word)):
        if letter == word[i]:
          blank[i] = letter
          correct_letters.append(letter)
          correct +=1
      
      #if letter not in word
      if letter not in word:
        print("Letter not in word. Try Again.")
        wrong += 1
        wrong_letters.append(letter)
      
      #print guess so far
      print (" ")
      print (" ".join(blank))
      print ("Correct: " + str(correct))
      print ("Wrong: " + str(wrong))
      print ( "Wrong letters: " + " ".join(wrong_letters))
      print (" ")
      
      #if correct answer before max guesses
      if (correct == len(word)):
        break
    
  #game result
  if (correct == len(word)):
    print ("Congratulations. You Win!")
  elif guesses == max_guesses:
    print ("Game Over. Number of maximum guesses reached. You Lose!")
    print ("Answer: " + word)
  else:
    print ("Error!")
    
  repeat = (input("Would you like to play again? Enter Y to play again or N to exit --> ")).lower()
