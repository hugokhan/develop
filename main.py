# currency problem
import math

#subroutine for currency exchange
def Exchange(currency, rate):
    if currency == "Yuan":
        return (100 * rate)
    elif currency == "Yen":
        return (100 * rate)
    elif currency == "Euro":
        return (100 * rate)
    elif currency == "USD":
        return (100 * rate)

def GetSymbol(currency):
    if currency == "Yuan" or currency == "Yen":
        return "¥"
    elif currency == "Euro":
        return "€"
    elif currency == "USD":
        return "$"
    elif currency == "GBP":
        return "£"

def GetExchangeRate(currency, rate):
  return (
          GetSymbol("GBP") + "100 = " +
          GetSymbol(currency) +
          " with round method: " + str(round(Exchange(currency, rate), 2)) + 
          " with math.ceil method: " + str(math.ceil(Exchange(currency, rate)))
        )

# main programme
Yuan_rate = 7.86
Yen_rate = 157.76
Euro_rate = 1.12
USD_rate = 1.10

#print("£100 =", Exchange("USD", USD_rate))
#print("£100 =", Exchange("Euro", Euro_rate))
#print("£100 =", Exchange("Yuan", Yuan_rate))
#print("£100 =", Exchange("Yen", Yen_rate))
#print("----------------------------------")
#print("£100 = " + str(Exchange("USD", USD_rate)))
#print("£100 = " + str(Exchange("Euro", Euro_rate)))
#print("£100 = " + str(Exchange("Yuan", Yuan_rate)))
#print("£100 = " + str(Exchange("Yen", Yen_rate)))
#print("----------------------------------")
print(GetExchangeRate("USD", USD_rate))
print(GetExchangeRate("Euro", Euro_rate))
print(GetExchangeRate("Yuan", Yuan_rate))
print(GetExchangeRate("Yen", Yen_rate))

