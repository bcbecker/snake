# snake
A classic version of the game snake

This simple game is written using the basic terminal handling module, curses. It modifies the terminal to create a window of specified size and border, where snake is played inside. It also uses randint from the random module to regenerate the '-' at random coordinates within the window.

The escape key (ESC) is used to exit the game, the space bar (SPACE) is used to pause/resume the game, and the up/down/left/right arrow keys are used to navigate the snake.

If the snake's head hits the border, or if it runs over another part of the snake, the game is over.


***NOTE***
I don't believe that the curses module is native to the Windows version of python, so the module must be downloaded using pip or your package manager of choice. If using mac, it should be good to go!

With pip, the command is: python -m pip install windows-curses
