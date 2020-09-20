#global __import__
import random
import time

#Functions of the main menu
# Shows spacing between the main menu if the player inputs something wrong
def cls():
    print("\n" * 50)

def image():
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("<       Main menu of the game        >")
    print("<       *********************        >")
    print("<    War between plastic and humans  >")
    print("<    ******************************  >")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print()

def Main_room():
  Main_room_options = ["1", "2", "3"]
  user_choice =""
  while user_choice not in Main_room_options:
    
    print(" ")
    print('''Hello player, this game is about war againest plastic and humans. You as the player, will decide on which side you would want to take, Plastic or humans. Choosing the plastic will send you to war while choosing the humans will let you know about the enviroment they are in.
    
  1) Plastic side
  2) Human side ( I personally choose this one ;] )
  3) Where's the nearest exit.''' )

    print(" ")
    user_choice = str(input("Enter the option number for your fate (!!suspense music!!): "))
  
  # User will have selected their level from the "user_choice"
  if user_choice == Main_room_options[0]:
    Minigame()
  elif user_choice == Main_room_options[1]:
    Storygame()
  elif user_choice == Main_room_options[2]:
    leave_main_menu()

# If the player chooses this, he will be playing the minigame based from the rps file but adjusted and innvotivated
def Minigame():
    print("\n \n You chose to side with the plastic.")
    print("\n Very sad :( ")

    # This will be a note for anyone viewing the game is that the structre of the program was sourced from my teams in DTP2A in teams, within files that say programming pratice, under a file called rock paper and sciccors. I will simply develop on it and make it suitable for my project with plastic pollution towards my audiences which are teenagers.
    # It will also be added into the main menu

    # Functions go here


    # Round checking function
    def check_rounds():
        while True:
            response = input("How many bases do you want to conquer:")

            round_error = "Incorrect. Either press <enter> or type a interger higher than 0. Thanks."
            print()
            if response != "":
                try:
                    response = int(response)

                    if response < 1:
                        print(round_error)
                        continue

                except ValueError:
                    print(round_error)
                    continue

            return response


    # User choice checking function
    def check_choice(question, options):
        valid = False
        while not valid:
            response = input(question)
            response = response.lower()     # make responses all lower case for the player

            if response == "stop now":
                return response
            elif response == "f":
                response = "fight"
            elif response == "r":
                response = "retreat"
            elif response == "d":
                response = "defend"

            if response in options:
                return response
            else:
                print("Dont understand whatever you typed solider. AGAIN.")
                print()


    # Feedback generator
    def feedback(statement, char):
        print()
        print(char*len(statement))
        print(statement)
        print(char*len(statement))
        print


    # main routine goes here...

    # initialise variables
    rps_list = ["fight", "retreat", "defend"]

    # Instructions go here...
    # Introduction of the minigame
    intro_heading ="///         War againest the humans - Instructions          ///"
    feedback(intro_heading, "/")
    print("For each game you play, either choose the number of battles or press <enter> for \n"
          "continuous battles. I would want to also clarify that you can end the game early by typing 'stop now'.\n"
          "\n"
          "When prompted choose fight / retreat / defend\n"
          "Towards the ending of each game, you will be able to see your game summary. After that point, you can \n"
          "can either play again (press <enter> when prompted) or quit by pressing\n"
          "any key.")
    print("/" * len(intro_heading))



    keep_going = ""

    while keep_going == "":
        # Play game

        result = ""

        # Rounds won will be calculated (total - draw - lost)
        rounds_played = 0
        rounds_lost = 0
        rounds_drawn = 0

        end_game = "no"

        # Play Game
        print()
        rounds = check_rounds()

        while end_game == "no":
            # Generating computer choices here
            comp_choice = random.choice(rps_list)


            # Getting users choice

            if rounds == "":
                heading = "Continuous Battles intiated: Battle {}".format(rounds_played + 1)
                print(heading)

            else:
                heading = "Battle {} of {}".format(rounds_played + 1, rounds)
                print(heading)

                if rounds_played == rounds - 1:
                    end_game = "yes"

            user_choice = check_choice("Please choose fight (f), retreat (r) or defend (d): ", rps_list)

            if user_choice == "stop now":
                break

            rounds_played += 1  # This must be AFTER the break otherwise the rounds won calculation will be incorrect.


            # Compare choices
            if comp_choice == user_choice:
                result = "It's a stalemate"
                rounds_drawn += 1
                character = "-"
            elif user_choice == "fight" and comp_choice == "retreat":
                result = "The enemy has fled. We have conquered their base"
                character =":"
            elif user_choice == "retreat" and comp_choice == "defend":
                result = "We managed to escape from the enemy unscaved, We will fight again in another time."
                character =":"
            elif user_choice == "retreat" and comp_choice == "fight":
                result = "We managed to escape from the enemy with large causulaties. Our fallen brothers will not die in vain."
                character = ":"
            elif user_choice == "Defend" and comp_choice == "retreat":
                result = "They are retreating, the base is ours to conquer."
                character =":"
            else:
                result = "The enemys has bested us. We must not lose AGAIN!!!"
                rounds_lost += 1
                character = "#"


            result_statement = "Plastic: {}    |    Humans: {}    |    Result: {}".format(user_choice, comp_choice, result)
            print()
            # Output result
            feedback(result_statement, character)
            print()

        # End of Game Statements
        summary_statement = "Wins: {}    /\    Losts: {}    /\   Draw: {}".format(rounds_played-rounds_drawn-rounds_lost,
                                                                              rounds_lost, rounds_drawn)
        print()
        print("***************    Summary   ************")
        print(summary_statement)
        print("*" * len(summary_statement))
        print()

        keep_going = input("Press <enter> to play again or any key to quit...")
        print()

    feedback("----    Congrats on playing my game   ----", "-")

        

def Storygame():
    print("You have chosen to side with the humans.")
    print("Nice one soldier :] ")
    print()

    # importing random for the choices inputed by the player
  

    # Intro of the game


    def title():
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        time.sleep(1)
        print("<            Humans side             >")
        time.sleep(1)
        print("<           *************            >")
        time.sleep(1)
        print("<      Short story about the war     >")
        time.sleep(1)
        print("<      *************************     >")
        time.sleep(1)
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        time.sleep(1)
        print()

    def Intro():
        print("Hold up player. My mistake but I want to mention that for this side of the story, you are only getting to choose once. The rest will just follow like a story. Ok bye :} ")
        time.sleep(8)
        print("Welcome to the war cadit.")
        time.sleep(2)
        print()
        print("\n Where plastic has consumed us to live in barrows while the skies fills with corruption.")
        time.sleep(4.5)
        print("\n The other cadits has left their posts to scavenge amongest the wasteland for resources.")
        time.sleep(4.5)
        print("\n Your task will be to investigate and record any findings about the enviroment outside to see how much damage has been cause ")
        time.sleep(5)
        print("\n Now cadit, go adventure outside and report back once your done with the research.")
        time.sleep(5)
        print(" \n Which path do I want to take for my journey. ")
        print()


    def Path1():
        path = ""
        while path != "1" and path != "2":  #Inputing validations
            path = input("Choose one of the paths to take  (1 or 2): ")

        return path
    #The path decided by the player will follow with the story
    def Checkpath(Path1):
        print()
        print("You walk down this path through the radioactive forest with your suit")
        time.sleep(5)
        print("You gaze upon the destruction plastic has wrecked across this world")
        time.sleep(5)
        print("Pieces of plastic shrouds the trees, trapping their life while seeing the unfortunate creatures mutated or engulfing pieces of trash for survival.")
        time.sleep(5)
        print()

        # Randomize the choice made by the player
        correctPath = random.randint(1, 2,)

        if Path1 == str(correctPath):
            print()
            print("At the end of your journey, You realise that the world has to be changed in a greener atomsphere for the creatures and humans who inhabits on earth.")
            time.sleep(5)
            print("You approach to a high cliff, gazing upon the rainbow coloured rivers to the trails of trash descending from the skies.")
            time.sleep(5.5)
        else:
            print()
            print("While reaching back to headquarters with your finding, You found a busted robot on your trail.")
            time.sleep(4)
            print("Damaged by the corrosive from the acid rains, geting up close, the robot suddenly spoke, saying one sentence over and over again. ")
            time.sleep(4)
            print("Humans have brought their own down fall as their creation rises.")
            time.sleep(4)





    playAgain = "yes"
    # This will intiate the functions and decide for the player if they want to play again or not
    while playAgain == "yes" or playAgain == "y":
        title()
        Intro()
        choice = Path1()
        Checkpath(choice)    #Choice will always be equal to "1" or "2"
        print()
        playAgain = input("Do you want to play again by typing yes or y or typing any keys to exit the game: ")
        print()

def leave_main_menu():
    print ("\n \n Well you are no fun")

# Main program to start
image()
Main_room()
