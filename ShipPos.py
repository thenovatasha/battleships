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
    
    # very human, well spread out board without many edge pieces
    shipPos.append([[(3, 2), (3, 3), (3, 4)],
                [(4, 8), (5,8),(6,8),(7,8),(8,8)],
                [(7,2),(8,2)],
                [(5,5),(6,5),(7,5)],
                [(0,7),(1,7)]])

    shipPos.append([[(0, 7), (0, 8), (0, 9)],
                [(9, 0), (9,1),(9,2),(9,3),(9,4)],
                [(2,6),(3,6)],
                [(8,7),(8,8),(8,9)],
                [(5,0),(6,0)]])
    
    shipPos.append([[(2, 7), (2, 8), (2, 9)],
                [(6, 3), (6,4),(6,5),(6,6),(6,7)],
                [(2,3),(3,3)],
                [(3,6),(3,7),(3,8)],
                [(7,1),(8,1)]])
    
    shipPos.append([[(1, 9), (2, 9), (3, 9)],
                [(4, 1), (5,1),(6,1),(7,1),(8,1)],
                [(1,2),(1,3)],
                [(6,7),(7,7),(8,7)],
                [(9,3),(9,4)]])
    
    shipPos.append([[(8, 1), (8, 2), (8, 3)],
                [(5, 6), (6,6),(7,6),(8,6),(9,6)],
                [(0,0),(1,0)],
                [(7,9),(8,9),(9,9)],
                [(6,4),(6,5)]])

    shipPos.append([[(8, 2), (8, 3), (8, 4)],
                [(2, 2), (3,2),(4,2),(5,2),(6,2)],
                [(3,5),(3,6)],
                [(6,7),(7,7),(8,7)],
                [(2,9),(3,9)]])

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