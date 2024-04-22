import random as rd

def snakewatergun(you, comp):
    # return 1 if you win, -1 if you lose, and 0 if draw
    # draw case
    if you == comp:
        return 0
    
    # snake gun or gun snake
    if (you == 's' and comp == 'g'):
        return -1 
    elif (you == 'g' and comp == 's'):
        return 1
    # snake water or water snake
    if (you == 's' and comp == 'w'):
        return 1
    elif  (you == 'w' and comp == 's'):
        return -1
    # gun water or water gun
    if (you == 'g' and comp == 'w'):
        return -1 
    elif ( you == 'w' and comp == 'g'):
        return 1

def main():
    number = rd.randrange(0,12)
    print(number)
    if (number < 4):
        comp = 's'
    if (number > 4 and number < 8 ):
        comp = 'w'
    if (number > 8 and number < 12):
        comp = 'g'
    
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
