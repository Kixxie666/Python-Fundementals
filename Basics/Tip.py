
Cost = float(input("How much was your bill?"))

Tip10 = float((Cost / 100) * 10)
answer = input("would you like to customise your tip?" + " " + "If not it will default to 10%....")
ftip = round(Tip10)
if answer == "no":
        print("Your tip will be £" + str(ftip) )
else:
       Amount = input("How much would you like to tip (percent)?...")
