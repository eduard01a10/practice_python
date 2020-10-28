import math
import random

def run(my_list, target_value):

    minum = 0
    maxinum = len(my_list) - 1
    guess = None

    while maxinum >= minum:  #Here while the maxinum index is higher or equal to minum the loop will continue
        
        guess = math.floor((minum + maxinum) / 2)
        print(f"The computer guessed {guess}")
        if my_list[guess] == target_value:
            print(f"The computer found your number and it is {my_list[guess]}")
            return guess
        
        elif my_list[guess] < target_value:
            minum = guess + 1
            
            
            
        elif my_list[guess] > target_value:
            maxinum = guess - 1
            
    return -1        
            


primes = [*range(0, 1001, 1)]
objective = int(input("Welcome, pick a number between 1 and 1000 and the computer will found it: "))

if __name__ == "__main__":
    run(primes, objective)
