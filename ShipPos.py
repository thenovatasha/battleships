import random

def getShipPos():
    '''
    THIS IS THE LIST OF SHIPS
    [5,3,3,2,2] 
    That is: 
    1x 5 long
    2x 3 long
    2x 2 long

    Your ships must satisfy this 
    Ship positions must be (0-9, 0-9)
    '''
    """
    # GENERATE SHIP POSITIONS
    # List of ships that must be placed
    remaining_ships = [5, 3, 3, 2, 2]
    shipPos = []
    all_pos = []
    # Place ships in a random order
    
    # Put down all ships
    for ship in remaining_ships:
        fits = False
        while (fits == False):
            fits = True
            this_shipPos = []
            if bool(random.getrandbits(1)):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                x_end = x+ship
                for x_counter in range(x, x_end):
                    this_shipPos.append((x_counter, y))
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                y_end = y+ship
                for y_counter in range(y, y_end):
                    this_shipPos.append((x, y_counter))

        shipPos.append(this_shipPos)


    visual = zero_array()
    for ship, num in zip(shipPos, remaining_ships):
        for coord in ship:
            visual[coord[0]][coord[1]] = num
    print_grid(visual)
    """
    shipPos = []
    shipPos.append([[(5,6), (5,7), (5,8)],
                [(3,4), (4,4), (5,4), (6,4), (7,4)],
                [(7,9), (8,9)],
                [(9,4),(9,5),(9,6)],
                [(8,1),(8,2)]])

    # lower board bias with more edge pieces
    shipPos.append([[(3,1), (4,1),(5,1)], 
                [(2,1),(2,2),(2,3),(2,4),(2,5)], 
                [(7,7),(8,7)] , 
                [(0,9), (1,9), (2,9)], 
                [(5,9), (6,9)]])
    
    # quite clumped into middle
    shipPos.append([[(2, 2), (2, 3), (2, 4)],
                [(3, 1), (3,2),(3,3),(3,4),(3,5)],
                [(5,1),(6,1)],
                [(4,7),(4,8),(4,9)],
                [(5,8),(5,9)]])

    return random.choice(shipPos)

def zero_array():
    """ Set the heatmap to all zeros """
    initArray = []
    UNKNOWN = ' '
    for row in range(10):
        initInnerRow = 10*[UNKNOWN]
        initArray.append(initInnerRow)
    return initArray

def print_grid(array):
    for r in range(10):
        for c in range(10):
            print(array[r][c], end=" ")
        print()
    print()