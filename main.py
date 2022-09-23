# currency problem

#subroutine for currency exchange
def Exchange(currency, rate):
  if currency == "Yuan":
    return (100*Yuan_rate)
  elif currency == "Yen":
    return (100*Yen_rate)
  elif currency == "Euro":
    return (100*Euro_rate)
  elif currency == "USD":
    USD_value = 100*USD_rate
    return ("$" + str(USD_value))

# main programme
Yuan_rate = 7.86
Yen_rate = 157.76
Euro_rate = 1.12
USD_rate = 1.10

print("£100 =",Exchange("USD", USD_rate))
  
  

  
