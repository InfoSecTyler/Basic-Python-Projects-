''''
Py-Sector Escape! V: 1.0
Coded by: Tyler Linne
Created On: 4/14/16
'''

import random
import os
import sys 

# set up the framework of the map
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

# Generate dialog to be displayed during the game
CREW = ['Gunner: Where are We?', "Navigatior: I Don't Remember This Place", 'Cook: Food Stores are Getting Low', 'LT: No Response From Our Mayday Calls']

#keep track of all the visited sectors
visited = []

# random number generator for the end screen
END = range(64)

#clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
#Set starting locations for the character, monster and door
def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)
    #ensure that player and monster/door will not start in the same sector 
    if monster == door or monster == start or door == start:
        return get_locations()
    
    return monster, door, start
  
#take imput from the user to move the player
def move_player(player, move):
    x, y = player
    
    if move == 'LEFT':
        y -=1
    elif move == 'RIGHT':
        y +=1
    elif move == 'UP':
        x -=1
    elif move == 'DOWN':
        x += 1
    
    return x, y

#remove choices that would cause the player to move off the map
def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
        
    return moves

#draw a visual representation of the game space 
def draw_map(player):
    print(' _ _ _ ')
    tile = '|{}'
    path = '|{}'
    #working on creating entires into the map to show where the player has been 
    
    for idx, cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player :
                print(tile.format('X'),end='') 
                visited.append(player) 
            else:
                print(tile.format('_'), end='') 
        else:
            if cell == player:
                print(tile.format('X|')) 
                visited.append(player)
            else:
                print(tile.format('_|')) 

#start of the game
clear()
monster, door, player = get_locations()
print('______________________________________________________________________________________')
print("""Your Ship is in Danger and You are lost. You Need to Escape Back to Your Home Sector. 
Good Luck""")
print('______________________________________________________________________________________')
print('')


while True:
    moves = get_moves(player)
    print("You're currently in Sector {}".format(player)) 
    print('')
    print('Internal Comms:')
    print('____________________________________')
    print('{}'.format(random.choice(CREW)))
    print('------------------------------------')
    
    print('Map:')
    draw_map(player)
    print('You have Visited These Sectors: {}'.format(visited)) 
    print('')
    print("You can move {}".format(moves))
    print('')
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()
    clear()
    if move == 'QUIT':
        break
    
    
    if move in moves:
        player = move_player(player, move)
    else:
        print('You can not escape this way, try again')
        continue
    #player wins!   
    if player == door:
        print('You Found Home!')
        print('You Avoided {} Dangers'.format(random.choice(END)))
        break
    #player looses
    if player == monster:
        print('Did we mention you were being chased? Well, you were caught...')
        print('You got shot {} times'.format(random.choice(END)))
        break
