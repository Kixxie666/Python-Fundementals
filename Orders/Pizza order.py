bill = 0
print("thanks for making pizza order food delivery choice yours now what like you")
size = input("what size pizza would you like? type: Small, Medium or Large.")
if size == "small":
    bill =+ 15
    pep1 = input("Would you like Pepperoni on your small pizza?")
    if pep1 == "yes":
        bill += 2
    chez = input("would you like extra Cheeeez type: Yes or No")
    if chez == "yes":
        bill += 1
        print (bill)
if size == "edium":
    bill =+ 20
    pep2 = input("Would you like Pepperoni on your Medium pizza?")
    if pep2 == "yes":
        bill += 3
    chez = input("would you like extra Cheeeez type: Yes or No")
    if chez == "yes":
        bill += 1
        print (bill)
elif size == "large":
    bill =+ 25
    pep3 = input("Would you like Pepperoni on your large pizza?")
    if pep3 == "yes":
        bill += 3
    chez = input("would you like extra Cheeeez type: Yes or No")
    if chez == "yes":
        bill += 1
        print (bill)
