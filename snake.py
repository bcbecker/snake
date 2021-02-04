# This is my attempt at making a functional snake game running in terminal, using curses to
# manipulate the terminal view rather than using another UI.
# ESC to quit, SPACE to pause, ARROWS to move




#----------------------------------------------------------------------------------------------------------------------------------
import curses
from random import randint


#Global variables:
player_score = 0                                     #player score
snake_body = [(9, 25), (10, 25), (11, 25)]           #start coordinates, immutable tuple (x, y)
snake_food = (4, 6)                                  #start coordinates (x, y)
ESC = 27                                             #end game key, ESC key is 27 character code
SPACE = 32                                           #pause game key, SPACE is 32 character code
key = curses.KEY_UP
possible_keys = [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT, ESC, SPACE]   #possible input keys

#Curses window setup:
curses.initscr()                            #initialize the screen with standard curses command
curses.noecho()                             #echoing keys off
curses.curs_set(False)                      #make cursor invisible
snake_win = curses.newwin(20, 50, 0, 0)     #defines window/size (y, x, starty, startx)
snake_win.keypad(True)                      #enable keypad mode
snake_win.nodelay(True)                     #not waiting for player input
snake_win.border(0)                         #border created at 0??? not 100%
snake_win.addch(snake_food[0], snake_food[1], '-')          #add first food


def game_over():
    #these are curses methods for ending terminal manip and restoring settings to original operation
    curses.nocbreak()
    snake_win.keypad(False)
    curses.echo()
    curses.endwin()

    #player's score printed so they know what they got
    print("\nGAME OVER\n")
    print("SCORE: " + str(player_score) + "\n")
    #or this:
    #print(f"SCORE: {player_score}")
    raise SystemExit


#Game logic:
while key != ESC:                                   #this will be the main loop where the program will reside in until game ends

    snake_win.addstr(0, 2 ,'SCORE: ' + str(player_score))                           #adds a scoreboard at the top
    snake_win.timeout(150 - (len(snake_body)) // 5 + len(snake_body) // 10 % 120)   #increase speed as size increases 

    previous_key = key                                          #up key is 'start' key defined in key
    player_move = snake_win.getch()                             #getch or get char recieves player key input
    key = player_move if player_move != -1 else previous_key    #continues moving in the selected direction
    if key not in possible_keys:
        key = previous_key

    #if space bar is pressed, pause for another
    if key == SPACE:
        key = -1
        while key != SPACE:
            key = snake_win.getch()
        key = previous_key

    #determine new coordinates for moves
    y = snake_body[0][0]
    x = snake_body[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1
        
    snake_body.insert(0, (y,x))              #add these coords to current snake position (could be optimized with append vs insert)
        
    #check if snake hits border coords
    if y == 0: game_over()
    if y == 19: game_over()
    if x == 0: game_over()
    if x == 49: game_over()

    #check if snake head runs over any other part of snake body
    if snake_body[0] in snake_body[1:]:
        game_over()

    #check if snake head runs over food/reset food
    if snake_body[0] == snake_food: 
        player_score += 10
        snake_food = ()
        while snake_food == ():
            snake_food = (randint(1, 18), randint(1, 48))          #rand coords for food reset
            if snake_food in snake_body:
                snake_food = ()                                    #good point for recursion
        snake_win.addch(snake_food[0], snake_food[1], '-')         #reset food

    #move the snake
    else:
        end_snake = snake_body.pop()
        snake_win.addch(end_snake[0], end_snake[1], ' ')
        
    snake_win.addch(snake_body[0][0], snake_body[0][1], 'O')        #add a 'O' to snake body
game_over()
