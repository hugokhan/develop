# Hours in a Day problem
import random

#subroutine to define number of days and hours
def N_hours(): 
  return random.randint(1,1000)
def N_days(inp_hours):
  if inp_hours % 24 == 0:
    return (inp_hours / 24) 
  else :
    return int((inp_hours / 24))

#main programme
hours = N_hours()
days = N_days(hours)
print("{} hours is {} days".format(hours,days))



      



