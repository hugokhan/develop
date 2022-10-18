# Tweet problem 

# Function to return if post is less than or equal to 20 characters
def GoodPost(Tweet):
   if len(Tweet) <= 20:
      return True
   else:
      return False

# Main program
print(GoodPost("This is a sample post for social networking."))






