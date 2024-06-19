from art import logo, vs
from game_data import data
from random import choice
from replit import clear

score = 0


def ques1():
  return choice(data)


def ques2():
  return choice(data)

first = ques1()
second = ques2()


 # Function for comparing the followers
def answer(first, second):
  ''' It compares the follower count of the two questions and returns the one with the highest follower count. '''

  if first['follower_count'] > second['follower_count']:
    return 'a'
  else:
    return 'b'


# Function for checking the answer
def compare(user_choice):
  global first, second, score
  result = answer(first, second)

  if user_choice == result:
    score += 1
    clear()
    first = second
    second = choice(data)
    return True
  else:
    
    print(f"Sorry, that's wrong. Final score: {score}")
    return False

    
      
def game():
  global first, second, score

  while True:
    print(logo)
    print(
        f"Compare A: {first['name']}, {first['description']}, {first['country']}."
    )
    print(vs)
    print(
        f"Against B: {second['name']}, {second['description']}, {second['country']}."
    )
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if not compare(user_choice):
      again = input("Do you want to play again? Type 'y' or 'n': ").lower()
      if again == 'y':
          score = 0
          first = ques1()
          second = ques2()
          clear()
      else:
          return False
      
      
game()
