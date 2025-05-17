class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#     \n
# COLOURE.BLUE    + colour.END 
#  colour.UNDERLINE +
game = input ( colour.UNDERLINE +"To play this game type either A or B to pick a choice and press enter. do you accept? " + colour.END + colour.BOLD + "   "  + " A: YES      B: NO " + colour.END )


if game == "B":
    print ("ok bye")
else:
    print (colour.BLUE + "After waking up in a strange forest with no memory of your past you stand up and take a look around. \n You notice there is a tree, larger than the others around you making ominous creaking sounds. \n as you continue to assess your surroundings you see a worn down dirt path leading deeper into the trees. "  + colour.END)
answer1 = input(colour.BOLD + "Do you\n A: " + colour.UNDERLINE + "Walk towards the tree and get a closer look..." + colour.END  + " \n  "  "B: " + colour.UNDERLINE + "Follow the dirt path and try to find someone who knows more about where you are." + colour.END)


if answer1 == "a":
    print (colour.BLUE + "The tree seems to react to your presence and starts creaking more and more the closer you get.\nThe sound of the trees branches shaking and its bark moving fills your ears. Now its the only thing you can hear in the dead silent forest. \n as you walk around the tree taking in its beauty and mystery you hear a faint whisper. \n " + colour.DARKCYAN + "It seems to be coming from inside the tree.. " + colour.END + colour.END)
    answer2 = input(colour.BOLD + "Do you\n A: " + colour.UNDERLINE + "Touch the tree and see if the bark is loose.." + colour.END  + " \n  "  "B: " + colour.UNDERLINE + "go back and follow the dirt path and try to find someone who knows more about where you are." + colour.END)
else:
    answer3 = input 


if answer1 == "a":
    print (colour.BLUE + "The tree seems to react to your presence and starts creaking more and more the closer you get.\nThe sound of the trees branches shaking and its bark moving fills your ears. Now its the only thing you can hear in the dead silent forest. \n as you walk around the tree taking in its beauty and mystery you hear a faint whisper. \n " + colour.DARKCYAN + "It seems to be coming from inside the tree.. " + colour.END + colour.END)
    answer2 = input(colour.BOLD + "Do you\n A: " + colour.UNDERLINE + "Touch the tree and see if the bark is loose.." + colour.END  + " \n  "  "B: " + colour.UNDERLINE + "go back and follow the dirt path and try to find someone who knows more about where you are." + colour.END)
#if answer2 == "a":
    
#else:

#if answer3 == "a":

#else:  