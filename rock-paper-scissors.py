import random


def getchoices():
  player_choice = input("enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choices(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "scissors":
      return "Scissors cuts the paper! You lose"
    else:
      return "Paper covers rock! You win!"
  elif player == "scissors":
    if computer == "Rock":
      return "Rock smashes scissors. You lose."
    else:
      return "Scissors cuts the paper. You win!"
  else:
    return "You write wrong object please try again."


choices = getchoices()
result = check_win(choices["player"], choices["computer"])
print(result)
