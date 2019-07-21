from player import *

import random


#GAME CODES:
# 0 -> no ship, unguessed
# 1 -> ship, unguessed
# 2 -> ship, guessed
# 3 -> no ship, guessed

OFFICIAL_MAX_TURNS = 1000
OFFICIAL_X_DIM = 8
OFFICIAL_Y_DIM = 8

game_board = [0]*OFFICIAL_X_DIM
for x in range(OFFICIAL_X_DIM):
    game_board[x] = [0]*OFFICIAL_Y_DIM

def print_board():
    print("=== GAME BOARD ===")
    for i in range(OFFICIAL_X_DIM):
        for j in range(OFFICIAL_Y_DIM):
            print(game_board[i][j], end =" ")
        print("")

def initialize_board():
    #reset to zeros
    game_board = [0]*OFFICIAL_X_DIM
    for x in range(OFFICIAL_X_DIM):
        game_board[x] = [0]*OFFICIAL_Y_DIM

    #add ships
    ship_dims = [5,4,3,3,2]
    for dim in ship_dims:
        while(not add_ship(dim)):
            pass


def add_ship(length):
    dir = (1,0)
    origin = (random.randint(0,8-length),random.randint(0,7))

    #direction tuple
    if(random.randint(0,1) == 1):
        dir = (0,1)
        origin = (random.randint(0,7),random.randint(0,8-length))

    for l in range(length):
        x = origin[0] + l*dir[0]
        y = origin[1] + l*dir[1]
        if(check_guess(x,y)):
            return False

    for l in range(length):
        x = origin[0] + l*dir[0]
        y = origin[1] + l*dir[1]
        game_board[x][y] = 1

    return True




def check_guess(x,y):
    if(x>=OFFICIAL_X_DIM or x<0 or y>=OFFICIAL_Y_DIM or y<0):
        return False
    if(game_board[x][y] == 1):
        return True
    else:
        return False

def make_guess(x,y):
    if(x>=OFFICIAL_X_DIM or x<0 or y>=OFFICIAL_Y_DIM or y<0):
        return False
    if(game_board[x][y] == 1):
        game_board[x][y] = 2
        return True
    else:
        game_board[x][y] = 3
        return False

def check_game_over():
    for i in range(OFFICIAL_X_DIM):
        for j in range(OFFICIAL_Y_DIM):
            if(game_board[i][j] == 1):
                return False
    return True

def main():
    #initialize a random board
    initialize_board()
    print_board()

    #counter that ticks onces each time a turn happens
    turn_counter = 0
    game_over = False

    #game loop
    while(not game_over and turn_counter<OFFICIAL_MAX_TURNS):

        #increment the counter
        turn_counter+=1

        #get a guess from the player
        x,y = take_turn()

        #check the game board to see if ship is there
        hit = make_guess(x,y)
        # print("Guess was:",x,y,". Hit?",hit)

        #add to list of guesses
        previous_guesses.append((x,y,hit))

        game_over = check_game_over()
        # print_board()

    if(turn_counter==OFFICIAL_MAX_TURNS):
        print("Game stopped after",OFFICIAL_MAX_TURNS,"turns. Perhaps make sure you don't repeat guesses.")
    else:
        print("Won the game in",turn_counter,"turns!")




if __name__ == "__main__":
    main()
