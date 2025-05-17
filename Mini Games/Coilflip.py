import random
coin_flip = input("Do you want to flip a coin?")
if coin_flip == ("yes"):
    coin = random.randint(1,2)
    if coin == (1):
        print("heads wins!")
    elif coin == (2):
        print("Tails wins")

