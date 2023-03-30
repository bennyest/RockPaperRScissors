import random
import re
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    mychoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", mychoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    print ("You chose: " + mychoice)
    choices = ['R', 'P', 'S']
    pyChoice = random.choice(choices)
    print ("I chose: " + pyChoice)
    if pyChoice == str.upper(mychoice):
        print ("Tie! ")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif pyChoice == 'R' and mychoice.upper() == 'S':
        print ("Scissors beats rock, I win! ")
        continue
    elif pyChoice == 'S' and mychoice.upper() == 'P':
        print ("Scissors beats paper! I win! ")
        continue
    elif pyChoice == 'P' and mychoice.upper() == 'R':
        print ("Paper beat rock, I win! ")
        continue
    else:
        print ("You win!")