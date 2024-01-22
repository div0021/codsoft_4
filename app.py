import random
from enum import Enum
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear') 

def rock_paper_scissor(name="PlayerOne"):
    game_count=0
    player_win_count=0
    computer_win_count=0

    def play_rock_paper_scissor():
        nonlocal name;
        nonlocal game_count
        nonlocal player_win_count
        nonlocal computer_win_count

        # defining enums
        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3

        playerChoice = input(f'\n{name.title()}, please enter... \n1 for 🪨 Rock\n2 for 📄Paper,or \n3 for ✂️ Scissor\n==> ')

        if playerChoice not in ["1","2","3"]:
            print(f"\nNot funny {name.title()}, please enter 1,2 or 3.")
            return play_rock_paper_scissor()
        
        player = int(playerChoice)
        computerChoice = random.choice("123")
        computer=int(computerChoice)

        # printing the chosed option
        print(f"\n{name.title()}, you chose {str(RPS(player)).split(".")[1].title()}.")

        print(f"\nComputer chose {str(RPS(computer)).split(".")[1].title()}.")

        # This function will decide who will win the game.
        def decide_winner(player,computer):
            nonlocal player_win_count
            nonlocal computer_win_count
            nonlocal name

            if player == 1 and computer == 3:
                player_win_count+=1
                return f"🙌🙌 {name.title()}, you win!!";
            elif player == 2 and computer == 1:
                player_win_count+=1
                return f"🙌🙌 {name.title()}, you win!!";
            elif player == 3 and computer == 2:
                player_win_count+=1
                return f"🙌🙌 {name.title()}, you win!!";
            elif player ==  computer:
                return f"😯😲😮 Tie game!";
            else:
                computer_win_count+=1
                return f"💻🖥️ Computer win!!\nSorry, {name.title()}... 😔😞😓"

        game_result = decide_winner(player,computer)
        print("\n"+game_result+"\n")

        nonlocal game_count
        game_count+=1

        # show the status of the game
        print("#####################\n")
        print(f"\n## Game count:{game_count} ##")
        print(f"\n## {name.title()} wins:{player_win_count} ##")
        print(f"\n## Computer wins:{computer_win_count} ##")
        print("\n####################\n")

        # ask for play again
        print(f"\nPlay again, {name.title()}?")

        while True:
            playagain = input("\nY for 🥳 Yes or \nQ to 🙅 Quit.\n")

            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            clear_console()
            return play_rock_paper_scissor()
        else:
            print(f"\n🎉🎉🎉🎉🎊🎈🎈 Thank you for playing, 👋👋 Byee {name.title()}.. \n")
            
        
    return play_rock_paper_scissor


if __name__ == "__main__":
    # Taking user input

    print("******************************************************\n")
    print("*** Welcome to 🪨 Rock, 📄Paper and ✂️ Scissor Game ***\n")
    print("******************************************************\n")
    name = input("Enter your name:\n").strip().title()

    rps=rock_paper_scissor(name)
    rps();

