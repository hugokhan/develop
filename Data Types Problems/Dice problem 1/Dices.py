# Polyhedral Dice Problem
import random 

#subroutine for faces on a dice
def N_sides():
  return random.randint(2,20)
def Value():
  return random.randint(1,N_sides())

# Main Programme
Value = Value()
print("You rolled a {}" .format(Value))


      



