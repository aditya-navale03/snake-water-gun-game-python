import random

def snakewatergun(you, comp):
    # return 1 if you win, -1 if you lose, and 0 if draw
    # draw case
    if you == comp:
        return 0
    
    # snake gun or gun snake
    if (you == 's' and comp == 'g') or (you == 'g' and comp == 's'):
        return -1
    # snake water or water snake
    elif (you == 's' and comp == 'w') or (you == 'w' and comp == 's'):
        return 1
    # gun water or water gun
    elif (you == 'g' and comp == 'w') or (you == 'w' and comp == 'g'):
        return -1

def main():
    choices = ['s', 'w', 'g']
    comp = random.choice(choices)
    
    print("Enter 'S' for snake\nEnter 'W' for water\nEnter 'G' for gun")
    you = input()
    
    result = snakewatergun(you, comp)
    
    print(f"You choose {you} and computer choose {comp}.")
    
    if result == 0:
        print("Game draw")
    elif result == 1:
        print("You win")
    elif result == -1:
        print("You lose")

if __name__ == "__main__":
    main()
