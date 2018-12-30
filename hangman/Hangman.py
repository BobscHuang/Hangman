import string
import random

print("Welcome to Bob's amazing hangman program!")

Item = list("_")

Furits_Veggies = [
                "apple", "avocado", "banana", "blackberry", "watermelon",
                "broccoli", "beans", "peach", "squash", "carrot", "cherry",
                "garlic", "grape", "lettuce", "kiwi", "leek", "lemon", "mango",
                "mushroom", "nut", "olive", "peanut", "pear", "pepper",
                "pineapple", "pumpkin", "radish", "rasisin", "strawberry",
                "potato", "tomato", "turnip", "zucchini"
                ]

Animals = [
            "goose", "dog", "cat", "hippo", "wolf", "turkey", "beaver",
            "bear", "duck", "chipmuck", "bobcat", "donkey", "horse", "goat",
            "elephant", "leopard", "armadillo", "buffalo", "baboon", "chimpanzee",
            "shark", "chicken", "dolphin", "deer", "falcon", "eagle", "sloth",
            "hamster", "whale", "human"
            ]

Countries = [
            "canada", "china", "usa", "germany", "cuba", "japan",
            "sweden", "turkey", "chad", "england", "ecuador", "iceland",
            "kenya", "luxembourg", "morocco", "india", "mexico", "brazil",
            "pakistan", "peru", "portugal", "argentina", "russia", "spain",
            "poland"
            ]

Word_Bank = [Furits_Veggies, Animals, Countries]
#print(Word_Bank)


print(" ")
print("Would you like to review the rules of hangman before starting?")
print("1. Of course")
print("2. NAHHH, I'm good")
Rules_View = input("What is your choice?: ")
print(" ")

if Rules_View == "1":
    print("*" * 80)
    print(" ")
    print("This game is a very standard text based version of hangman")
    print("The rules are simple, you must guess the word of the opponent")
    print("For mutiplayer, player 1 will enter a word for player 2 to guess")
    print("For single player, the computer will randomly pick a word from its prexisting wordbanks")
    print("Also, the computer will give a hint to what catergory the word is from, for example 'animals'")
    print("In both game modes, the number of wrong guesses allowed is 8")
    print("The game will display a tracking sheet with the length of the word and what has been guessed correctly")
    print("To make the players life easier, it will also display which words have yet to be guessed")
    print("The main goal is to simply guess the unknown word correctly without guessing wrong 8 times")
    print("By guessing the word right player 2 wins, else player 1 or computer wins")
    print("HAPPY GUESSING!")
    print(" ")
    print("*" * 80)
    print(" ")

while True:

    Letters = list(string.ascii_lowercase)

    print("A: Mutiplayer")
    print("B: Single Player")

    Mode = input("What mode would you like to play? ")
    Mode = Mode.upper()

    while Mode != "A" and Mode != "B":

        print(" ")
        print("That is not a valid choice!")
        print("A: Single Player")
        print("B: Mutiplayer")
        Mode = input("What mode would you like to play? ")
        Mode = Mode.upper()

    if Mode == "A":

        while True:

            Word = input("Player 1 please enter desired word for player 2 to guess: ")

            #check if word is all in letters
            
            if Word.isalpha() == False:
                print("That's not a word!")
            
            Word = list(Word)

            Word_2 = Word

            #check length of word
            
            if len(Word) < 3:
                print("Your word should be atleast 3 letters long!")

            else:
                break

    elif Mode == "B":

        Word_Bank1 = random.choice(Word_Bank)

        if Word_Bank1 == Furits_Veggies:
            Caterory = "This word it from the caterory of fruits and vegetables!"

        elif Word_Bank1 == Animals:
            Caterory = "This word it from the caterory of animals!"

        else:
            Caterory = "This word it from the caterory of countries!"

        Word = random.choice(Word_Bank1)

        Word = list(Word)

        Word_2 = Word

        

    print(" ")    
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("                      ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔╦╗╔═╗╦═╗╔╦╗")
    print("                      ║ ╦╠═╣║║║║╣   ╚═╗ ║ ╠═╣╠╦╝ ║ ")
    print("                      ╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╩ ╩ ╩╩╚═ ╩ ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

    #makes word into lowercase
        
    Word = [x.lower() for x in Word]

    Tries = 0

    Characters = len(Word)

    Word_Blank = Word

    #replaces word with blanks
        
    Word_Blank = ["_" if x >= "a" else x for x in Word_Blank]

    if Mode == "B":
        print(Caterory)

    while True:
        
        print("This is your tracking sheet")              
        print(Word_Blank)
        print(" ")
        print("The word is", Characters, "letters total in legth")

        #letters left

        Letters_Left = len(Word) - Word.count(" ")

        if Letters_Left > 1:
        
            print("There are still", Letters_Left, "letters left to guess for this word")

        else:
            
            print("There is still", Letters_Left, "letter left to guess for this word")

        print("Player two please guess the letters")


        while True:
            
        
            Guess_1 = input("What is your guess? ")
            Guess_1 = Guess_1.lower()

            if Guess_1 in Letters:
                break

            else:
                print("\nThat is not a valid choice or you have already guessed it\n")

        print(" ")
        print("-" * 80)
        print(" ")
            
                
        Letters = [s.replace(Guess_1, '') for s in Letters]
        Letters = list(filter(None,Letters))
        
        if Guess_1 in Word: #in the word?
            print("Good job! '" + Guess_1 + "' is in this word")

            Number_Letter = Word.count(Guess_1)

            if Number_Letter > 1:

                print("There are exactly " + str(Number_Letter) + " " + (Guess_1) + "'s in this word")

            elif Number_Letter == 1:

                print("There is exactly", Number_Letter, Guess_1, "in this word")

            #adds letter to blank list

            while True:

                Number_Letter = Number_Letter - 1
                
                Location = Word.index(Guess_1)

                Word_Blank[Location] = Guess_1

                #removes guessed letter

                Word[Location] = " "

                if Number_Letter == 0:
                    break

        else:

            #calculates turns left
            
            Tries = Tries + 1 
            print("Unforturenetly '" + Guess_1 + "' is not in this word")
        print("The letters you have yet to chose are:")
        print(Letters)

        if Tries < 7 or Tries == 8:

            print("You have", 8 - Tries, "chances left before you lose") 

        else:

            print("You have only", 8 - Tries, "chance left before you lose")

                #AMAZING STICK FIGERS!!!!

        if Tries == 0:

            print(" ")
            print("        ------------        ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 1:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 2:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |                   ")
            print("        |                   ")
            print("        |                   ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 3:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |         /         ")
            print("        |        /          ")
            print("        |       /           ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 4:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |          |        ")
            print("        |         /  \      ")
            print("        |        /    \     ")
            print("        |       /      \    ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 5:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |        / |        ")
            print("        |       /  |        ")
            print("        |      /   |        ")
            print("        |         /  \      ")
            print("        |        /    \     ")
            print("        |       /      \    ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 6:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     --      --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |        / | \      ")
            print("        |       /  |  \     ")
            print("        |      /   |   \    ")
            print("        |         /  \      ")
            print("        |        /    \     ")
            print("        |       /      \    ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 7:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     -- x    --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |        / | \      ")
            print("        |       /  |  \     ")
            print("        |      /   |   \    ")
            print("        |         /  \      ")
            print("        |        /    \     ")
            print("        |       /      \    ")
            print("    ---------               ")
            print(" ")
            
        elif Tries == 8:

            print(" ")
            print("        ------------        ")
            print("        |        ----       ")
            print("        |      --    --     ")
            print("        |     -- x  x --    ")
            print("        |      --    --     ")
            print("        |        ----       ")
            print("        |          |        ")
            print("        |        / | \      ")
            print("        |       /  |  \     ")
            print("        |      /   |   \    ")
            print("        |         /  \      ")
            print("        |        /    \     ")
            print("        |       /      \    ")
            print("    ---------               ")
            print(" ")
             
        #END
        
        if "_" not in Word_Blank:

            print("You have succssfully guessed the word: ")
            print(Word_2)
            
            print(" ")
            print("                      ╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╔╗╔")
            print("                      ╚╦╝║ ║║ ║  ║║║║ ║║║║")
            print("                       ╩ ╚═╝╚═╝  ╚╩╝╚═╝╝╚╝")
            print(" ")
            
            print("Congratz! You won!")
        
            break

        if Tries == 8:

            print("The word was:")
            print(Word_2)
                
            print(" ")
            print("                  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗")
            print("                  ║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝")
            print("                  ╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═")
            print(" ")
            
            print("You have ran out of luck and lost!")
        
            break
        
    print("If you want to end the game type stop ")
    print("If you want to continue simply press enter! ")

    inp = input()
    inp = inp.upper()
    
    if inp == "STOP":
        break





    

