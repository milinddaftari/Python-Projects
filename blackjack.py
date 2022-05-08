from art import logo
from os import system, name
import random

deck = {
  "A": 11,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10,
}

def deal_cards(hand):
  hand = hand.append(random.choice(list(deck)))


def is_blackjack(user_hand, dealers_hand):
  user_count = 0
  dealer_count = 0
  for hand in user_hand:
    if deck[hand] == 11 or deck[hand] == 10:
      user_count += deck[hand]
  for hand in dealers_hand:
    if deck[hand] == 11 or deck[hand] == 10:
      dealer_count += deck[hand]

  if user_count == 21 and dealer_count == 21:
    print("BLACKJACK: COMPUTER WINS")
    return True
  elif (user_count == 21) and (user_count > dealer_count):
    print("BLACKJACK: USER WINS")
    return True
  elif (dealer_count == 21) and (dealer_count > user_count):
    print("BLACKJACK: COMPUTER WINS")
    return True
  else:
    return False
  

def calculate_score(user_hand, dealers_hand):
  users_score = 0
  dealers_score = 0

  for hand in user_hand:
    if hand == "A" and ((users_score + 11) > 21):
      users_score += 1
    else:
      users_score += deck[hand]
  print(f"User's score {users_score}")
  for hand in dealers_hand:
    if hand == "A" and dealers_score > 21:
      dealers_score += 1
    else:
      dealers_score += deck[hand]
  print(f"Computer's partial score {deck[dealers_hand[0]]}")
  return users_score,dealers_score

def play_again_choice(play_again):
  play_again_choice_selection = input("GAME OVER - Do you want to play again (Y / N): ")
  if play_again_choice_selection.upper() == "Y":
    play_again = True
  elif play_again_choice_selection.upper() == "N":
    play_again = False
  else:
    print("Incorrect Input - Ending the Game")
    play_again = False
  return play_again

def clear():
   # for windows
   if name == 'nt':
    _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')


def play_blackjack():
  play_again = True
  while play_again:
    clear()
    print(logo)
    play_again = False
    user_hand = []
    deal_cards(user_hand)
    deal_cards(user_hand)
    print(f"USER'S HAND IS {user_hand}")
    
    dealers_hand = []
    deal_cards(dealers_hand)
    deal_cards(dealers_hand)
    print(f"COMPUTER'S HAND IS ['{dealers_hand[0]}', 'X']")  
    
    if is_blackjack(user_hand, dealers_hand):
      play_again = play_again_choice(play_again)
      if not(play_again):
        break
      
    users_score,dealers_score = calculate_score(user_hand, dealers_hand)
    if users_score > 21:
      print(f"BUST: USER LOST AS SCORE IS {users_score}")
      play_again = play_again_choice(play_again)
      if not(play_again):
        break
    elif dealers_score > 21:
      print(f"BUST: COMPUTER LOST AS SCORE IS {dealers_score}")
      play_again = play_again_choice(play_again)
      if not(play_again):
        break
    hit = True
    while hit:
      draw_another_card = input("Do you want to draw another card (Y / N) : ")   
      if draw_another_card.upper() == "Y":
        hit = True
      elif draw_another_card.upper() == "N":
        hit = False
        break
      else:
        print("Assuming a No to Hit as wrong input was given")
        hit = False
        break
      
      users_score,dealers_score = calculate_score(user_hand, dealers_hand)
      if(users_score > 21):
        hit = False
        break
      else:
        deal_cards(user_hand)
        print(f"USER'S HAND IS {user_hand}")
        print(f"COMPUTER'S HAND IS ['{dealers_hand[0]}', 'X']")

    while dealers_score < 17:
      deal_cards(dealers_hand)
    
    users_score,dealers_score = calculate_score(user_hand, dealers_hand)
    if dealers_score > 21:
      print(f"USER'S HAND IS {user_hand} AND SCORE IS {users_score}")
      print(f"COMPUTER'S HAND IS {dealers_hand} AND SCORE IS {dealers_score}")
      print("USER WINS AS COMPUTER'S HAND EXCEEDS 21")
    else:
      print(f"USER'S HAND IS {user_hand} AND SCORE IS {users_score}")
      print(f"COMPUTER'S HAND IS {dealers_hand} AND SCORE IS {dealers_score}")
    
    if users_score > dealers_score:
      print(f"USER WINS AS SCORE IS {users_score}")
    elif users_score < dealers_score:
      print(f"COMPUTER WINS AS SCORE IS {dealers_score}")
    else:
      print("DRAW AS BOTH SCORES ARE EQUAL")

    play_again = play_again_choice(play_again)
    if not(play_again):
      break
    
play_blackjack()
