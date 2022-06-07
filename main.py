import random
input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
print()
player_wins = 0
cpu_wins = 0

choices = ["r", "p", "s"]

while True:
  random_index = random.randint(0,2)
  cpu_choice = choices[random_index]
  
  player_choice = input("Rock, Paper, or Scissors? Enter R for Rock, P for Paper or S for Scissors ").lower()
  while player_choice not in choices:
    player_choice = input("Not a valid choice. Try again: ").lower()
      
  print()
  print("Player", "(", player_choice, ")" " : CPU", "(", cpu_choice, ")")
  print()
  
  if player_choice == 'r':
    if cpu_choice == 'r':
      print("It's a tie, Enter Y to play again")
    elif cpu_choice == 's':
      print("You win!")
      player_wins+=1
    elif cpu_choice == 'p':
      print("You lose!")
      cpu_wins+=1
  elif player_choice == 'p':
    if cpu_choice == 'p':
      print("It's a tie, Enter Y to play again")
    elif cpu_choice == 'r':
      print("You win!")
      player_wins+=1
    elif cpu_choice == 's':
      print("You lose!")
      cpu_wins+=1
  elif player_choice == 's':
    if cpu_choice == 's':
      print("It's a tie, Enter Y to play again")
    elif cpu_choice == 'p':
      print("You win!")
      player_wins+=1
    elif cpu_choice == 'r':
      print("You lose!")
      cpu_wins+=1
    
  print()
  print("You have "+str(player_wins)+" wins")
  print("The computer has "+str(cpu_wins)+" wins")
  print()
  
  repeat = input("Do you want to play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("Not a valid choice. Try again: ").lower()
      
  if repeat == 'n':
    break
    
print("Come and player another time")
