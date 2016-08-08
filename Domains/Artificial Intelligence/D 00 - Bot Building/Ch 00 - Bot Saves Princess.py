###############################################################################################
## Hackrank Challenge - Bot saves princess                                                   ##
##      Atrificial Intelligence / Bot Building                                               ##
##                                                                                           ##
## https://www.hackerrank.com/challenges/saveprincess                                        ##
##                                                                                           ##
## Princess Peach is trapped in one of the four corners of a square grid. You are in the     ##
## center of the grid and can move one step at a time in any of the four directions.         ##
## Can you rescue the princess?                                                              ##
##                                                                                           ##
## ====Input Format====                                                                      ##
## The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid.    ##
## This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot   ##
## position is denoted by 'm' and the princess position is denoted by 'p'.                   ##
##                                                                                           ##
## Grid is indexed using Matrix Convention                                                   ##
## https://www.hackerrank.com/scoring/board-convention                                       ##
##                                                                                           ##
## ====Output Format====                                                                     ##
## Print out the moves you will take to rescue the princess in one go. The moves must be     ##
## separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.            ##
##                                                                                           ##
## ====Sample Input==== ====Smaple Output====                                                ##
## 3                    DOWN                                                                 ##
## ---                  LEFT                                                                 ##
## -m-                                                                                       ##
## p--                                                                                       ##
##                                                                                           ##
## ====Task====                                                                              ##
## Complete the function displayPathtoPrincess which takes in two parameters - the integer   ##
## N and the character array grid. The grid will be formatted exactly as you see it in       ##
## the input, so for the sample input the princess is at grid[2][0]. The function shall      ##
## output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the           ##
## princess. The goal is to reach the princess in as few moves as possible.                  ##
##                                                                                           ##
## The above sample input is just to help you understand the format. The princess ('p')      ##
## can be in any one of the four corners.                                                    ##
##                                                                                           ##
## ====Scoring====                                                                           ##
## Your score is calculated as follows:                                                      ##
## (NxN - number of moves made to rescue the princess)/10, where N is the size of the        ##
## grid (3x3 in the sample testcase).                                                        ##
###############################################################################################
class Coordinate (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __add__ (coord1, coord2):
        return Coordinate (coord1.x + coord2.x, coord1.y + coord2.y)

    def __sub__ (coord1, coord2):
        return Coordinate (coord1.x - coord2.x, coord1.y - coord2.y)

def printPathToPrincess (dir):
    for s in dir:
        print (s)

def calcPathToPrincess (delta):
    # Attempt to get delta tuple to (0, 0)

    # If x value is positive, Princess is to the left of Mario
    # If x value is negative, Princess is to the right of Mario
    # If y value is positive, Princess is above Mario
    # If y value is negative, Princess is below Mario

    # Create list of directions
    directions = list ()
    
    # Process lateral movements
    while (delta.x != 0):
        if delta.x > 0:
            delta.x -= 1
            directions.append ("LEFT")
        elif delta.x < 0:
            delta.x += 1
            directions.append ("RIGHT")
    # Process vertical movements
    while (delta.y != 0):
        if delta.y > 0:
            delta.y -= 1
            directions.append ("UP")
        elif delta.y < 0:
            delta.y += 1
            directions.append ("DOWN")

    return (directions)
    

def procPathToPrincess (m, grid):
    foundP = False # Found Princess flag
    foundM = False # Found Mario flag
    i = 0   # The current row
    j = 0   # The current column

    # Keep searching the matrix until both positions are found.
    while (foundP == False or foundM == False):
        # Found a character
        if (grid[i][j] == 'm' or grid[i][j] == 'p'):
            # Found Mario
            if (grid[i][j] == 'm'):
                # Set flag and save location (x, y)
                foundM = True
                locM = Coordinate (j, i)
            # Found Princess
            elif (grid[i][j] == 'p'):
                # Set flag and save location (x, y)
                foundP = True
                locP = Coordinate (j, i)

        # Did not find anything, so continue scanning
        # Move one column to the right
        # If at maxiumum right, move one row down and restart column counting
        j += 1
        if (j == m):
            j = 0
            i += 1

    # Calculate delta to princess
    delta = locM - locP

    return (delta)

if __name__ == "__main__":
    # Read in size of matrix
    m = int (input ())
    # Create blank matrix
    grid = []

    # Read in each line of matrix
    for i in range (0, m):
        # Split each value of the line and place it in the matrix
        grid.append (raw_input ())

    # Process the current matrix
    delta = procPathToPrincess (m, grid)
    # Calculate movements
    dir = calcPathToPrincess (delta)
    # Print directions
    printPathToPrincess (dir)
