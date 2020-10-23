import random


def game():
    rematch = True
    
    while rematch:
        game_list = ["rock", "paper", "scissors"]
        randomizer = random.choice(game_list)
        print("This is a rock, paper, scissors game")
        player = input("Choose one: ")
        
        print(randomizer)

    
    
        if player == "rock" and randomizer == "scissors":
            print(f"The computer chose {randomizer}. You win!")
            #continue
        
        elif player == "paper" and randomizer == "rock":
            print(f"The computer chose {randomizer}. You win!")
        
        elif player == "scissors" and randomizer == "paper":
            print(f"The computer chose {randomizer}. You win!")

        elif player == "rock" and randomizer == "paper":
            print(f"The computer chose {randomizer}. You lose!")

        elif player == "paper" and randomizer == "scissors":
            print(f"The computer chose {randomizer}. You lose!")
        
        elif player == "scissors" and randomizer == "rock":
            print(f"The computer chose {randomizer}. You lose!")

        elif player == "rock" and randomizer == "rock":
            print(f"The computer chose {randomizer}. try again")

        elif player == "paper" and randomizer == "paper":
            print(f"The computer chose {randomizer}. try again")

        elif player == "scissors" and randomizer == "scissors":
            print(f"The computer chose {randomizer}. try again")


        rematch = input("Try again? (y/n) ")
        if rematch == "y":
            True
        else:
            False
            break
        


if __name__ == "__main__":
    game()