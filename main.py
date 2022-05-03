#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []

for _ in range(word_length):
 _ = display.insert(0, "_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


#Check user_word_selection letter
while display != (chosen_word):
  user_word_selection = input("Guess a letter associated with the mystery word: ").lower()
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter {letter}\n Guessed letter: {user_word_selection}")
    if letter == user_word_selection:
      display[position] = letter
    else:
      break

print(display)



