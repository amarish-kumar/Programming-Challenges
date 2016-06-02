###############################################################################################
## Hackrank Challenge - Bot saves princess - 2                                               ##
##      Atrificial Intelligence / Bot Building                                               ##
##                                                                                           ##
## https://www.hackerrank.com/challenges/saveprincess2                                       ##
##                                                                                           ##
## In this version of "Bot saves princess", Princess Peach and bot's position are randomly   ##
## set. Can you save the princess?                                                           ##
##                                                                                           ##
## ====Task====                                                                              ##
## Complete the function nextMove which takes in 4 parameters - an integer N,                ##
## integers r and c indicating the row & column position of the bot and                      ##
## the character array grid - and outputs the next move the bot makes to rescue              ##
## the princess.                                                                             ##
##                                                                                           ##
## ====Input Format====                                                                      ##
## The first line of the input is N (<100), the size of the board (NxN). The second line     ##
## of the input contains two space separated integers, which is the position of the bot.     ##
##                                                                                           ##
## Grid is indexed using Matrix Convention                                                   ##
## https://www.hackerrank.com/scoring/board-convention                                       ##
##                                                                                           ##
## The position of the princess is indicated by the character 'p' and the position of        ##
## the bot is indicated by the character 'm' and each cell is denoted by                     ##
## '-' (ascii value: 45).                                                                    ##
##                                                                                           ##
## ===Output Format====                                                                      ##
## Output only the next move you take to rescue the princess. Valid moves are                ##
## LEFT, RIGHT, UP or DOWN                                                                   ##
##                                                                                           ##
## ====Sample Input==== ====Sample Output==== ====Resultant State====                        ##
## 5                    LEFT                  -----                                          ##
## 2 3                                        -----                                          ##
## -----                                      p-m--                                          ##
## -----                                      -----                                          ##
## p--m-                                      -----                                          ##
## -----                                                                                     ##
## -----                                                                                     ##
##                                                                                           ##
## ====Explanation====                                                                       ##
## As you can see, bot is one step closer to the princess.                                   ##
##                                                                                           ##
## ====Scoring====                                                                           ##
## Your score for every testcase would be (NxN minus number of moves made to rescue          ##
## the princess)/10 where N is the size of the grid (5x5 in the sample testcase).            ##
## Maximum score is 17.5                                                                     ##
###############################################################################################

class Coordinate (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __add__ (coord1, coord2):
        return Coordinate (coord1.x + coord2.x, coord1.y + coord2.y)

    def __sub__ (coord1, coord2):
        return Coordinate (coord1.x - coord2.x, coord1.y - coord2.y)

def nextMove (locM, locP):
    # Calculate delta to princess
    delta = locM - locP

    # Attempt to approach delta (0, 0)

    # If x value is positive, Princess is to the left of Mario
    # If x value is negative, Princess is to the right of Mario
    # If y value is positive, Princess is above Mario
    # If y value is negative, Princess is below Mario

    # Find on which axis character is furthest from princess
    if (abs (delta.x) > abs (delta.y)):
        if delta.x > 0:
            return ("LEFT")
        else:
            return ("RIGHT")
    else:
        if delta.y > 0:
            return ("UP")
        else:
            return ("DOWN")


def procMatrix (n, grid):
    foundP = False # Found Princess flag
    i = 0   # The current row
    j = 0   # The current column

    while (foundP != True):
        # Found a character
        if (grid[i][j] == 'm' or grid[i][j] == 'p'):
            # Found Princess
            if (grid[i][j] == 'p'):
                # Set flag and save location (x, y)
                foundP = True
                locP = Coordinate (j, i)

        # Did not find anything, so continue scanning
        # Move one column to the right
        # If at maxiumum right, move one row down and restart column counting
        j += 1
        if (j == n):
            j = 0
            i += 1

    return (locP)

if __name__ == "__main__":
    n = input ()
    
    loc = raw_input ().split (' ')
    locM = Coordinate (int (loc[1]), int (loc[0]))

    grid = []
    for i in range (0, n):
        grid.append (raw_input ())

    locP = procMatrix (n, grid)
    print nextMove (locM, locP)
