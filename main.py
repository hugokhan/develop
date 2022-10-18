#electric car problem
import random
import math

#subroutine for functions
def minutes():
  return random.randint(1, 200)

def total_minutes_charged(inp_minutes):
  if inp_minutes >= 15:
    return round(((inp_minutes * 0.20) +1), 4)
  else :
    return round(((15 * 0.20) +1), 4)

def points(inp_minutes):
  if inp_minutes < 15:
    return 22
  else :
    return math.floor((inp_minutes * 1.5))

#main programme
minutes = minutes()
charge = total_minutes_charged(minutes)
points = points(minutes)

print("You have charged your car for {} minutes. Your total charge is £{:.2f}. You have received {} points for this charge.".format(minutes, charge, points))



