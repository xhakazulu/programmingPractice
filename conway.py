#Conway's Game of Life | An example of Cellular Automata -- a set of rules governing the behavior of a field made up of discrete cells.
#In practice, it creates a pretty animation to look at.


import random, time, copy

WIDTH - 60
HEIGHT = 20

#Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.

    for y in range(HEIGHT):
        if random.randint(0,1) ==0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) #nextCells is a list of column lists.

while True: #Main program loop.
    print('\n\n\n\n\n') #Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighbouring coordinates:
            #'%WIDTH' ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x-1) %WIDTH
            rightCoord = (x+1) %WIDTH
            aboveCoord = (y-1)%HEIGHT
            belowCoord=(y+1)%HEIGHT

            #Count numer of living neighbours:
            
    
