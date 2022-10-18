# initials problem 

# Subroutine for name configuration
def GetFirstName(firstName):
  return firstName[0:1].upper()

def GetFullName(firstName, lastName):
  return GetFirstName(firstName) + " " + lastName.upper()

# main programme
firstName = "Ben"
lastName = "White"

print("Full name: {}".format(GetFullName(firstName, lastName)))













